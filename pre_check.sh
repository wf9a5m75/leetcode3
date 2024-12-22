#!/usr/bin/env bash

# ファイルの最終更新日時を取得
last_commit_date=$(git log -1 --format="%ci" -- README.md)

# 現在の日付と比較して何日前かを計算
days_ago=$(( ($(date -d "$last_commit_date" +%s) - $(date +%s)) / 86400 ))

NEW_FILES=$(find ./*/* \( -name "*.kt" -or -name "*.py" \) -a -mtime $days_ago | wc -l)
if [[ $NEW_FILES -gt 0 ]]; then
  echo "DO_UPDATE=1" >> $GITHUB_OUTPUT
else
  echo "DO_UPDATE=0" >> $GITHUB_OUTPUT
fi
