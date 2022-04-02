#!/bin/bash
cd ../master/docs/
make html
cd ../../gh-pages
rm -rf ./docs/*
cp -r ../master/docs/_build/html/* ./docs/
cp -r ../master/docs/_build/doctrees .
git add .
git commit -am "Update documentation"
git push