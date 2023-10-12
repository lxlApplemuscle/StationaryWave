# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:19:33 2023

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
grid_CESM= io.loadmat(r'D:\python\Stationary wave\CESM\grid')
lat_CESM = np.array(grid_CESM["lat"])[:, 341:-1]
level_CSEM = np.array([  3.643466,   7.59482 ,  14.356632,  24.61222 ,  38.2683  ,  54.59548 ,
        72.012451,  87.82123 , 103.317127, 121.547241, 142.994039, 168.22508 ,
       197.908087, 232.828619, 273.910817, 322.241902, 379.100904, 445.992574,
       524.687175, 609.778695, 691.38943 , 763.404481, 820.858369, 859.534767,
       887.020249, 912.644547, 936.198398, 957.48548 , 976.325407, 992.556095])
##
v2Data_ctrl = io.loadmat(path+"\\v2_ctrl")
v2Data_rKE  = io.loadmat(path+"\\Ctrl_rKE\\v2_rKE")
v2Data_rGS  = io.loadmat(path+"\\rGS\\v2_rGS")
v2Data_rKG  = io.loadmat(path+"\\rKG\\v2_rKG")
v2Data_CESM = io.loadmat(r'D:\python\Stationary wave\CESM\v2_300_R_test')

v2_ctrl = np.mean(np.array(v2Data_ctrl["v2"]), 2)
v2_rKE  = np.mean(np.array(v2Data_rKE["v2"]), 2)
v2_rGS  = np.mean(np.array(v2Data_rGS["v2"]), 2)
v2_rKG  = np.mean(np.array(v2Data_rKG["v2"]), 2)
v2_CESM = np.mean(np.array(v2Data_CESM["v2_300_R_test"]), 2)

v2Diff_rKE = v2_rKE-v2_ctrl
v2Diff_rGS = v2_rGS-v2_ctrl
v2Diff_rKG = v2_rKG-v2_ctrl

##
fig = plt.figure(dpi = 600, figsize=(6,6))
cmap1 = cmaps.BlueWhiteOrangeRed

ax1 = fig.add_subplot(221)# 创建子图
p11 = ax1.contour(lat_CESM[0, :], -level_CSEM, v2_CESM[:,341:-1], [-2,0,2,4,6,8,10,12,14,16,18],colors=['k'],
                linestyles=['-'], linewidths=[0.5])
plt.clabel(p11, inline=True, fontsize=4)
plt.xticks([0, 20, 40, 60],['EQ',r'$20^\circ$N',r'$40^\circ$N',r'$60^\circ$N'],fontdict={"size":8})
plt.yticks([-200,-400,-600,-800,-1000],[r'$200$',r'$400$',r'$600$',r'$800$',r'$1000$'], fontdict={"size":8})
plt.ylabel('Pressure(hPa)')
ax1.text(lat_CESM[0, 10], -level_CSEM[10], "CESM", va="center", fontdict={"weight":"bold"})

ax2 = fig.add_subplot(222)# 创建子图
p20 = ax2.contourf(Lat, -Level[0, :], v2Diff_rKE[:, :], 
                 levels=np.linspace(-1.5, 1.5, 21), cmap=cmap1, extend='both')
p21 = ax2.contour(Lat, -Level[0, :], v2_ctrl[:,:], [-2,0,2,4,6,8,10,12],colors=['k'],
                linestyles=['-'], linewidths=[0.5])
plt.xticks([])
plt.yticks([-20000,-40000,-60000,-80000,-100000],[r'$200$',r'$400$',r'$600$',r'$800$',r'$1000$'], fontdict={"size":8})
ax2.text(Lat[10], -Level[0, 10], "rKE", va="center", fontdict={"weight":"bold"})

ax3 = fig.add_subplot(223)# 创建子图
p30 = ax3.contourf(Lat, -Level[0, :], v2Diff_rGS[:, :], 
                 levels=np.linspace(-1.5, 1.5, 21), cmap=cmap1, extend='both')
p31 = ax3.contour(Lat, -Level[0, :], v2_ctrl[:,:], [-2,0,2,4,6,8,10,12],colors=['k'],
                linestyles=['-'], linewidths=[0.5])
plt.xticks([20, 40, 60],[r'$20^\circ$N',r'$40^\circ$N',r'$60^\circ$N'])
plt.yticks([-20000,-40000,-60000,-80000,-100000],[r'$200$',r'$400$',r'$600$',r'$800$',r'$1000$'],fontdict={"size":8})
ax3.text(Lat[10], -Level[0, 10], "rGS", va="center", fontdict={"weight":"bold"})
plt.ylabel('Pressure(hPa)')

ax4 = fig.add_subplot(224)# 创建子图
p40 = ax4.contourf(Lat, -Level[0, :], v2Diff_rKG[:, :], 
                 levels=np.linspace(-1.5, 1.5, 21), cmap=cmap1, extend='both')
p41 = ax4.contour(Lat, -Level[0, :], v2_ctrl[:,:], [-2,0,2,4,6,8,10,12],colors=['k'],
                linestyles=['-'], linewidths=[0.5])
plt.xticks([20, 40, 60],[r'$20^\circ$N',r'$40^\circ$N',r'$60^\circ$N'])
plt.yticks([])
ax4.text(Lat[10], -Level[0, 10], "rKG", va="center", fontdict={"weight":"bold"})
fig.subplots_adjust(wspace=.2, hspace=.12)

fig.subplots_adjust(right=0.9)
cbar_ax = fig.add_axes([0.92, 0.2, 0.02, 0.6])
cb0 = plt.colorbar(p20, cbar_ax)
cb0.ax.tick_params(length=0, labelsize=6)
cb0.set_ticks(np.linspace(-1.5, 1.5, 11))
#fig.savefig('v2_zonal.png',dpi=600,bbox_inches='tight',pad_inches=0.05)



