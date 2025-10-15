import dpdata
import numpy as np
import ase.io

########## train and test ##########
train = []
test = []
train_ratio = 0.8

tol = read("model.xyz", ":", format="extxyz")
random_sample = random.sample(range(len(tol)), int(len(tol)*0.8))
ase.io.write("./train.xyz", [tol[i] for i in random_sample])
ase.io.write("./test.xyz", [tol[i] for i in range(len(tol)) if i not in random_sample])
##########
train = ase.io.read("./train.xyz", ":")
frame_num = len(train)
atom_num = sum([len(s) for s in train])
print(f"frame number of train: {frame_num}")
print(f"atom number of train: {atom_num} \n")

test = ase.io.read("./test.xyz", ":")
frame_num = len(test)
atom_num = sum([len(s) for s in test])
print(f"frame number of test: {frame_num}")
print(f"atom number of test: {atom_num} \n")
