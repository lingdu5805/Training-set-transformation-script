#使用ASE将LAMMPS的data格式文件转换为extxyz格式并按y坐标排序
from ase.io import read, write
import numpy as np

# 读取LAMMPS data文件
atoms = read('01-npt.data', format='lammps-data')

# 按y坐标升序排列原子
indices = np.argsort(atoms.positions[:, 1])  # 获取排序索引
sorted_atoms = atoms[indices]                # 创建排序后的原子对象

# 写入extxyz格式文件
write('model.xyz', sorted_atoms, format='extxyz')
