import os
import numpy as np
from pymol import cmd

proteins = "1.14.13".split()

# Configuration
data_path = "/mnt/gemini/data/zhenqiaosong/protein_design/geometric_protein_design/models/output/33layer_enzygen_substrate"

esmfold_path = "/home/joshuawaibel/esm/esm_results"

output_file = "/home/joshuawaibel/EnzyGen/detailed_rmsd_results.csv"

rmsds = []
rmsd_dict = {}

# Initialize results storage
results = {}

for protein in proteins:
    pdbs = open(os.path.join(data_path, protein, "pdb.txt")).readlines()
    protein_results = []
    
    for idx, pdb in enumerate(pdbs):
        enzygen_pdb = os.path.join(data_path, protein, f"pred_pdbs/{pdb.strip()}.pdb")
        esmfold_pdb = os.path.join(esmfold_path, protein, f"result_{idx}.pdb")
        
        if not os.path.exists(esmfold_pdb):
            print(f"Skipping {pdb.strip()} - ESMFold prediction missing")
            continue

        # Load structures
        cmd.load(enzygen_pdb, "enzygen")
        cmd.load(esmfold_pdb, "esmfold")
        
        # Calculate RMSD for Cα atoms only (more meaningful comparison)
        alignment = cmd.align("enzygen & name ca", "esmfold & name ca")
        rmsd = alignment[0]
        
        protein_results.append({
            "pdb_id": pdb.strip(),
            "rmsd": rmsd,
            "sequence_idx": idx
        })
        
        cmd.delete("all")

    # Save detailed results
    results[protein] = {
        "individual": protein_results,
        "average": np.mean([x["rmsd"] for x in protein_results]) if protein_results else np.nan
    }

# Write CSV output
with open(output_file, "w") as f:
    f.write("protein,pdb_id,sequence_idx,rmsd\n")
    for protein, data in results.items():
        for entry in data["individual"]:
            f.write(f"{protein},{entry['pdb_id']},{entry['sequence_idx']},{entry['rmsd']:.2f}\n")

# Print summary
print("\nProtein\tAvg RMSD\tNum Compared")
for protein, data in results.items():
    print(f"{protein}\t{data['average']:.2f} Å\t{len(data['individual'])} structures")
