#!/bin/bash

NEW_FILES=$(find ./*/* -name "README.md" -a -mtime -1 | wc -l)
if [ $NEW_FILES == 0 ]; then
  echo "No update"
  echo "DO_UPDATE=0" >> $GITHUB_OUTPUT
  exit 0
else
  echo "Need update"
  echo "::group::new problems"
  find ./*/* -name "README.md" -a -mtime -1
  echo "::endgroup::"
  echo "DO_UPDATE=1" >> $GITHUB_OUTPUT
fi

OUTPUT=./README.md
echo "# LeetCode 2nd turn" > $OUTPUT
now=$(date)
echo "### last update: ${now}" >> $OUTPUT


echo "" > /tmp/README.md

runOnLinux=0
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  runOnLinux=1
elif [[ "$OSTYPE" == "darwin"* ]]; then
  runOnLinux=0
else
  echo "$OSTYPE is unsupported. This script works on Linux or macOS only" > stderr
  exit 1
fi


easy=0
medium=0
hard=0
total=0
for file_path in $(find . -name "README.md")
do
  if [ "$file_path" != "./README.md" ]; then
    info=$(head -n 2 "${file_path}")
    name=$(echo ${info} | sed 's/##/#/g' | cut -d '#' -f 2)
    level=$(echo ${info} |  cut -d ':' -f 2 | tr '[:upper:]' '[:lower:]' | tr -d '[:space:]')



    if [ $runOnLinux == 1 ]; then
      modified_epoctime=$(stat -c %Y  ${file_path})
      modified=$(date --date "@${modified_epoctime}" +"%Y-%m-%d %H:%M")
      modified_sort=$(date --date "@${modified_epoctime}" +"%Y%m%d%H%M")
    else
      modified=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M" ${file_path})
      modified_sort=$(stat -f "%Sm" -t "%Y%m%d%H%M" ${file_path})
    fi
    dir_path=$(dirname $file_path)

    if [ "${level}" = "easy" ]; then
      ((easy+=1))
    fi
    if [ "${level}" = "medium" ]; then
      ((medium+=1))
    fi
    if [ "${level}" = "hard" ]; then
      ((hard+=1))
    fi


    echo "${modified_sort}@| [${name}]($dir_path/) | ${level} | ${modified} | " >> /tmp/README.md
  fi
done
((total=easy+medium+hard))
echo "## summary" >> $OUTPUT
echo "| level | counts |" >> $OUTPUT
echo "|-|-|" >> $OUTPUT
echo "| easy |${easy} |" >> $OUTPUT
echo "| medium |${medium} |" >> $OUTPUT
echo "| hard |${hard} |" >> $OUTPUT
echo "| total | ${total} |" >> $OUTPUT
echo "" >> $OUTPUT
echo "## questions" >> $OUTPUT
echo "| problem | level| last modified |" >> $OUTPUT
echo "|-|-|-|" >> $OUTPUT

sort -t'@' -k1 -nr /tmp/README.md  | cut -d'@' -f 2 >> $OUTPUT
rm /tmp/README.md
