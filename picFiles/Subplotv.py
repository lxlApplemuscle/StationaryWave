# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 09:37:12 2023

@author: lixianlong
"""

import numpy as np
import cmaps
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LatitudeFormatter, LongitudeFormatter
import scipy.io as io
#from smooth2D import smooth2D

path = r'D:\python\Stationary wave\channel'
gridData = io.loadmat(path+"\grid.mat")
Lon = np.array(gridData["Lon"])[0, :]
Lat = np.array(gridData["Lat"])[0, :]

lev1 = 9 #300hPa
lev2 = 7 #500hPa

vDatactrl = io.loadmat(path+'\\v_ctrl')
v_ctrl  = np.array(vDatactrl["v_300"])
vDatarGS  = io.loadmat(path+"\\v_rKG")
v_rGS = np.array(vDatarGS["v"])
v_diff_300 = v_rGS[lev1, :, :] - v_ctrl[lev1, :, :]
v_diff_500 = v_rGS[lev2, :, :] - v_ctrl[lev2, :, :]

fig = plt.figure(dpi = 600, figsize=(8,4))
ax = fig.add_subplot(211,projection=ccrs.PlateCarree(central_longitude=240))# 创建子图
ax.set_extent([0, 360, 15, 72], crs = ccrs.PlateCarree())
ax.coastlines(linewidth=.5, color='gray')
x_extent = [120, 180, 240, 300, 360]
y_extent = [15, 35, 55, 70]
#ax.set_xticks(x_extent, crs=ccrs.PlateCarree())
ax.set_yticks(y_extent, crs=ccrs.PlateCarree())
#lon_formatter = LongitudeFormatter(zero_direction_label=False)
lat_formatter = LatitudeFormatter()
#ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
ax.tick_params(length=0)

ax1 = fig.add_subplot(212,projection=ccrs.PlateCarree(central_longitude=240))# 创建子图
ax1.set_extent([0, 360, 15, 72], crs = ccrs.PlateCarree())
ax1.coastlines(linewidth=.5, color='gray')
ax1.set_xticks(x_extent, crs=ccrs.PlateCarree())
ax1.set_yticks(y_extent, crs=ccrs.PlateCarree())
lon_formatter = LongitudeFormatter(zero_direction_label=False)
lat_formatter = LatitudeFormatter()
ax1.xaxis.set_major_formatter(lon_formatter)
ax1.yaxis.set_major_formatter(lat_formatter)
ax1.tick_params(length=0)

fig.subplots_adjust(hspace=-0.4)

cmap1 = cmaps.BlueWhiteOrangeRed

lontest = np.linspace(-270, 90, Lon.shape[0])
p0 = ax.contourf(lontest, Lat, v_diff_300[:, :], 
                 levels=np.linspace(-1, 1, 21), cmap=cmap1, extend='both', 
                 transform=ccrs.PlateCarree())
p1 = ax.contour(lontest, Lat, v_ctrl[lev1, :, :], [-15,-12,-9,-6,-3,3,6,9,12,15],colors=['k'],
                linestyles=['--','--','--','--','--','-','-','-','-','-'], linewidths=[0.5],
                transform=ccrs.PlateCarree())
ax.text(lontest[350], Lat[240], r"(a)$V^{*}_{300}$", va="center")

p2 = ax1.contourf(lontest, Lat, v_diff_500[:, :], 
                 levels=np.linspace(-1, 1, 21), cmap=cmap1, extend='both', 
                 transform=ccrs.PlateCarree())
p3 = ax1.contour(lontest, Lat, v_rGS[lev2, :, :], [-10,-8,-6,-4,-2,2,4,6,8,10],colors=['k'],
                linestyles=['--','--','--','--','--','-','-','-','-','-'], linewidths=[0.5],
                transform=ccrs.PlateCarree())
ax1.text(lontest[350], Lat[240], r"(b)$V^{*}_{500}$", va="center")
cb0 = fig.colorbar(p0, ax=ax1, orientation='horizontal', pad = .125,
                   fraction=0.1)
cb0.ax.tick_params(length=0, labelsize=6)
cb0.set_ticks(np.linspace(-1, 1, 11))
plt.show()

#fig.savefig('v_300_500_KG.png',dpi=600,bbox_inches='tight',pad_inches=0.05)

