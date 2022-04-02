#!/bin/bash
cd ../master/docs/
make html
cd ../../gh-pages
ls
#rm -rf ./docs/*
cp -r ../master/docs/_build/html/* ./docs
git add .
git commit -am "Update documentation"
git push