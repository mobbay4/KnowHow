#!/bin/bash
cd ../docs/
make html
cd ../__build__
rm -rf ./docs/*
cp -r ../docs/_build/html/* ./docs
git add .
git commit -am "Update documentation"
git push