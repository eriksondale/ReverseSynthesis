from sys import argv as arg
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw


def isStartingMaterial(molecule):
    # import list of acceptable starting materials
    # iterate through to confirm mol (e.g. Benzene)
    # OR traverse mol graph to confirm all hydrocarbons
    return True
    # or False later.....

def molBreakdown(mainMol, reactLib): # Forseeing issue of competitive rxns; make priority queue of best reactions?
    # Recursively breakdown molecule via a BST until all leaf nodes
    # are consistent with starting materials


    # is mainMol starting?
        # no? find applicable reaction
            # branch left and right
            # if no reaction applicable to

    # Add debug tool to print depth of tree, make flag 



if(len(arg) != 2):
    print('Requires argument: .smi file of select molecule')
else:
    if (arg[1].endswith('.smi')) == False:
        print('Requires .smi file to read..')
    else:
        with open(arg[1],'r') as molFile:
            orgMol = molFile.read()           # FUTURE: Allow user to draw molecule to deconstruct using other lib
            mainMol = Chem.MolFromSmiles(orgMol) # !!!! Make smi mol supplier object
            reactLib = [] # read reaction file library and store as dictionary
                                # key: str of reaction name
                                # value: reaction object

            try:
                molBreakdown(mainMol, reactLib)
            except Exception as e:
                print("Error: " + e)
        print("Done!")
        # Maybe add feature to print image depicting deconstruction of molecule
