#!/usr/bin/env bash
# Deploy the static site from master → gh-pages (served from the branch ROOT).
#
# What gets deployed (and nothing else):
#   static/data/*.json        → data/
#   static/photos/*           → photos/        (adds/updates; removes files deleted on master)
#   static/css/style.css      → css/style.css
#   static/js/{api,app,branches,cytomap,dossier,navigator,search}.js → js/
#   static/index.html is NOT copied automatically — gh-pages keeps its own index.html
#   (master's references Joe's uncommitted cinema/timeline-arc WIP). Pass --index to
#   copy it deliberately, and only after the WIP files are deployed too.
#
# Usage:  tools/deploy_ghpages.sh "Deploy: message" [--index] [--no-push]
set -euo pipefail
cd "$(dirname "$0")/.."

MSG="${1:?commit message required}"; shift || true
COPY_INDEX=0; PUSH=1
for a in "$@"; do
  case "$a" in
    --index) COPY_INDEX=1 ;;
    --no-push) PUSH=0 ;;
  esac
done

if [ -n "$(git status --porcelain -- static/data static/photos static/css/style.css static/js)" ]; then
  echo "!! uncommitted changes under static/ — commit on master first (deploy copies from master's tree)"; exit 1
fi

TMP=$(mktemp -d)
git archive master static/data static/photos static/css/style.css static/js | tar -x -C "$TMP"

git checkout -q gh-pages
# data
rm -f data/*.json; cp "$TMP"/static/data/*.json data/
# photos — mirror
rsync -a --delete "$TMP"/static/photos/ photos/
# css + core js only
cp "$TMP"/static/css/style.css css/style.css
for f in api app branches cytomap dossier navigator search; do cp "$TMP"/static/js/$f.js js/$f.js; done
if [ "$COPY_INDEX" = 1 ]; then git show master:static/index.html > index.html; fi
# keep the meta-description counts in sync with stats.json (gh-pages keeps its own index.html)
python3 - <<'PY'
import json, re
st = json.load(open('data/stats.json'))
e, r = st['entities'], st['relationships']
s = open('index.html').read()
s = re.sub(r'\d[\d,]* entities and \d[\d,]* relationships',
           lambda m: f"{e:,} entities and {r:,} relationships" if ',' in m.group(0) else f"{e} entities and {r} relationships", s)
s = re.sub(r'js/dossier\.js\?v=\d+', 'js/dossier.js?v=14', s)   # safeRelHref photo fix
open('index.html', 'w').write(s)
PY
rm -rf "$TMP"

git add -A data photos css js index.html
if git diff --cached --quiet; then
  echo "nothing to deploy"; git checkout -q master; exit 0
fi
git commit -q -m "$MSG"
echo "gh-pages: $(git rev-parse --short HEAD)"
if [ "$PUSH" = 1 ]; then
  git push -q github gh-pages
  git push -q origin gh-pages || true
fi
git checkout -q master
echo "done"
