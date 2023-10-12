# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 21:51:43 2023

@author: lixianlong
"""

import numpy as np
import cmaps
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LatitudeFormatter, LongitudeFormatter
import scipy.io as io
from smooth2D import smooth2D

path = r'D:\python\Stationary wave\channel'
gridData = io.loadmat(path+"\grid.mat")
Lon = np.array(gridData["Lon"])[0, :]
Lat = np.array(gridData["Lat"])[0, :]

vDatactrl = io.loadmat(path+'\\w_500_ctrl')
vall  = np.array(vDatactrl["w_500"])
vDatarKE  = io.loadmat(path+"\\w_500_rKE")
v_rKE = np.array(vDatarKE["w_500"])
v_diff = v_rKE-vall
v_smooth = smooth2D(v_diff, Nr=10, Nc=10)
v_smoall = smooth2D(vall, Nr=15, Nc=15)

fig = plt.figure(dpi = 600, figsize=(8,4))
ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=240))# 创建子图
ax.set_extent([0, 360, 15, 72], crs = ccrs.PlateCarree())
ax.coastlines(linewidth=.5, color='gray')
x_extent = [120, 180, 240, 300, 360]
y_extent = [15, 35, 55, 70]
ax.set_xticks(x_extent, crs=ccrs.PlateCarree())
ax.set_yticks(y_extent, crs=ccrs.PlateCarree())
lon_formatter = LongitudeFormatter(zero_direction_label=False)
lat_formatter = LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
ax.tick_params(length=0)

cmap1 = cmaps.BlueWhiteOrangeRed

lontest = np.linspace(-270, 90, Lon.shape[0])
p0 = ax.contourf(lontest, Lat, v_smooth[:, :], 
                 levels=np.linspace(-0.001, 0.001, 21), cmap=cmap1, extend='both', 
                 transform=ccrs.PlateCarree())
p1 = ax.contour(lontest, Lat, v_smoall[:, :], [-0.008,-0.006,-0.004,-0.002,-0.001,0.001,0.002,0.004,0.006,0.008],colors=['k'],
                linestyles=['-','-','-','-','-','--','--','--','--','--'], linewidths=[0.5],
                transform=ccrs.PlateCarree())
cb0 = fig.colorbar(p0, ax=ax, orientation='horizontal', pad = .1,
                   fraction=0.05)
cb0.ax.tick_params(length=0, labelsize=6)
cb0.set_ticks(np.linspace(-1e-3, 1e-3, 6))
plt.show()

#fig.savefig('w_500_ctrl_rKE.png',dpi=600,bbox_inches='tight',pad_inches=0.05)
