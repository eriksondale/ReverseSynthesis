from sys import argv as arg
import rdkit
from rdkit import Chem
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
            Draw.MolToFile(mainMol,'./' + arg[1].strip('smi') + '.png')
