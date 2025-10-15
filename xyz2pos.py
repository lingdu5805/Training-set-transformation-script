import os
from ase import io

# 读入所有结构
structures = io.read("./structure_sel_100_frames.xyz", index=":")
# 批量转化为子文件夹的POSCAR
for i, atoms in enumerate(structures):
    workdir = f"calc_{i:04d}"
    os.makedirs(workdir, exist_ok=True)
    # POSCAR
    io.write(os.path.join(workdir, "POSCAR"), atoms, format="vasp", vasp5=True, direct=True)
