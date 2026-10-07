"""Failure-oriented checks for sample integrity, not resource compatibility tests."""
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from urllib.parse import urlsplit, unquote

import catalog


class CatalogChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for name in ['data','content','assets','site/prototype']:
            shutil.copytree(catalog.ROOT/name,self.root/name)
        (self.root/'docs').mkdir()
        for name in ['README.md','README.zh-CN.md']:
            shutil.copy2(catalog.ROOT/name,self.root/name)

    def change(self,ident,action):
        path = self.root/'data/resources'/(ident+'.json')
        record = json.loads(path.read_text())
        action(record)
        path.write_text(json.dumps(record))

    def test_release_build_and_scope(self):
        _, records = catalog.validate(self.root)
        with self.assertRaisesRegex(ValueError, '1.0 requires'):
            catalog.release_check(records[:100])
        out = catalog.build(self.root, release=True)
        self.assertEqual(out.name, 'dist')
        self.assertEqual(len(list(out.rglob('*.html'))), 2 * len(records) + 4)
        self.assertNotIn('noindex,nofollow', (out/'en/index.html').read_text())
        (out/'obsolete.html').write_text('old generated page')
        catalog.build(self.root, release=True)
        self.assertFalse((out/'obsolete.html').exists())

    def test_valid_bilingual_fixture(self):
        _, records = catalog.validate(self.root)
        self.assertEqual(len(records),len(list((catalog.ROOT/'data/resources').glob('*.json'))))

    def test_stale_translation_rejected(self):
        self.change('dataview',lambda r:r.update(revision=r['revision']+1))
        with self.assertRaisesRegex(ValueError,'stale revision'):
            catalog.validate(self.root)

    def test_unreviewed_copy_rejected(self):
        path = self.root/'content/en/dataview.md'
        path.write_text(path.read_text()+'\nNew unreviewed claim.\n')
        with self.assertRaisesRegex(ValueError,'without review hash'):
            catalog.validate(self.root)

    def test_dangling_resource_relation_rejected(self):
        self.change('dataview',lambda r:r['related'].append('missing-resource'))
        with self.assertRaisesRegex(ValueError,'dangling/self relation'):
            catalog.validate(self.root)

    def test_image_replacement_requires_review(self):
        path = self.root/'assets/themes/minimal/preview.png'
        path.write_bytes(path.read_bytes()+b'changed')
        with self.assertRaisesRegex(ValueError,'asset checksum mismatch'):
            catalog.validate(self.root)

    def test_hands_on_claim_requires_evidence(self):
        self.change('dataview',lambda r:r['verification'].update(level='hands-on'))
        with self.assertRaisesRegex(ValueError,'hands-on needs'):
            catalog.validate(self.root)

    def test_unknown_price_not_accepted_as_free(self):
        self.change('obsidian-sync',lambda r:r.update(pricing='probably-free'))
        with self.assertRaisesRegex(ValueError,'invalid pricing'):
            catalog.validate(self.root)

    def test_theme_requires_preview(self):
        self.change('things',lambda r:r.update(assets=[]))
        with self.assertRaisesRegex(ValueError,'theme needs preview'):
            catalog.validate(self.root)

    def test_navigation_cannot_omit_duplicate_or_misclassify_resources(self):
        path = self.root/'data/navigation.json'
        original = json.loads(path.read_text())
        for mutation in ['omit','duplicate','category','route']:
            nav = json.loads(json.dumps(original))
            if mutation == 'omit':
                nav['groups'][0]['resources'].pop()
            elif mutation == 'duplicate':
                nav['groups'][0]['resources'].append(nav['groups'][0]['resources'][0])
            elif mutation == 'category':
                nav['groups'][0]['category'] = 'ai'
            else:
                nav['routes'][0]['resources'].append('missing-resource')
            path.write_text(json.dumps(nav))
            with self.assertRaises(ValueError, msg=mutation):
                catalog.validate(self.root)

    def test_unsafe_links_and_unsupported_markup_rejected(self):
        with self.assertRaisesRegex(ValueError,'unsafe link'):
            catalog.inline('[run](javascript:alert)')
        with self.assertRaisesRegex(ValueError,'Unsupported'):
            catalog.markdown('<script>alert(1)</script>')
        with self.assertRaisesRegex(ValueError,'escapes repository'):
            catalog.within(self.root,'../../outside.png')

    def test_generated_links_images_and_language_targets_exist(self):
        out = catalog.build(self.root)
        class Links(HTMLParser):
            def __init__(self):
                super().__init__()
                self.targets=[]
            def handle_starttag(self,tag,attrs):
                for key,value in attrs:
                    if key in ['src','href']:
                        self.targets.append(value)
        pages=list(out.rglob('*.html'))
        self.assertEqual(len(pages),2*len(list((self.root/'data/resources').glob('*.json')))+4)
        for page in pages:
            parser=Links()
            parser.feed(page.read_text())
            for link in parser.targets:
                parsed=urlsplit(link)
                if parsed.scheme or not parsed.path:
                    continue
                target=(page.parent/unquote(parsed.path)).resolve()
                self.assertTrue(target.is_relative_to(out.resolve()),link)
                self.assertTrue(target.exists(),f'{page.name}: {link}')
        self.assertIn('../zh-cn/dataview.html',(out/'en/dataview.html').read_text())
        self.assertIn('../en/dataview.html',(out/'zh-cn/dataview.html').read_text())

    def test_readmes_are_independent_catalogs_and_preserve_manual_prose(self):
        import re
        for name in ['README.md','README.zh-CN.md']:
            path=self.root/name
            path.write_text('Manual introduction\n'+path.read_text()+'\nManual footer\n')
        contract, records=catalog.validate(self.root)
        catalog.write_readmes(self.root,contract,records)
        for lang,name in [('en','README.md'),('zh-cn','README.zh-CN.md')]:
            text=(self.root/name).read_text()
            self.assertTrue(text.startswith('Manual introduction\n'))
            self.assertTrue(text.endswith('Manual footer\n'))
            for r in records:
                self.assertIn('['+r['locales'][lang]['title']+'](',text)
                if r['type'] != 'workflow':
                    self.assertIn(r['sources'][0]['url'],text)
            catalog_text = text.split('<!-- catalog:start -->')[1].split('<!-- catalog:end -->')[0]
            self.assertEqual(catalog_text.count('!['),sum(len(r['assets']) for r in records))
            self.assertIn('](assets/banners/awesome-obsidian.png)', text.split('<!-- catalog:start -->')[0])
            self.assertNotIn('实测',text)
            self.assertNotIn('documentation-reviewed',text)
            self.assertNotIn('**Limits',text)
            self.assertNotIn('localhost',text)
            self.assertNotIn('127.0.0.1',text)
            anchors = re.findall(r'<a id="([^"]+)"></a>',text)
            self.assertEqual(len(anchors), len(set(anchors)))
            for target in re.findall(r'\]\(([^)]+)\)',text):
                if target.startswith('#'):
                    self.assertIn(target[1:], anchors)
                if target.startswith(('https://','#','docs/','CONTRIBUTING')):
                    continue
                self.assertTrue((self.root/target).exists(),target)

    def test_readme_missing_markers_refuses_overwrite(self):
        path=self.root/'README.md'
        path.write_text('User-owned document without generation markers')
        contract,records=catalog.validate(self.root)
        with self.assertRaisesRegex(ValueError,'refusing to overwrite'):
            catalog.write_readmes(self.root,contract,records)
        self.assertEqual(path.read_text(),'User-owned document without generation markers')


if __name__ == '__main__':
    unittest.main()
