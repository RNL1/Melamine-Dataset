# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 12:03:52 2018

@author: r.nik
"""

import pickle
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Read Data
pkl_file = open('Melamine_Dataset.pkl', 'rb')
data = pickle.load(pkl_file)
pkl_file.close()

# Get colormap
col = cm.get_cmap('viridis',4)
col = col.colors

f, axes = plt.subplots(2, 4, sharey='row')


c = tuple(col[0])
axes[0,0].plot(data['wn1'],data['R562']['X1'].T,Color=c)
axes[0,0].set_title('R562')
axes[0,0].xlim = (5400,6400)
axes[0,0].xaxis.set_major_locator(plt.FixedLocator([5600,5900,6200]))
axes[0,0].ylim = (0.5,2.5)
axes[0,0].grid()


axes[1,0].plot(data['wn2'],data['R562']['X2'].T, Color=c)
axes[1,0].set_xlim([6550,7050])
axes[1,0].xaxis.set_major_locator(plt.FixedLocator([6600,6800,7000]))
axes[1,0].ylim = (0.2,0.7)
axes[1,0].grid()


c = tuple(col[1])
axes[0,1].plot(data['wn1'],data['R568']['X1'].T,Color=c)
axes[0,1].set_title('R568')
axes[0,1].xlim = (5400,6400)
axes[0,1].xaxis.set_major_locator(plt.FixedLocator([5600,5900,6200]))
axes[0,1].ylim = (0.5,2.5)
axes[0,1].grid()


axes[1,1].plot(data['wn2'],data['R568']['X2'].T,Color=c)
axes[1,1].set_xlim([6550,7050])
axes[1,1].xaxis.set_major_locator(plt.FixedLocator([6600,6800,7000]))
axes[1,1].ylim = (0.2,0.7)
axes[1,1].grid()


c = tuple(col[2])
axes[0,2].plot(data['wn1'],data['R861']['X1'].T,Color=c)
axes[0,2].set_title('R861')
axes[0,2].xlim = (5400,6400)
axes[0,2].xaxis.set_major_locator(plt.FixedLocator([5600,5900,6200]))
axes[0,2].ylim = (0.5,2.5)
axes[0,2].grid()

axes[1,2].plot(data['wn2'],data['R861']['X2'].T,Color=c)
axes[1,2].set_xlim([6550,7050])
axes[1,2].xaxis.set_major_locator(plt.FixedLocator([6600,6800,7000]))
axes[1,2].ylim = (0.2,0.7)
axes[1,2].grid()

c = tuple(col[3])
axes[0,3].plot(data['wn1'],data['R862']['X1'].T,Color=c)
axes[0,3].set_title('R862')
axes[0,3].xlim = (5400,6400)
axes[0,3].xaxis.set_major_locator(plt.FixedLocator([5600,5900,6200]))
axes[0,3].ylim = (0.5,2.5)
axes[0,3].grid()

axes[1,3].plot(data['wn2'],data['R862']['X2'].T,Color=c)
axes[1,3].set_xlim([6550,7050])
axes[1,3].xaxis.set_major_locator(plt.FixedLocator([6600,6800,7000]))
axes[1,3].ylim = (0.2,0.7)
axes[1,3].grid()


# Some Customizations



f.add_subplot(111, frameon=False)
plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
plt.xlabel('Wavenumber (1/cm)')
plt.ylabel('Absorbance (a.u.)')

