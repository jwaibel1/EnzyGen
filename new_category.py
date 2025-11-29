import json

# load the full test split (adjust path as needed)
with open('preprocess/case.json') as fin:
    all_cases = json.load(fin)

# filter on ec4
filtered = [c for c in all_cases if c['ec4'] == '2.1.1.67']

# write out your custom case file
out = {'cases': filtered}
with open('preprocess/test_ec2_1_1_67.json', 'w') as fout:
    json.dump(out, fout, indent=2)
