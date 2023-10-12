# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 09:37:48 2023

@author: lixianlong
"""

import numpy as np
import scipy.io as io

path = r'/mnt/WRF-Channel02/mywork/Lixl/rKG/monthly_3D_rKG'
gridName = r'/mnt/WRF-Channel02/mywork/Lixl/grid.mat'
gridData = io.loadmat(gridName)
Lon = np.array(gridData["Lon"])
Lat = np.array(gridData["Lat"])
Levels = np.array(gridData["Levels"])

month  = np.array([12, 1, 2])
year   = np.linspace(2002, 2018, 17, dtype=int)
vwData = np.empty([51, 12, Lat.shape[1], Lon.shape[1]])
n = 0

for i in range(0, 3):
    m = month[i]
    for j in range(0, 17):
        y = year[j]
        filename = path+"//"+str(y)+str(m).zfill(2)+".mat"
        Data = io.loadmat(filename)
        vwData[n, :, :, :] = np.array(Data["V"])
        n = n+1

## monthly V*2
zonal_mean_v = np.mean(vwData, axis=3)
bb = np.expand_dims(zonal_mean_v, 3).repeat(Lon.shape[1], axis=3)
month_v_star = vwData-bb
month_v_star = np.single(month_v_star)
month_var = np.var(month_v_star, axis=0)
## subseasonal V*
sea_v = np.mean(vwData.reshape([3, 17, 12, Lat.shape[1], Lon.shape[1]]), axis=0)
zonal_mean_sea_v = np.mean(sea_v, axis=3)
sea_v_star = sea_v-np.expand_dims(zonal_mean_sea_v, axis=3).repeat(Lon.shape[1], axis=3)
sea_v_star = np.single(sea_v_star)
sea_var = np.var(sea_v_star, axis=0)

subsea_var_v_star = month_var-sea_var
subsea_var_v_star = np.single(subsea_var_v_star)
io.savemat(r"/mnt/WRF-Channel02/mywork/Lixl/rKG/picData/v2_rKG.mat", {"v2":subsea_var_v_star})




