import os
import json
import sys

import numpy as np
from numpy import nan
import argparse
from pymol import cmd

proteins = "1.14.13".split()
# 2.4.1 3.2.2 2.7.10 4.6.1 2.1.1 3.6.4 3.1.4 3.6.5 1.14.13 3.4.21 3.5.1 3.4.19 3.5.2 2.4.2 4.2.1 1.1.1 1.2.1 2.7.11 2.3.1 3.1.3 2.7.1 2.7.4 3.1.1 2.5.1 2.7.7 2.6.1 4.1.1 1.11.1 3.6.1 1.14.14"

data_path = "/mnt/gemini/data/zhenqiaosong/protein_design/geometric_protein_design/models/output/33layer_enzygen_substrate"

esmfold_results_path = "/home/joshuawaibel/esm/esm_results"

rmsds = []
rmsd_dict = {}
# for protein in proteins:
for protein in proteins:
    pdbs = open(os.path.join(data_path, protein, "pdb.txt")).readlines()
    this_rmsds = []
    
    for idx, pdb in enumerate(pdbs):
        # EnzyGen's predictions
        realpdb_path = os.path.join(data_path, protein, f"pred_pdbs/{pdb.strip()}.pdb")
        # ESMFold prediction path - MODIFIED
        esmfold_pdb_path = os.path.join(esmfold_results_path, protein, f"result_{idx}.pdb")
    
        if not os.path.exists(esmfold_pdb_path):
            print(f"Missing ESMFold prediction: {esmfold_pdb_path}")
            continue
        # Load the two protein structures
        cmd.load(realpdb_path, "enzygen")
        cmd.load(esmfold_pdb_path, "esmfold")

        # Perform alignment and get RMSD
        alignment = cmd.align("enzygen", "esmfold")
        this_rmsds.append(alignment[0])
        
        cmd.delete("all")

    if this_rmsds:
        avg_rmsd = np.mean(this_rmsds)
        rmsd_dict[protein] = avg_rmsd
        print(f"{protein}: Avg RMSD = {avg_rmsd:.2f} Å")
    else:
        rmsd_dict[protein] = np.nan
    

print("\nFinal RMSD values:")
for protein, rmsd in rmsd_dict.items():
    print(f"{protein}: {rmsd:.2f} Å")
    
print(f"\nOverall average: {np.nanmean(list(rmsd_dict.values())):.2f} Å")
print(f"{protein}\t{data['average']:.2f} Å\t{len(data['individual'])} structures")