Dataset conversion script

This repository provides several utility scripts for structural data conversion between various formats commonly used in atomistic simulations. 
These scripts complement dpdata, adding support for conversions involving the extxyz format.

Available Scripts

npy2extxyz.py — Convert DeepMD .npy datasets to EXTXYZ format.

extxyz2npy.py — Convert EXTXYZ structures to DeepMD .npy format.

xyz2pos.py — Convert EXTXYZ files to VASP POSCAR format for single-point calculations.

vasp2npy.py — Convert VASP single-point calculation results to DeepMD .npy format.

extxyz_get_tra_val.py — Extract training and validation subsets from a single EXTXYZ dataset.

data2extxyz.py — Convert LAMMPS data files to EXTXYZ format.

Notes

These scripts aim to simplify dataset preparation for machine-learning interatomic potential training.

Ensure that dpdata, ase, and related dependencies are properly installed before use.

Contributions and improvements are welcome.
