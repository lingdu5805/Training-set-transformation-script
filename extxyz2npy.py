import dpdata
import ase.io
import os

os.system("sed 's/force/forces/g' selected_structures.xyz > sel.xyz")

d_sel=ase.io.read("sel.xyz", format="extxyz",index=':')

data=dpdata.MultiSystems()

for i in range(len(d_sel)):
    dd=dpdata.LabeledSystem(d_sel[i],fmt="ase/structure")
    data.append(dd)

data.to_deepmd_raw("./deepmd_sel")
data.to_deepmd_npy("./deepmd_sel")
