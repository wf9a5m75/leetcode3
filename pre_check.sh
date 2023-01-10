#!/bin/bash

git log --after 'yesterday' --invert-grep --author='action@github.com'

NEW_FILES=$(git log --after 'yesterday' --invert-grep --author='action@github.com' | wc -l)
git log --after 'yesterday' --invert-grep --author='action@github.com' 
if [[ $NEW_FILES -gt 0 ]]; then
  echo "DO_UPDATE=1" >> $GITHUB_OUTPUT
else
  echo "DO_UPDATE=0" >> $GITHUB_OUTPUT
fi
