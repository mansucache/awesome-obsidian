#!/usr/bin/env python3
"""Record an editor's explicit locale review; never verify sources automatically."""
import argparse
import json
from pathlib import Path
import catalog


def review(root, ident, locales, bump=False):
    if not catalog.ID.fullmatch(ident):
        raise ValueError('invalid resource id')
    path = root/'data/resources'/(ident+'.json')
    record = json.loads(path.read_text())
    if not locales or not set(locales).issubset(record['locales']):
        raise ValueError('choose existing locales that you have actually reviewed')
    # Read every requested body before modifying anything.
    hashes = {lang: catalog.digest(root/'content'/lang/(ident+'.md')) for lang in locales}
    if bump:
        record['revision'] += 1
        for loc in record['locales'].values():
            loc['status'] = 'stale'
    for lang in locales:
        record['locales'][lang].update(status='current', based_on_revision=record['revision'], content_sha256=hashes[lang])
    if any(loc['status'] != 'current' for loc in record['locales'].values()):
        record['publication'] = 'draft'
    path.write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('id')
    parser.add_argument('--reviewed', nargs='+', choices=['en','zh-cn'], required=True)
    parser.add_argument('--bump', action='store_true', help='Increment revision and mark unreviewed locales stale')
    args = parser.parse_args()
    try:
        r = review(catalog.ROOT,args.id,args.reviewed,args.bump)
        print(f"Updated {r['id']} revision {r['revision']}; publication={r['publication']}. Source dates unchanged.")
    except (OSError, ValueError) as exc:
        parser.exit(1,str(exc)+'\n')


if __name__ == '__main__':
    main()
