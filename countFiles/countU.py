# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 09:20:10 2023

@author: lixianlong
"""

import numpy as np
import scipy.io as io

path = r'/mnt/WRF-Channel02/mywork/Lixl/rKG/monthly_3D_rKG' ## change path
gridName = r'/mnt/WRF-Channel02/mywork/Lixl/grid.mat'
gridData  = io.loadmat(gridName)
Lon = np.array(gridData["Lon"])
Lat = np.array(gridData["Lat"])
Levels = np.array(gridData["Levels"])

month = np.array([12, 1, 2])
year  = np.linspace(2002, 2018, 17, dtype=int)

uData = np.empty([3, 17, 12, Lat.shape[1]])

for j in range(0, 17):
    y = year[j]
    for i in range(0, 3):
        m = month[i]
        filename = path+"//"+str(y)+str(m).zfill(2)+".mat"
        Data = io.loadmat(filename)
        U = np.array(Data["U"])
        uData[i, j, :, :] = np.mean(U, axis=2)
        
uMean = np.mean(np.mean(uData, axis=0), axis=0)
io.savemat(r"/mnt/WRF-Channel02/mywork/Lixl/rKG/picData/u_rKG.mat", {"u":uMean}) ## change  path
        