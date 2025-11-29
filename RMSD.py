import os
import json
import sys

import numpy as np
from numpy import nan
import argparse
from pymol import cmd

proteins = "1.14.13"
# 2.4.1 3.2.2 2.7.10 4.6.1 2.1.1 3.6.4 3.1.4 3.6.5 1.14.13 3.4.21 3.5.1 3.4.19 3.5.2 2.4.2 4.2.1 1.1.1 1.2.1 2.7.11 2.3.1 3.1.3 2.7.1 2.7.4 3.1.1 2.5.1 2.7.7 2.6.1 4.1.1 1.11.1 3.6.1 1.14.14"
proteins = proteins.split()

data_path = "/mnt/gemini/data/zhenqiaosong/protein_design/geometric_protein_design/models/output/33layer_enzygen_substrate"

rmsds = []
rmsd_dict = {}
# for protein in proteins:
for protein in proteins:
    pdbs = open(os.path.join(data_path,protein,  "pdb.txt")).readlines()
    real_pdbs = os.listdir(os.path.join(data_path, protein, "pred_pdbs"))
    gen_pdbs = os.listdir(os.path.join(data_path, protein, "af2pdb"))
    this_rmsds = []
    for idx, pdb in enumerate(pdbs):
        realpdb_path = os.path.join(data_path, protein, "pred_pdbs/{}.pdb".format(pdb.strip()))
        genpdb_path = os.path.join(data_path, protein, "af2pdb/beta{}/ranked_0.pdb".format(idx))
        if not (os.path.exists(genpdb_path)):
            continue
        # Load the two protein structures
        cmd.load(realpdb_path, "prot{}1".format(pdb.strip()))
        cmd.load(genpdb_path, "prot{}2".format(pdb.strip()))

        alignment_info = cmd.align("prot{}1".format(pdb.strip()), "prot{}2".format(pdb.strip()))
        # alignment_info is a tuple; the first element is the RMSD.
        print(alignment_info[0])
        this_rmsds.append(alignment_info[0])
    # print(protein)
    # print(np.average(this_rmsds))
    rmsds.append(np.average(this_rmsds))
    rmsd_dict[protein] = np.average(this_rmsds)

print("\n Final RMSD for each protein: \n")
for protein in rmsd_dict:
    print(protein)
    print(rmsd_dict[protein])
    
print("Overall average: %f" % np.average(rmsds))