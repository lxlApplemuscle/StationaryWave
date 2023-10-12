# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 20:29:33 2023

@author: lixianlong
"""

import numpy    as np
import scipy.io as io

path = r'/mnt/WRF-Channel02/mywork/Lixl/rKG/monthly_3D_rKG' ## change file path
gridName = r'/mnt/WRF-Channel02/mywork/Lixl/grid.mat'
gridData  = io.loadmat(gridName)
Lon = np.array(gridData["Lon"])
Lat = np.array(gridData["Lat"])
Levels = np.array(gridData["Levels"])

month = np.array([12, 1, 2])
year  = np.linspace(2002, 2018, 17, dtype=int)
vData = np.empty([year.shape[0], Levels.shape[1], Lat.shape[1], Lon.shape[1]])
clima_v = np.empty([month.shape[0], Levels.shape[1], Lat.shape[1], Lon.shape[1]])

for j in range(0, 3):
    m = month[j]
    for i in range(0, 17):
        y = year[i]
        filename = path+"//"+str(y)+str(m).zfill(2)+".mat"
        Data = io.loadmat(filename)
        vData[i, :, :, :] = np.array(Data["V"])
    clima_v[j, :, :, :] = np.mean(vData[:, :, :, :], 0)
    
vwData   = np.empty([Levels.shape[1], Lat.shape[1], Lon.shape[1]])
v_month3 = np.empty([3, year.shape[0], Levels.shape[1], Lat.shape[1], Lon.shape[1]])

for i in range(0, 3):
    m = month[i]
    v_all = np.empty([year.shape[0], Levels.shape[1], Lat.shape[1], Lon.shape[1]])
    for j in range(0, 17):
        y = year[j]
        filename = path+"//"+str(y)+str(m).zfill(2)+".mat"
        print(filename)
        Data = io.loadmat(filename)
        vwData[:, :, :] = np.array(Data["V"])
        v_zonalmean = np.empty([Levels.shape[1], Lat.shape[1], Lon.shape[1]])
        for k in range(0, Lon.shape[1]):
            v_zonalmean[:, :, k] = clima_v[i, :, :, k]-np.mean(vwData[:, :, :], axis=2)
        v_all[j, :, :, :] = v_zonalmean
    v_month3[i, :, :, :, :] = v_all
    
v_Ano = np.mean(np.mean(v_month3, axis=0), axis=0)
io.savemat(r"/mnt/WRF-Channel02/mywork/Lixl/rKG/picData/v_rKG.mat", {"v":v_Ano})










