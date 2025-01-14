import glob
import os.path
from typing import List, Dict
import time
import re

def parseReadMe(readMeFilePath: str) -> List[str | List[str]]:
    f = open(readMeFilePath)
    title = ""
    level = ""
    tags = []

    for line in f.readlines():
        line = line.rstrip()
        if line.startswith("# "):
            title = re.sub(r"\#\s", "", line)
        elif "level:" in line:
            level = re.sub(r".*level: ", "", line)
        elif line.startswith("- tag: "):
            tags.append(line.replace("- tag: ", ""))
        elif line.startswith("-tag:"):
            tags.append(line.replace("-tag:", ""))

    f.close()
    return (title, level, tags)

def generateMeta(dirPath: str) -> Dict[str, str| List[str] | bool ]:
    results = {
        "title": "",
        "level": "",
        "tags": [],
        "lastModified": "",
        "languages": set()
    }

    lastModified = 0
    filesInDir = os.listdir(dirPath)
    for file in filesInDir:
        pathParts = os.path.splitext(file)
        filename = pathParts[-2]
        ext = pathParts[-1]
        filePath = f"{dirPath}/{file}"

        if (filename == "README" and ext == ".md"):
            title, level, tags = parseReadMe(filePath)
            results["title"] = title
            results["level"] = level
            results["tags"] = tags
            continue

        lastModified = max(lastModified, os.path.getmtime(filePath))

        match ext:
            case ".py":
                results["languages"].add("python")
                pass
            case ".kt":
                results["languages"].add("kotlin")
                pass
            case ".ts":
                results["languages"].add("typescript")
                pass
            case ".java":
                results["languages"].add("java")
                pass
            case ".go":
                results["languages"].add("go")
                pass

    results["lastModified"] = lastModified

    return results

readMeFiles = glob.glob("./*/README.md")

countLevels = {
    "easy": 0,
    "medium": 0,
    "hard": 0,
}
outputs = []

for file in readMeFiles:
    dirPath = os.path.dirname(file)
    meta = generateMeta(dirPath)
    meta["dirPath"] = dirPath
    meta["tags"] = ", ".join(list(map(lambda it: f"`{it}`", meta["tags"])))

    level = meta["level"].lower()
    if level in countLevels:
        countLevels[level] += 1
    outputs.append(meta)

outputs.sort(
    key = lambda meta: meta["lastModified"],
    reverse = True
)

total = countLevels['easy'] + countLevels['medium'] + countLevels['hard']
last_update_time = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())

with open("./README.md", "w") as f:

    f.write(f"""
# LeetCode 3rd turn
### last update: {last_update_time}
## summary
| level | counts |
|-|-|
| easy | {countLevels['easy']} |
| medium | {countLevels['medium']}  |
| hard | {countLevels['hard']}  |
| total | {total}  |

## questions
| problem | level| tags | last modified | languages |
|-|-|-|-|-|\n""")

    for meta in outputs:
        lastModified = time.strftime("%Y-%m-%d",
                            time.gmtime(meta["lastModified"]))

        languages = " ".join(set(sorted(map(lambda x : f"![](./images/{x}.png)", meta["languages"]))))
        line = f"| [{ meta['title'] }]({ meta['dirPath'] }) | { meta['level'] } | { meta['tags'] }  | { lastModified }  | { languages } |\n"
        f.write(line)
f.close()