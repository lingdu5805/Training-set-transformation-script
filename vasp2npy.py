import os,unittest
import numpy as np
import dpdata
from dpdata import LabeledSystem,MultiSystems
import glob

## All single point structures of vasp are converted into deepmd/npy and deepmd/raw

data = MultiSystems()
aimd_list = glob.glob('calc_**/OUTCAR', recursive=True)
l_d = len(aimd_list)

for idx, aimd_out in enumerate(aimd_list):
    dir_name = os.path.dirname(aimd_out)
    try:
        d1 = dpdata.LabeledSystem(f'{dir_name}/OUTCAR',fmt='vasp/outcar')
        data.append(d1)
        print(f"{dir_name} Processed {idx+1}/{l_d}")
    except:
        print(f"{dir_name} Error")
        continue

print(data)
data.to_deepmd_npy("./deepmd")
data.to_deepmd_raw("./deepmd")
print("outcar to npy, yes")

## All single point structures of vasp are converted into ase track files, which is convenient to see the structure in batches with "ase gui".

for i in range(len(data)):
    natoms=int(data[i].get_atom_numbs()[0])
    data[i].to_ase_traj(f"./deepmd/nepkit-Si{natoms}.traj")

print("outcar to traj, yes")
