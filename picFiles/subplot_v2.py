# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:00:32 2023

@author: lixianlong
"""

import numpy as np
import cmaps
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LatitudeFormatter, LongitudeFormatter
import scipy.io as io

path = r'D:\python\Stationary wave\channel'
gridData = io.loadmat(path+"\grid.mat")
Lon = np.array(gridData["Lon"])[0, :]
Lat = np.array(gridData["Lat"])[0, :]

v2Data_ctrl = io.loadmat(path+"\\v2_ctrl")
v2Data_rKE  = io.loadmat(path+"\\Ctrl_rKE\\v2_rKE")
v2Data_rGS  = io.loadmat(path+"\\rGS\\v2_rGS")
v2Data_rKG  = io.loadmat(path+"\\rKG\\v2_rKG")

v2_ctrl = np.array(v2Data_ctrl["v2"])
v2_rKE  = np.array(v2Data_rKE["v2"])
v2_rGS  = np.array(v2Data_rGS["v2"])
v2_rKG  = np.array(v2Data_rKG["v2"])

v2Diff_rKE = v2_rKE[9, :, :]-v2_ctrl[9, :, :]
v2Diff_rGS = v2_rGS[9, :, :]-v2_ctrl[9, :, :]
v2Diff_rKG = v2_rKG[9, :, :]-v2_ctrl[9, :, :]

fig = plt.figure(dpi = 600, figsize=(8,4))
cmap1 = cmaps.BlueWhiteOrangeRed
x_extent = [120, 180, 240, 300, 360]
y_extent = [15, 35, 55, 70]
lontest = np.linspace(-270, 90, Lon.shape[0])

ax1 = fig.add_subplot(311,projection=ccrs.PlateCarree(central_longitude=240))# 创建子图
ax1.set_extent([0, 360, 15, 72], crs = ccrs.PlateCarree())
ax1.coastlines(linewidth=.5, color='gray')
ax1.set_yticks(y_extent, crs=ccrs.PlateCarree())
lat_formatter = LatitudeFormatter()
ax1.yaxis.set_major_formatter(lat_formatter)
ax1.tick_params(length=0)
p10 = ax1.contourf(lontest, Lat, v2Diff_rKE[:, :], 
                 levels=np.linspace(-10, 10, 21), cmap=cmap1, extend='both', 
                 transform=ccrs.PlateCarree())
p11 = ax1.contour(lontest, Lat, v2_ctrl[9, :, :], [0,4,8,12,16,20],colors=['k'],
                linestyles=['-'], linewidths=[0.5],
                transform=ccrs.PlateCarree())
ax1.text(lontest[350], Lat[240], r"(a)rKE", va="center", fontdict={"weight":"bold"})

ax2 = fig.add_subplot(312,projection=ccrs.PlateCarree(central_longitude=240))# 创建子图
ax2.set_extent([0, 360, 15, 72], crs = ccrs.PlateCarree())
ax2.coastlines(linewidth=.5, color='gray')
ax2.set_yticks(y_extent, crs=ccrs.PlateCarree())
lat_formatter = LatitudeFormatter()
ax2.yaxis.set_major_formatter(lat_formatter)
ax2.tick_params(length=0)
p20 = ax2.contourf(lontest, Lat, v2Diff_rGS[:, :], 
                 levels=np.linspace(-10, 10, 21), cmap=cmap1, extend='both', 
                 transform=ccrs.PlateCarree())
p21 = ax2.contour(lontest, Lat, v2_ctrl[9, :, :], [0,4,8,12,16,20],colors=['k'],
                linestyles=['-'], linewidths=[0.5],
                transform=ccrs.PlateCarree())
ax2.text(lontest[350], Lat[240], r"(b)rGS", va="center", fontdict={"weight":"bold"})

ax3 = fig.add_subplot(313,projection=ccrs.PlateCarree(central_longitude=240))# 创建子图
ax3.set_extent([0, 360, 15, 72], crs = ccrs.PlateCarree())
ax3.coastlines(linewidth=.5, color='gray')
ax3.set_xticks(x_extent, crs=ccrs.PlateCarree())
ax3.set_yticks(y_extent, crs=ccrs.PlateCarree())
lon_formatter = LongitudeFormatter(zero_direction_label=False)
lat_formatter = LatitudeFormatter()
ax3.xaxis.set_major_formatter(lon_formatter)
ax3.yaxis.set_major_formatter(lat_formatter)
ax3.tick_params(length=0)
p30 = ax3.contourf(lontest, Lat, v2Diff_rKG[:, :], 
                 levels=np.linspace(-10, 10, 21), cmap=cmap1, extend='both', 
                 transform=ccrs.PlateCarree())
p31 = ax3.contour(lontest, Lat, v2_ctrl[9, :, :], [0,4,8,12,16,20],colors=['k'],
                linestyles=['-'], linewidths=[0.5],
                transform=ccrs.PlateCarree())
ax3.text(lontest[350], Lat[240], r"(c)rKG", va="center", fontdict={"weight":"bold"})

fig.subplots_adjust(hspace=0.1)
fig.subplots_adjust(top=0.9)
cbar_ax = fig.add_axes([0.2, 0.03, 0.6, 0.03])
cb0 = plt.colorbar(p20, cbar_ax, orientation='horizontal')
cb0.ax.tick_params(length=0, labelsize=6)
cb0.set_ticks(np.linspace(-10, 10, 11))
fig.savefig('v2_diff_change.png',dpi=600,bbox_inches='tight',pad_inches=0.05)









