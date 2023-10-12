# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 09:23:22 2023

@author: lixianlong
"""

import numpy as np
import cmaps
import matplotlib.pyplot as plt
import scipy.io as io

path = r'D:\python\Stationary wave\channel'
gridData = io.loadmat(path+"\grid.mat")
Lon = np.array(gridData["Lon"])[0, :]
Lat = np.array(gridData["Lat"])[0, :]
Level = np.array(gridData["Levels"])

uData_ctrl = io.loadmat(path+"\\u_ctrl")
uData_rKE  = io.loadmat(path+"\\Ctrl_rKE\\u_rKE")
uData_rGS  = io.loadmat(path+"\\rGS\\u_rGS")
uData_rKG  = io.loadmat(path+"\\rKG\\u_rKG")
uData_ERA5 = io.loadmat(path+"\\u_era5")

u_ctrl = np.array(uData_ctrl["u"])
u_rKE  = np.array(uData_rKE["u"])
u_rGS  = np.array(uData_rGS["u"])
u_rKG  = np.array(uData_rKG["u"])
u_era5 = np.array(uData_ERA5["u"])
level_era5 = np.array(uData_ERA5["level_era5"])

uDiff_rKE = u_rKE-u_ctrl
uDiff_rGS = u_rGS-u_ctrl
uDiff_rKG = u_rKG-u_ctrl

fig = plt.figure(dpi = 600, figsize=(6,6))
cmap1 = cmaps.BlueWhiteOrangeRed

lat = np.linspace(90, -90, 721)

#extend = (0, 1, 0, 1)
ax1 = fig.add_subplot(221)# 创建子图
p11 = ax1.contour(lat[0:401], -level_era5[0, :], u_era5[:, 0:401], [-5,0,5,10,15,20,25,30],colors=['k'],
                linestyles=['-'], linewidths=[0.5])
plt.clabel(p11, inline=True, fontsize=4)
plt.xticks([0, 20, 40, 60],['EQ',r'$20^\circ$N',r'$40^\circ$N',r'$60^\circ$N'],fontdict={"size":8})
plt.yticks([-200,-400,-600,-800,-1000],[r'$200$',r'$400$',r'$600$',r'$800$',r'$1000$'], fontdict={"size":8})
plt.ylabel('Pressure(hPa)')
ax1.text(lat[380], -level_era5[0, 11], "ERA5", va="center", fontdict={"weight":"bold"})

ax2 = fig.add_subplot(222)# 创建子图
p20 = ax2.contourf(Lat, -Level[0, :], uDiff_rKE[:, :], 
                 levels=np.linspace(-0.5, 0.5, 21), cmap=cmap1, extend='both')
p21 = ax2.contour(Lat, -Level[0, :], u_ctrl[:,:], [-5,0,5,10,15,20,25,30],colors=['k'],
                linestyles=['-'], linewidths=[0.5])
plt.xticks([])
plt.yticks([-20000,-40000,-60000,-80000,-100000],[r'$200$',r'$400$',r'$600$',r'$800$',r'$1000$'], fontdict={"size":8})
ax2.text(Lat[10], -Level[0, 10], "rKE", va="center", fontdict={"weight":"bold"})

ax3 = fig.add_subplot(223)# 创建子图
p30 = ax3.contourf(Lat, -Level[0, :], uDiff_rGS[:, :], 
                 levels=np.linspace(-0.5, 0.5, 21), cmap=cmap1, extend='both')
p31 = ax3.contour(Lat, -Level[0, :], u_ctrl[:,:], [-5,0,5,10,15,20,25,30],colors=['k'],
                linestyles=['-'], linewidths=[0.5])
plt.xticks([20, 40, 60],[r'$20^\circ$N',r'$40^\circ$N',r'$60^\circ$N'])
plt.yticks([-20000,-40000,-60000,-80000,-100000],[r'$200$',r'$400$',r'$600$',r'$800$',r'$1000$'], fontdict={"size":8})
ax3.text(Lat[10], -Level[0, 10], "rGS", va="center", fontdict={"weight":"bold"})
plt.ylabel('Pressure(hPa)')

ax4 = fig.add_subplot(224)# 创建子图
p40 = ax4.contourf(Lat, -Level[0, :], uDiff_rKG[:, :], 
                 levels=np.linspace(-0.5, 0.5, 21), cmap=cmap1, extend='both')
p41 = ax4.contour(Lat, -Level[0, :], u_ctrl[:,:], [-5,0,5,10,15,20,25,30],colors=['k'],
                linestyles=['-'], linewidths=[0.5])
plt.xticks([20, 40, 60],[r'$20^\circ$N',r'$40^\circ$N',r'$60^\circ$N'])
plt.yticks([])
ax4.text(Lat[10], -Level[0, 10], "rKG", va="center", fontdict={"weight":"bold"})
fig.subplots_adjust(wspace=.2, hspace=.12)

fig.subplots_adjust(right=0.9)
cbar_ax = fig.add_axes([0.92, 0.2, 0.02, 0.6])
cb0 = plt.colorbar(p20, cbar_ax)
cb0.ax.tick_params(length=0, labelsize=6)
cb0.set_ticks(np.linspace(-0.5, 0.5, 11))
#fig.savefig('u_zonal.png',dpi=600,bbox_inches='tight',pad_inches=0.05)







