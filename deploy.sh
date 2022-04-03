#!/bin/bash
source venv/bin/activate
rm -rf site/*
mkdocs build
rm -rf ../gh-pages/docs/*
cp -r site/* ../gh-pages/docs/
cd ../gh-pages
git add --all
git commit -m "Update documentation"
git push
