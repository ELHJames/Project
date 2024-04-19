#!/usr/bin/env python
# coding: utf-8

# In[7]:


import matplotlib.pyplot as plt
import numpy as np


# In[8]:


def plot_clusters(x, y, y_err):
    plt.figure(figsize=(10, 6))
    
    plt.errorbar(x, y, yerr=y_err, fmt='+', markersize=7, color='black', ecolor='black', capsize=5, label='Data')

    #Horizontal dotted line to differentiate high scores.
    plt.axhline(y=87, xmin=0, xmax=1, color='black', linestyle='--')

    plt.xlabel('Topic Number', size=20)
    plt.ylabel('Score / %', size=20)
    plt.grid(True)
    plt.xlim(0, 50)
    plt.ylim(-5,100)
    plt.xticks(size=15)
    plt.yticks(size=15)
    plt.show()

#The values in ascneding order for topic final scores.
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
     21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,
     38,39,40,41,42,43,44,45,46,47,48,49]

y = [4.84, 11.65, 23.17, 25.24, 34.38, 34.65, 
     42.94, 53.08, 54.85, 56.49, 63.9, 65.11, 65.64, 
     66.47, 66.87, 67.82, 67.93, 69.59, 70.12, 71.05, 
     71.09, 71.69, 72.41, 73.05, 73.12, 73.19, 73.55, 
     73.97, 75.05, 75.49, 77.31, 80.42, 81.03, 81.32, 
     81.47, 82.04, 82.14, 83.5, 85.15, 88.15, 89.02, 
     89.77, 91.21, 92.44, 92.7, 92.72, 92.83, 92.97, 94.58]

#Uncertainties in final score provided by sensitivity analysis.
y_err = [7.26, 6.71, 8.59, 8.44, 4.93, 4.55, 3.36, 7.69, 
         7.94, 3.15, 3.37, 8.58, 8.70, 2.71, 8.76, 5.48, 
         8.03, 8.61, 5.51, 4.91, 8.74, 6.66, 8.96, 9.03, 
         9.09, 3.28, 3.53, 8.64, 2.50, 1.61, 9.28, 2.59, 
         3.91, 3.90, 2.86, 1.72, 1.25, 2.42, 2.14, 0.84, 
         1.61, 1.65, 1.24, 1.31, 1.26, 1.82, 1.21, 1.63, 1.37]

plot_clusters(x, y, y_err)

