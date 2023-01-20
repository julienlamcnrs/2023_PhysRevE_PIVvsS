#!/usr/local/intel/2020.0.015/intelpython3/bin/python3

import subprocess
from shutil import copyfile
import numpy as np
import glob
import sys
import os


search="zInput/colvar*.out"  # Need to retrieve results from CPA in that folder
listOfFiles=sorted(glob.glob(search))
print (np.size(listOfFiles))

data=np.genfromtxt(listOfFiles[0], usecols=[0,1,2,3])
data[:,3]=0

data_all=data
i=1
for input_file in listOfFiles[1:]:
        data=np.genfromtxt(input_file, usecols=[0,1,2,3])
        data[:,3]=i
        data_all=np.append(data_all,data,axis=0)
        i=i+1


list_S=np.arange(1.13,1.18,0.001)
print (list_S)
for i in np.arange(0,51):
	S=round(list_S[i],3)
	i_tmp=np.argmin(abs(data_all[:,1]-S))
	chosen_file=listOfFiles[int(data_all[i_tmp,-1])].replace("colvar","dump")
	chosen_file=chosen_file.replace("out","lammpstrj")
	chosen_file="../"+chosen_file
	print(str(i).zfill(2),chosen_file,int(data_all[i_tmp,0]/0.005),round(S*1000,1)/1000,data_all[i_tmp,1],data_all[i_tmp,2],data_all[i_tmp,3])


