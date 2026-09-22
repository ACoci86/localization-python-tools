import json

def find_missing_keys(source, target):
    source_key = set(source.keys())
    target_key = set(target.keys())

    return source_key - target_key



with open("en.json") as e:
    en = json.load(e)

with open("fr.json") as f:
    fr = json.load(f)


result = find_missing_keys(en, fr)

for key in result:
    print("Missing:", key)

extra = find_missing_keys(fr, en)

for key in extra:
    print("Extra (not in English):", key)