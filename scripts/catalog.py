#!/usr/bin/env python3
"""Validate the bilingual catalog and build its static reading site."""
import argparse
from datetime import date
import hashlib
import html
import json
from pathlib import Path
import re
import shutil
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r'\[([^\]\n]+)\]\(([^\s)]+)\)')
ID = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def https(url):
    parsed = urlsplit(url)
    return parsed.scheme == 'https' and bool(parsed.netloc) and not parsed.username


def within(root, value):
    path = (root / value).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError('Path escapes repository: ' + value)
    return path


def inline(text):
    """Only links are interpreted. All other content is escaped."""
    out, pos = [], 0
    for match in LINK.finditer(text):
        out.append(html.escape(text[pos:match.start()]))
        label, target = match.groups()
        if target.endswith('.md') and ID.fullmatch(target[:-3]):
            target = target[:-3] + '.html'
        elif not https(target):
            raise ValueError('Unsupported or unsafe link: ' + target)
        out.append(f'<a href="{html.escape(target, quote=True)}">{html.escape(label)}</a>')
        pos = match.end()
    out.append(html.escape(text[pos:]))
    return ''.join(out)


def markdown(text):
    """Supported catalog grammar: headings, paragraphs, lists and safe links."""
    out, paragraph, listing = [], [], False

    def flush():
        if paragraph:
            out.append('<p>' + inline(' '.join(paragraph)) + '</p>')
            paragraph.clear()

    for line in text.splitlines():
        if (line.startswith(('```', '~~~', '|', '>', '    ', '\t', '###', '![', '* ', '+ '))
                or re.match(r'\d+\. ', line) or '<' in line or '**' in line or '`' in line):
            raise ValueError('Unsupported catalog Markdown: ' + line[:90])
        if not line.startswith('- ') and listing:
            out.append('</ul>')
            listing = False
        if not line.strip():
            flush()
        elif line.startswith('# '):
            flush()
            out.append('<h1>' + inline(line[2:]) + '</h1>')
        elif line.startswith('## '):
            flush()
            out.append('<h2>' + inline(line[3:]) + '</h2>')
        elif line.startswith('- '):
            flush()
            if not listing:
                out.append('<ul>')
                listing = True
            out.append('<li>' + inline(line[2:]) + '</li>')
        else:
            flush()  # Sample paragraphs are one line; avoid reordering list blocks.
            paragraph.append(line)
    flush()
    if listing:
        out.append('</ul>')
    return '\n'.join(out)


def load(root=ROOT):
    contract = json.loads((root / 'data/catalog-contract.json').read_text())
    contract['navigation'] = json.loads((root / 'data/navigation.json').read_text())
    records = []
    for path in sorted((root / 'data/resources').glob('*.json')):
        record = json.loads(path.read_text())
        if record.get('id') != path.stem:
            raise ValueError(f'{path.name}: filename must match id')
        records.append(record)
    return contract, records


def validate(root=ROOT):
    contract, records = load(root)
    errors = []

    def require(ok, message):
        if not ok:
            errors.append(message)

    ids = [r.get('id') for r in records]
    require(len(ids) == len(set(ids)), 'duplicate ids')
    require(bool(records), 'catalog must contain resources')
    by_id = {r['id']: r for r in records}
    navigation = contract['navigation']
    grouped = []
    for collection in ['groups', 'routes']:
        items = navigation[collection]
        require(len({item['id'] for item in items}) == len(items), 'duplicate navigation ids')
        for item in items:
            require(bool(ID.fullmatch(item['id'])), 'invalid navigation id')
            require(all(item['labels'].get(lang) for lang in contract['locales']), 'missing navigation translation')
            require(bool(item['resources']) and len(set(item['resources'])) == len(item['resources']), 'empty or duplicate navigation resources')
            require(all(ident in by_id for ident in item['resources']), 'dangling navigation resource')
            if collection == 'groups':
                grouped.extend(item['resources'])
                require(item['category'] in contract['categories'], 'unknown navigation category')
                require(all(by_id.get(ident, {}).get('category') == item['category'] for ident in item['resources']), 'navigation category mismatch')
            else:
                require(all(item['descriptions'].get(lang) for lang in contract['locales']), 'missing route description')
    require(len(grouped) == len(set(grouped)) and set(grouped) == set(ids), 'navigation must cover every resource exactly once')
    require(set(contract['categories']).issubset({r.get('category') for r in records}),
            'catalog has an empty primary category')
    urls = []
    for r in records:
        ident = r.get('id', '<missing>')
        try:
            require(set(contract['required_fields']).issubset(r) and not (set(r) - set(contract['required_fields']) - {'editor_approval'}), f'{ident}: unexpected/missing record fields')
            require(bool(ID.fullmatch(ident)), f'{ident}: invalid id')
            for field, enum in [('type','types'),('pricing','pricing'),('openness','openness'),
                                ('level','levels'),('publication','publication'),('status','statuses')]:
                require(r[field] in contract[enum], f'{ident}: invalid {field}')
            require(r['category'] in contract['categories'], f'{ident}: unknown category')
            for field, choices in [('secondary_categories',contract['categories']),
                                   ('scenarios',contract['scenarios']),('platforms',contract['platforms'])]:
                require(isinstance(r[field], list), f'{ident}: {field} must be list')
                require(len(r[field]) == len(set(r[field])), f'{ident}: repeated {field}')
                require(all(v in choices for v in r[field]), f'{ident}: invalid {field}')
            require(bool(r['platforms']) and bool(r['languages']), f'{ident}: empty platform/language')
            require(isinstance(r['license'], str) or r['license'] is None, f'{ident}: invalid license')
            require(type(r['revision']) is int and r['revision'] >= 1, f'{ident}: invalid revision')
            require(len(set(r['related'])) == len(r['related']), f'{ident}: duplicate related id')
            require(all(v in ids and v != ident for v in r['related']), f'{ident}: dangling/self relation')
            require(bool(r['sources']), f'{ident}: missing sources')
            # Original workflows may cite the same primary documentation as a resource.
            if r['type'] != 'workflow':
                urls.append(r['sources'][0]['url'].rstrip('/'))
            for src in r['sources']:
                require(https(src['url']), f'{ident}: invalid source URL')
                require(bool(src['title'].strip()) and bool(src['supports'].strip()), f'{ident}: empty source evidence')
                require(date.fromisoformat(src['checked_at']) <= date.today(), f'{ident}: future source check')
            v = r['verification']
            require(v['level'] in contract['verification_levels'], f'{ident}: invalid verification')
            require(date.fromisoformat(v['date']) <= date.today(), f'{ident}: future verification')
            if v['level'] == 'hands-on':
                require(bool(v.get('environment')) and bool(v.get('result')), f'{ident}: hands-on needs environment/result')
            require(set(r['locales']) == set(contract['locales']), f'{ident}: missing/unexpected locale')
            for lang in contract['locales']:
                loc = r['locales'][lang]
                require(bool(loc['title'].strip()) and bool(loc['summary'].strip()), f'{ident}/{lang}: empty copy')
                require(loc['status'] == 'current', f'{ident}/{lang}: stale translation')
                require(loc['based_on_revision'] == r['revision'], f'{ident}/{lang}: stale revision')
                require(all(bool(r[f][lang].strip()) for f in ['cost_note']), f'{ident}/{lang}: missing cost note')
                require(bool(v['scope'][lang]) and bool(v['limitations'][lang]), f'{ident}/{lang}: missing evidence boundary')
                path = root / 'content' / lang / (ident + '.md')
                text = path.read_text()
                require(digest(path) == loc['content_sha256'], f'{ident}/{lang}: content changed without review hash')
                require(text.startswith('# ' + loc['title'] + '\n'), f'{ident}/{lang}: title mismatch')
                headings = re.findall(r'^## (.+)$', text, re.M)
                required = contract['common_sections'][lang] + contract['type_sections'][r['type']][lang]
                require(all(s in headings for s in required), f'{ident}/{lang}: missing type-specific section')
                require(len(headings) == len(set(headings)), f'{ident}/{lang}: duplicate section')
                for _, target in LINK.findall(text):
                    if target.endswith('.md') and not https(target):
                        require(target[:-3] in ids, f'{ident}/{lang}: dangling Markdown link {target}')
                        require(target[:-3] in r['related'], f'{ident}/{lang}: prose link missing from related')
                    else:
                        require(https(target), f'{ident}/{lang}: unsafe link')
                markdown(text)
            if r['type'] == 'theme':
                require(bool(r['assets']), f'{ident}: theme needs preview')
            for asset in r['assets']:
                path = within(root, asset['path'])
                header = path.read_bytes()[:12]
                valid_image = ((path.suffix == '.png' and header.startswith(b'\x89PNG\r\n\x1a\n')) or
                               (path.suffix == '.webp' and header[:4] == b'RIFF' and header[8:12] == b'WEBP'))
                require(valid_image, f'{ident}: invalid image signature')
                require(digest(path) == asset['sha256'], f'{ident}: asset checksum mismatch')
                require(https(asset['url']) and https(asset['source_page']), f'{ident}: asset source missing')
                require(bool(re.fullmatch('[a-f0-9]{40}', asset['commit'])), f'{ident}: image commit not pinned')
                require(asset['commit'] in asset['url'], f'{ident}: unpinned image URL')
                require(bool(within(root, asset['license_path']).read_text().strip()), f'{ident}: license notice missing')
                require(bool(asset['author']) and bool(asset['rights']), f'{ident}: missing credit/rights')
                require(all(bool(asset['alt'][lang]) for lang in contract['locales']), f'{ident}: missing image alt')
                require(asset['kind'] in ['upstream-preview','maintainer-screenshot'], f'{ident}: invalid image kind')
            if r['publication'] == 'published':
                require(bool(r.get('editor_approval')), f'{ident}: publication requires human editorial approval')
        except (KeyError, ValueError, TypeError, OSError) as exc:
            errors.append(f'{ident}: malformed record/content: {exc}')
    require(len(urls) == len(set(urls)), 'duplicate primary source URLs')
    for lang in contract['locales']:
        require({p.stem for p in (root/'content'/lang).glob('*.md')} == set(ids), f'{lang}: orphan or missing body')
    if errors:
        raise ValueError('\n'.join(errors))
    return contract, records


LABELS = {
    'en': {'title':'Explore the Obsidian ecosystem','intro':'Find a resource. Understand its trade-offs. Build a workflow that fits.',

           'search':'Search resources and scenarios','category':'Category','price':'Cost','all':'All',
           'results':'results','empty':'No matching resources. Clear a filter or try another term.',
           'browse':'Browse by resource','workflow':'Start with a task','gallery':'Theme previews',
           'source':'Sources & review','related':'Related resources','back':'All resources','home':'Community guide',
           'checked':'Documentation checked','limit':'Review boundary','cost':'Cost details','platforms':'Documented platforms',
           'license':'Upstream license','unknown':'Not verified','preview':'Theme preview',
           'credit':'Image credit','notice':'Upstream license notice','footer':'Explore resources, themes and workflows for Obsidian.',
           'skip':'Skip to content','scope':'Review scope','rights':'Repository MIT notice retained; third-party marks remain with their owners.',
           'guide':'Open reading workflow','reset':'Reset filters','nav':'Language'},
    'zh-cn': {'title':'找到适合你的 Obsidian 用法','intro':'发现资源，理解取舍，组合出适合自己的工作流。',

           'search':'搜索资源与使用场景','category':'分类','price':'费用','all':'全部',
           'results':'项结果','empty':'没有匹配结果，请清除筛选或换个词。',
           'browse':'按资源浏览','workflow':'从一个具体任务开始','gallery':'主题预览',
           'source':'来源与核查','related':'关联资源','back':'全部资源','home':'社区生态指南',
           'checked':'文档核查','limit':'验证边界','cost':'费用说明','platforms':'文档支持平台',
           'license':'上游许可','unknown':'未核实','preview':'主题预览',
           'credit':'图片署名','notice':'上游许可原文','footer':'发现 Obsidian 资源、主题与工作流。',
           'skip':'跳到正文','scope':'核查范围','rights':'保留仓库 MIT 许可；图内第三方标识权利归原权利人。',
           'guide':'打开阅读流程','reset':'重置筛选','nav':'语言'}
}
PRICE = {'en':{'free':'Free','paid':'Paid','optional-payment':'Optional payment','unknown':'Unknown','not-applicable':'Not applicable'},
         'zh-cn':{'free':'免费','paid':'收费','optional-payment':'可选付费','unknown':'未核实','not-applicable':'不适用'}}
PLATFORM_ZH = {'windows':'Windows','macos':'macOS','linux':'Linux','ios':'iOS','android':'Android','browser':'浏览器','agent-dependent':'取决于 Agent','not-applicable':'不适用','unknown':'未核实'}
E = html.escape


def shell(lang, title, body, page='index.html', script=False):
    ui = LABELS[lang]
    other = 'zh-cn' if lang == 'en' else 'en'
    switch = '简体中文' if other == 'zh-cn' else 'English'
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>{E(title)} · Awesome Obsidian</title>
<link rel="stylesheet" href="../style.css"></head><body>
<a class="skip" href="#main">{ui['skip']}</a><header><a class="brand" href="index.html"><span class="mark">◇</span> Awesome Obsidian</a>
<nav aria-label="{ui['nav']}"><span>{ui['home']}</span><a lang="{other}" hreflang="{other}" href="../{other}/{page}">{switch}</a></nav></header>
<main id="main">{body}</main><footer>{ui['footer']} · <a href="../credits.html">{ui['credit']}</a></footer>
{'<script src="../catalog.js" defer></script>' if script else ''}</body></html>'''


def cards(contract, records, lang):
    result = []
    topics = {ident:g for g in contract['navigation']['groups'] for ident in g['resources']}
    for r in records:
        loc = r['locales'][lang]
        # Search is bilingual even when the surrounding interface is not.
        search = ' '.join([loc['title'] + ' ' + loc['summary'] for loc in r['locales'].values()] +
                          r['tags'] + [label for s in r['scenarios'] for label in contract['scenarios'][s].values()])
        topic = topics[r['id']]
        search += ' ' + ' '.join(topic['labels'].values())
        result.append(f'''<article class="card" data-record data-category="{r['category']} {' '.join(r['secondary_categories'])}" data-topic="{topic['id']}" data-price="{r['pricing']}" data-search="{E(search,quote=True)}">
<p class="eyebrow">{E(topic['labels'][lang])} <span>{PRICE[lang][r['pricing']]}</span></p>
<h3><a href="{r['sources'][0]['url'] if r['type'] != 'workflow' else r['id'] + '.html'}">{E(loc['title'])}</a></h3><p>{E(loc['summary'])}</p>
</article>''')
    return ''.join(result)


def readme_catalog(root, contract, records, lang):
    """Compact Markdown catalog, independently readable without the website."""
    zh = lang == 'zh-cn'
    by_id = {r['id']:r for r in records}
    total, themes, guides = len(records), sum(r['type']=='theme' for r in records), sum(r['type']=='workflow' for r in records)
    stats = f'{total} 条内容 · {themes} 个带图主题 · {guides} 篇场景指南' if zh else f'{total} entries · {themes} illustrated themes · {guides} workflow guides'
    lines = [stats, '', '## '+('从你想做的事开始' if zh else 'Start with a task'), '',
             '| '+('我想…… | 可以从这里开始' if zh else 'I want to… | Start here')+' |', '| --- | --- |']
    for route in contract['navigation']['routes']:
        links = ' · '.join(f'[{by_id[ident]["locales"][lang]["title"]}](#resource-{ident})' for ident in route['resources'])
        lines.append(f'| {route["labels"][lang]} | {links} |')
    lines += ['', '## '+('目录' if zh else 'Contents'), '']
    for key, labels in contract['categories'].items():
        count = sum(r['category'] == key for r in records)
        lines.append(f'- [{labels[lang]}](#category-{key}) · {count}')
    lines.append('')
    for key, labels in contract['categories'].items():
        lines += [f'<a id="category-{key}"></a>', '', '## '+labels[lang], '']
        if key == 'ai':
            lines += [('模型 API、订阅与云服务可能单独收费。' if zh else 'Model APIs, subscriptions and cloud services may have separate costs.'), '']
        groups = [g for g in contract['navigation']['groups'] if g['category'] == key]
        if len(groups) > 1:
            lines += [' · '.join(f'[{g["labels"][lang]}](#topic-{g["id"]})' for g in groups), '']
        for group in groups:
            if len(groups) > 1:
                lines += [f'<a id="topic-{group["id"]}"></a>', '', '### '+group['labels'][lang], '']
            for ident in group['resources']:
                r = by_id[ident]
                loc = r['locales'][lang]
                target = f'content/{lang}/{r["id"]}.md' if r['type']=='workflow' else r['sources'][0]['url']
                badge = f' · {PRICE[lang][r["pricing"]]}' if r['pricing'] in ['paid','optional-payment'] else ''
                lines += [f'- <a id="resource-{ident}"></a>[{loc["title"]}]({target}) — {loc["summary"]}{badge}']
                for a in r['assets']:
                    lines += ['', f'![{a["alt"][lang]}]({a["path"]})', '']
            lines.append('')
        lines.append('')
    return '\n'.join(lines).rstrip()+'\n'


def write_readmes(root, contract, records):
    for lang, name in [('en','README.md'),('zh-cn','README.zh-CN.md')]:
        path = root/name
        text = path.read_text()
        start,end = '<!-- catalog:start -->','<!-- catalog:end -->'
        if text.count(start) != 1 or text.count(end) != 1 or text.index(start) > text.index(end):
            raise ValueError(name+': expected one ordered catalog marker pair; refusing to overwrite prose')
        prefix, rest = text.split(start)
        _, suffix = rest.split(end)
        path.write_text(prefix+start+'\n'+readme_catalog(root,contract,records,lang)+end+suffix)


def release_check(records):
    counts = (len(records), sum(r['type'] == 'theme' for r in records),
              sum(r['type'] == 'workflow' for r in records))
    if any(actual < minimum for actual, minimum in zip(counts, (220, 15, 6))):
        raise ValueError('1.0 requires at least 220 entries, 15 illustrated themes and 6 workflows')


def build(root=ROOT, release=False):
    contract, records = validate(root)
    if release:
        release_check(records)
    write_readmes(root, contract, records)
    out = root / ('site/dist' if release else 'site/preview')
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True, exist_ok=True)
    for name in ['style.css','catalog.js']:
        shutil.copy2(root/'site/prototype'/name, out/name)
    for r in records:
        for asset in r['assets']:
            for field in ['path','license_path']:
                dest = out/asset[field]
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(root/asset[field],dest)
    for lang in contract['locales']:
        directory = out/lang
        directory.mkdir(exist_ok=True)
        ui = LABELS[lang]
        options = ''.join(f'<option value="{key}">{E(val[lang])}</option>' for key,val in contract['categories'].items())
        topics = ''.join(f'<option value="{g["id"]}">{E(contract["categories"][g["category"]][lang])} / {E(g["labels"][lang])}</option>' for g in contract['navigation']['groups'])
        prices = ''.join(f'<option value="{key}">{val}</option>' for key,val in PRICE[lang].items())
        links = ''.join(f'<a class="chip" href="?category={key}#catalog">{E(val[lang])} · {sum(r["category"] == key or key in r["secondary_categories"] for r in records)}</a>' for key,val in contract['categories'].items())
        by_id = {r['id']:r for r in records}
        routes = []
        for route in contract['navigation']['routes']:
            choices = []
            for ident in route['resources']:
                r = by_id[ident]
                target = ident+'.html' if r['type']=='workflow' else r['sources'][0]['url']
                choices.append(f'<a href="{E(target,quote=True)}">{E(r["locales"][lang]["title"])}</a>')
            routes.append(f'<article class="route"><h3>{E(route["labels"][lang])}</h3><p>{E(route["descriptions"][lang])}</p><p>{" · ".join(choices)}</p></article>')
        gallery = ''.join(f'''<a class="theme" href="{r['id']}.html"><img src="../{r['assets'][0]['path']}" alt="{E(r['assets'][0]['alt'][lang],quote=True)}" loading="lazy"><span>{E(r['locales'][lang]['title'])}</span></a>''' for r in records if r['type']=='theme')
        themes = sum(r['type']=='theme' for r in records)
        guides = sum(r['type']=='workflow' for r in records)
        stats = f'{len(records)} 条内容 · {themes} 个带图主题 · {guides} 篇场景指南' if lang=='zh-cn' else f'{len(records)} entries · {themes} illustrated themes · {guides} workflow guides'
        body = f'''<section class="hero"><h1>{ui['title']}</h1><p class="intro">{ui['intro']}</p><p>{stats}</p><div class="chips"><a class="chip" href="#catalog">{ui['search']}</a><a class="chip" href="#theme-gallery">{ui['gallery']}</a></div></section>
<section><h2>{ui['workflow']}</h2><div class="routes">{''.join(routes)}</div></section>
<section aria-labelledby="browse"><h2 id="browse">{ui['browse']}</h2><div class="chips">{links}</div></section>
<section id="catalog"><div class="filters"><label class="search">{ui['search']}<input id="search" type="search" placeholder="Dataview, 阅读, AI…" autocomplete="off"></label>
<label>{ui['category']}<select id="category"><option value="">{ui['all']}</option>{options}</select></label>
<label>{'用途' if lang=='zh-cn' else 'Topic'}<select id="topic"><option value="">{ui['all']}</option>{topics}</select></label>
<label>{ui['price']}<select id="price"><option value="">{ui['all']}</option>{prices}</select></label><button id="reset" type="button">{ui['reset']}</button></div>
<p id="count" role="status" aria-live="polite" data-suffix="{ui['results']}">{len(records)} {ui['results']}</p>
<p>{'费用指资源本身，模型 API 与托管服务可能单独收费。' if lang=='zh-cn' else 'Costs refer to the resource itself; model APIs and hosting may be billed separately.'}</p>
<p id="empty" hidden>{ui['empty']}</p><div class="grid">{cards(contract,records,lang)}</div></section>
<section id="theme-gallery"><h2>{ui['gallery']}</h2><div class="gallery">{gallery}</div></section>'''
        (directory/'index.html').write_text(shell(lang,ui['title'],body,script=True))
        for r in records:
            loc = r['locales'][lang]
            text = (root/'content'/lang/(r['id']+'.md')).read_text()
            body = f'<a class="back" href="index.html">← {ui["back"]}</a><div class="article">' + markdown(text)
            for asset in r['assets']:
                body += f'<figure><a href="../{asset["path"]}"><img src="../{asset["path"]}" alt="{E(asset["alt"][lang],quote=True)}"></a></figure>'
            related = [x for x in records if x['id'] in r['related'] or r['id'] in x['related']]
            if related:
                body += f'<h2>{ui["related"]}</h2><ul>' + ''.join(f'<li><a href="{x["id"]}.html">{E(x["locales"][lang]["title"])}</a></li>' for x in related) + '</ul>'
            body += '</div>'
            (directory/(r['id']+'.html')).write_text(shell(lang,loc['title'],body,page=r['id']+'.html'))
        title = 'Resource catalog' if lang=='en' else '资源目录'
        catalog_text = readme_catalog(root,contract,records,lang)
        catalog_text = LINK.sub(lambda m: f'[{m[1]}](../{m[2]})' if m[2].startswith(('content/','assets/')) else m[0], catalog_text)
        lines = [f'# {title}', '', '[English](../README.md) · [中文](../README.zh-CN.md)', '', catalog_text,
                 '[Image credits / 图片来源与许可](../assets/README.md)', '']
        (root/'docs'/f'samples.{lang}.md').write_text('\n'.join(lines))
    credits = ['<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Image credits</title></head><body><h1>Image credits / 图片来源与许可</h1>']
    for r in records:
        for asset in r['assets']:
            credits.append(f'<p>{E(r["locales"]["en"]["title"])} — {E(asset["author"])} · <a href="{E(asset["source_page"],quote=True)}">Source</a> · <a href="{asset["license_path"]}">License</a></p>')
    credits.append('</body></html>')
    (out/'credits.html').write_text(''.join(credits))
    (out/'index.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex,nofollow"><meta http-equiv="refresh" content="0;url=en/index.html"><title>Awesome Obsidian</title></head><body><a href="en/index.html">English</a> · <a href="zh-cn/index.html">简体中文</a></body></html>')
    if release:
        for page in out.rglob('*.html'):
            page.write_text(page.read_text().replace('<meta name="robots" content="noindex,nofollow">', ''))
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['check','build'])
    parser.add_argument('--release', action='store_true', help='Check 1.0 scope and build site/dist')
    args = parser.parse_args()
    try:
        if args.command == 'build':
            print('Built static site:', build(release=args.release))
        else:
            _, records = validate()
            if args.release:
                release_check(records)
            print(f'PASS: {len(records)} records, {len(records)*2} localized pages, source/relationship/image checks')
    except (ValueError,OSError) as exc:
        parser.exit(1,str(exc)+'\n')


if __name__ == '__main__':
    main()
