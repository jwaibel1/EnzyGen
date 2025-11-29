#!/usr/bin/env python
import time
from rdkit import Chem

# 1) Your exact SMILES list, in order (including duplicates)
SMILES_LIST = [
  "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
              "NC(=O)C1=CN(C=CC1)[C@@H]1O[C@H](COP([O-])(=O)OP([O-])(=O)OC[C@H]2O[C@H]([C@H](OP([O-])([O-])=O)[C@@H]2O)n2cnc3c(N)ncnc23)[C@@H](O)[C@H]1O",
             "NC(=O)C1=CN(C=CC1)[C@@H]1O[C@H](COP([O-])(=O)OP([O-])(=O)OC[C@H]2O[C@H]([C@H](OP([O-])([O-])=O)[C@@H]2O)n2cnc3c(N)ncnc23)[C@@H](O)[C@H]1O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=O)C1=CN(C=CC1)[C@@H]1O[C@H](COP([O-])(=O)OP([O-])(=O)OC[C@H]2O[C@H]([C@H](OP([O-])([O-])=O)[C@@H]2O)n2cnc3c(N)ncnc23)[C@@H](O)[C@H]1O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=O)C1=CN(C=CC1)[C@@H]1O[C@H](COP([O-])(=O)OP([O-])(=O)OC[C@H]2O[C@H]([C@H](OP([O-])([O-])=O)[C@@H]2O)n2cnc3c(N)ncnc23)[C@@H](O)[C@H]1O",
             "NC(=O)C1=CN(C=CC1)[C@@H]1O[C@H](COP([O-])(=O)OP([O-])(=O)OC[C@H]2O[C@H]([C@H](OP([O-])([O-])=O)[C@@H]2O)n2cnc3c(N)ncnc23)[C@@H](O)[C@H]1O",
             "NC(=O)C1=CN(C=CC1)[C@@H]1O[C@H](COP([O-])(=O)OP([O-])(=O)OC[C@H]2O[C@H]([C@H](OP([O-])([O-])=O)[C@@H]2O)n2cnc3c(N)ncnc23)[C@@H](O)[C@H]1O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=O)C1=CN(C=CC1)[C@@H]1O[C@H](COP([O-])(=O)OP([O-])(=O)OC[C@H]2O[C@H]([C@H](OP([O-])([O-])=O)[C@@H]2O)n2cnc3c(N)ncnc23)[C@@H](O)[C@H]1O",
             "NC(=O)C1=CN(C=CC1)[C@@H]1O[C@H](COP([O-])(=O)OP([O-])(=O)OC[C@H]2O[C@H]([C@H](OP([O-])([O-])=O)[C@@H]2O)n2cnc3c(N)ncnc23)[C@@H](O)[C@H]1O",
             "NC(=O)C1=CN(C=CC1)[C@@H]1O[C@H](COP([O-])(=O)OP([O-])(=O)OC[C@H]2O[C@H]([C@H](OP([O-])([O-])=O)[C@@H]2O)n2cnc3c(N)ncnc23)[C@@H](O)[C@H]1O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=O)C1=CN(C=CC1)[C@@H]1O[C@H](COP([O-])(=O)OP([O-])(=O)OC[C@H]2O[C@H]([C@H](OP([O-])([O-])=O)[C@@H]2O)n2cnc3c(N)ncnc23)[C@@H](O)[C@H]1O",
             "NC(=O)C1=CN(C=CC1)[C@@H]1O[C@H](COP([O-])(=O)OP([O-])(=O)OC[C@H]2O[C@H]([C@H](OP([O-])([O-])=O)[C@@H]2O)n2cnc3c(N)ncnc23)[C@@H](O)[C@H]1O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=O)C1=CN(C=CC1)[C@@H]1O[C@H](COP([O-])(=O)OP([O-])(=O)OC[C@H]2O[C@H]([C@H](OP([O-])([O-])=O)[C@@H]2O)n2cnc3c(N)ncnc23)[C@@H](O)[C@H]1O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "NC(=[NH2+])NCCC[C@H]([NH3+])C([O-])=O",
             "Nc1ccccc1C(=O)C[C@H]([NH3+])C([O-])=O",
             "Nc1ccccc1C(=O)C[C@H]([NH3+])C([O-])=O",
             "Nc1ccccc1C(=O)C[C@H]([NH3+])C([O-])=O",
             "Oc1cccc(c1)C([O-])=O",
]

def smiles_to_inchi(smi: str) -> str:

    mol = Chem.MolFromSmiles(smi)
    if mol is None:
        raise ValueError(f"RDKit failed to parse SMILES: {smi}")
    # This requires an RDKit build with InChI support
    inchi = Chem.MolToInchi(mol)
    return inchi

def main():
    print("SMILES\tInChI")
    for smi in SMILES_LIST:
        try:
            inchi = smiles_to_inchi(smi)
        except Exception as e:
            # report parsing/conversion errors without stopping
            print(f"{smi}\tERROR\t{e}")
            continue

        print(f"{smi}\t{inchi}")

if __name__ == "__main__":
    main()
