#!/usr/bin/env bash

NEW_FILES=$(find ./*/* \( -name "*.kt" -or -name "*.py" \) -a -mtime -1 | wc -l)
echo "NEW_FILES: $NEW_FILES"
if [[ $NEW_FILES -gt 0 ]]; then
  echo "DO_UPDATE=1" >> $GITHUB_OUTPUT
else
  echo "DO_UPDATE=0" >> $GITHUB_OUTPUT
fi
