import json

# 1. Load the mapping from paste.txt (saved as mapping.json)
with open("mapping.json") as f:
    pdb_to_substrate = json.load(f)  # keys like "2ort.A" and values like "NC(=[NH2+])NCCC[C@H]…"[1]

# 2. Your list of PDB IDs
pdbs = [
    "2ort.A","1m9q.A","6pp1.A","3dqs.A","3dqt.A","6pp2.A","3pnh.A","4gqe.A",
    "4k5d.A","4cdt.A","3nnz.A","3n5z.A","5vul.A","4k5g.A","5fw0.A","4v3y.A",
    "4upp.A","3tyn.A","3n61.A","5unw.A","5agk.A","1jwj.A","5agl.A","7s3z.A",
    "6nh0.A","7tsb.A","3e6o.A","5vv2.A","5vux.A","5vv0.A","6ngz.A","6ngf.A",
    "5adf.A","6nga.A","1nse.A","6ngc.A","5vv3.A","5nse.A","1d1w.A","3e65.A",
    "1qw5.A","6po8.A","1vag.A","1df1.A","1zvl.A","3eai.A","5y66.A","5mzi.A",
    "6foy.A","2dkh.A"
]

# 3. Lookup and print results
for pdb in pdbs:
    substrate = pdb_to_substrate.get(pdb)
    if substrate is None:
        substrate = "NOT FOUND"
    print(f"{pdb}\t{substrate}")
