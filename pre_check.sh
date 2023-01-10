#!/usr/bin/env bash

#NEW_COMMITS=$(git log --after 'yesterday' --invert-grep --author='action@github.com')
git version
NEW_COMMITS=$(git log --since 'yesterday' --invert-grep --author='action@github.com' | wc -l )
echo "NEW COMMITS: $NEW_COMMITS"
if [[ $NEW_COMMITS -gt 0 ]]; then
  echo "DO_UPDATE=1" >> $GITHUB_OUTPUT
else
  echo "DO_UPDATE=0" >> $GITHUB_OUTPUT
fi
