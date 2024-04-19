#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


# In[4]:


#Data read from csv file.
df = pd.read_csv('JWST_Python_File.csv')

#Relevant collumns extracted.
years = df['Year']
wos_hits = df['WoS']
alt_news_hits = df['Alt - News']
alt_social_hits = df['Alt-Social']

fig, ax = plt.subplots(figsize=(10, 6))

#Linear regression model with trendlines.
def plot_trendline(x, y, color, label):
    model = LinearRegression().fit(x.values.reshape(-1, 1), y)
    trendline = model.predict(x.values.reshape(-1, 1))
    angle = np.arctan(model.coef_[0]) * (180 / np.pi)  # Calculate angle in degrees
    plt.plot(x, trendline, color=color, linestyle='--', label=f'{label}: {round(angle, 2)}\N{DEGREE SIGN}')
    return angle

#Angle to x-axis.
angle_wos = plot_trendline(years, wos_hits, 'green', 'Web of Science')
angle_alt_social = plot_trendline(years, alt_social_hits, 'red', 'Alt Social')
angle_alt_news = plot_trendline(years, alt_news_hits, 'blue', 'Alt News')


#Points added for clarity.
ax.scatter(years, wos_hits, color='green', marker='+', s=100, zorder=5)
ax.scatter(years, alt_news_hits, color='blue', marker='+', s=100, zorder=5)
ax.scatter(years, alt_social_hits, color='red', marker='+', s=100, zorder=5)

ax.set_xlim(2008, 2017)
ax.set_ylim(bottom=0)
ax.set_xlabel('Year', fontsize='20')
ax.set_ylabel('Number of Hits', fontsize='20')
plt.legend(fontsize='17')

#Ratio of angles
ratio_wos = (angle_wos) / 90 * 100
ratio_alt_news = (angle_alt_news) / 90 * 100
ratio_alt_social = (angle_alt_social) / 90 * 100

ax.grid(False)
ax.tick_params(axis='both', which='both', direction='inout', length=6, labelsize='15')
plt.show()

#Angles and ratios outputted.

print("Angle for WoS trendline:", round(angle_wos, 2))
print("Angle for Alt News trendline:", round(angle_alt_news, 2))
print("Angle for Alt Social trendline:", round(angle_alt_social, 2))
print("Ratio of angles to 90 degrees (WoS):", round(ratio_wos, 2))
print("Ratio of angles to 90 degrees (Alt News):", round(ratio_alt_news, 2))
print("Ratio of angles to 90 degrees (Alt Social):", round(ratio_alt_social, 2))

