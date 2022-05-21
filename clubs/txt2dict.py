#!python3

import json

with open("clubs_map.txt", "r", encoding="utf8") as f:
    out = dict()
    for line in f.readlines():
        abbr, ext = line.split(":")
        out[abbr] = ext[:-1]
    f.close()

print(json.dumps(out))
