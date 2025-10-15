import dpdata
import numpy as np
import ase.io
import os

filelist=['init.000', 'init.001', 'init.002', 'sys.Si64', 'sys.Si72']

data = dpdata.MultiSystems()

#read npy 
for i in filelist :
    d=dpdata.LabeledSystem(f'./collect_data/{i}',fmt='deepmd/npy')
    data.append(d)

#npy convert to extxyz
for i in range(len(data)):
    dd = data[i].to_ase_structure()
    natoms = data[i].get_natoms()
    ase.io.write(f"model_{natoms}.xyz", dd, format="extxyz")

os.system("cat model_*.xyz > model.xyz")
