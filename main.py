from sys import argv as arg
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw

if(len(arg) != 2):
    print('Requires argument: .smi file')
else:
    if (arg[1].endswith('.smi')) == False:
        print('Requires .smi file to read..')
    else:
        with open(arg[1],'r') as molFile:
            orgMol = molFile.read()
            mainMol = Chem.MolFromSmiles(orgMol)
            #rxn = AllChem.ReactionFromSmarts()
            #reactant = []
            #reactant.append(mainMol)
            #product = rxn.RunReactants(reactant)
            #for prod in product:
                #for pair in prod:
                    #print(AllChem.MolToSmiles(pair))
            Draw.MolToFile(mainMol,'./' + arg[1].strip('.smi') + '.png')
