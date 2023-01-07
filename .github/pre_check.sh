#!/bin/bash

NEW_FILES=$(git log --after 'yesterday' --invert-grep --author='action@github.com' | wc -l)
if [[ $NEW_FILES -gt 0 ]]; then
  echo "::set-output name=DO_UPDATE::1"
else
  echo "::set-output name=DO_UPDATE::0"
fi
