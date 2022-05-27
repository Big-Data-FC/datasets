#!python3

import json
import csv

with open("clubs_map.csv", "r", encoding="utf8") as f:
    out = dict()
    reader = csv.reader(f, delimiter=",", quotechar='"')
    reader.__next__()  # skip header
    for row in reader:
        abbr, ext = row[0], row[3]
        out[abbr] = ext
f.close()

with open("clubs_map.json", "w", encoding="utf8") as f:
    json.dump(out, f, ensure_ascii=False)
