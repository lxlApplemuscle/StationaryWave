# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 09:27:11 2023

@author: lixianlong
"""

import numpy as np
import cmaps
import matplotlib.pyplot as plt
import scipy.io as io
from smooth2D import smooth2D

path = r'D:\python\Stationary wave\channel'
gridData = io.loadmat(path+"\grid.mat")
Lon = np.array(gridData["Lon"])[0, :]
Lat = np.array(gridData["Lat"])[0, :]
Level = np.array(gridData["Levels"])

uData = io.loadmat(path+"\\u_ctrl")
uall  = np.array(uData["u"])
uData_rKE = io.loadmat(path+"\\u_rKE")
u_rKE = np.array(uData_rKE["u"])
u_diff = u_rKE-uall

fig = plt.figure(dpi = 600, figsize=(6,6))
ax = plt.gca()
cmap1 = cmaps.BlueWhiteOrangeRed

p0 = ax.contourf(Lat, -Level[0, :], u_diff[:, :], 
                 levels=np.linspace(-0.5, 0.5, 21), cmap=cmap1, extend='both')
p1 = ax.contour(Lat, -Level[0, :], uall[:,:], [-5,0,5,10,15,20,25,30],colors=['k'],
                linestyles=['-'], linewidths=[0.5])
plt.xticks([20, 40, 60],[r'$20^\circ$N',r'$40^\circ$N',r'$60^\circ$N'])
plt.yticks([-20000,-40000,-60000,-80000,-100000],[r'$200$',r'$400$',r'$600$',r'$800$',r'$1000$'])
plt.ylabel('Pressure(hPa)')
ax.tick_params(length=0)
cb0 = fig.colorbar(p0, ax=ax, orientation='vertical', pad = .1,
                   fraction=0.05)
cb0.ax.tick_params(length=0, labelsize=6)
cb0.set_ticks(np.linspace(-0.5, 0.5, 11))
plt.show()

#fig.savefig('u_ctrl_rKE.png',dpi=600,bbox_inches='tight',pad_inches=0.05)