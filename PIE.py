#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


x = [453, 360, 216, 191, 124, 107, 218]
labels = ['Astrophysics', 'Particle & Field Physics',
          'Condensed Matter', 'Quantum Physics',
          'Med & Bio Physics',
          'AMO Physics',
          'Other']
fig, ax = plt.subplots(figsize=(10, 10))

colors = ['tab:cyan', 'tab:blue', 'tab:purple',
          'tab:pink', 'tab:brown', 'tab:olive', 'tab:green']

ax.pie(x, labels=labels, autopct='%.1f%%', colors=colors,
       wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
       textprops={'fontsize': 21})
plt.tight_layout()


# In[ ]:




