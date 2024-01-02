#!/bin/bash

cd content

for file in *.md; do
    pandoc -s --from=gfm --to=html5 --mathjax "$file" -o "../articles/${file%.md}.html"
done

cd -
