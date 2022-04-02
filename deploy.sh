#!/bin/bash
cd ../master
source venv/bin/activate
mkdocs build 
cd ../gh-pages
rm -rf ./docs/*
cp -r ../master/site/* ./docs
git add .
git commit -am "Update documentation"
git push