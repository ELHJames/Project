#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.gridspec import GridSpec


# In[2]:


def get_hsvcmap(i, N, rot=0.):
    nsc = 24
    chsv = mcolors.rgb_to_hsv(plt.cm.hsv(((np.arange(N)/N)+rot) % 1.)[i,:3])
    rhsv = mcolors.rgb_to_hsv(plt.cm.Reds(np.linspace(.2,1,nsc))[:,:3])
    arhsv = np.tile(chsv,nsc).reshape(nsc,3)
    arhsv[:,1:] = rhsv[:,1:]
    rgb = mcolors.hsv_to_rgb(arhsv)
    return mcolors.LinearSegmentedColormap.from_list("",rgb)


def columnwise_heatmap(array, ax=None, **kw):
    ax = ax or plt.gca()
    premask = np.tile(np.arange(array.shape[1]), array.shape[0]).reshape(array.shape)
    images = []
    for i in range(array.shape[1]):
        col = np.ma.array(array, mask = premask != i)
        im = ax.imshow(col, cmap=get_hsvcmap(i, array.shape[1], rot=0.5), **kw)
        images.append(im)
        
        
        for j in range(array.shape[0]):
            ax.text(i, j, f'{array[j,i]}', ha='center', va='center', 
                    color='ghostwhite', fontsize=25)  
            
    return images


data = [
    [5, 0, 0, 0, 0, 0, 1],  
    [0, 4, 0, 3, 0, 3, 1],  
    [7, 3, 7, 4, 5, 9, 9],  
    [6, 1, 0, 2, 6, 3, 6],  
    [4, 2, 2, 4, 5, 6, 6]   
]

fig, ax = plt.subplots(figsize=(10, 6))

ims = columnwise_heatmap(np.array(data), ax=ax, aspect="auto")

ax.set(xticks=np.arange(len(data[0])), yticks=np.arange(len(data)),
       xticklabels=['Astro', 'P&F', 'CM',
                  'Quantum', 'Med', 'AMO', 'Other'],
       yticklabels=['PhD - Astro', 'PhD - Photonics', 'ChatGPT', 'Gemini', 'Claude'])

ax.tick_params(axis='x', labelsize=20)  # Increase x-axis label size
ax.tick_params(axis='y', labelsize=20)  # Increase y-axis label size

ax.set_xlabel('Physics Fields', fontsize=22)
ax.set_ylabel('Sources', fontsize=22)

plt.show()

