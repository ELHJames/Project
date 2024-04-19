#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# The following displays the changing of the weights, done to check the code is working correctly.

# In[11]:


#Input the scores and initial weightings
spreadsheet_scores = {'WoS': 29.49, 'A-News': 23.93, 'A-Social': -4.98, 
                      'Finance': 9.11, 'Employees': 7.31, 'Benefits': 2.00}
initial_weightings = {'WoS': 0.30, 'A-News': 0.25, 'A-Social': 0.05, 'Finance': 0.15, 'Employees': 0.15, 'Benefits': 0.10}

#Finds unweighted values
unweighted_values = {key: spreadsheet_scores[key] / initial_weightings[key] for key in spreadsheet_scores}

#Input range of percentage changes and interval
percentage_changes = np.arange(-5, 5.01, 0.01) / 100  

#Sensitivity analysis begins
for key in spreadsheet_scores:
    for change in percentage_changes:
        #Current score weighting changed
        new_weightings = initial_weightings.copy()
        new_weightings[key] += change
        
        #Other scores need to be adjusted so the proportions remain the same
        for other_key in new_weightings:
            if other_key != key:
                new_weightings[other_key] *= (1 - new_weightings[key]) / (1 - initial_weightings[key])
        
        #Checks that total new weighting equals 1
        total_weighting = sum(new_weightings.values())
        
        #New values printed
        print(f'Weightings after changing {key} by {change * 100:.2f}%:', end=' ')
        for k, v in new_weightings.items():
            print(f'{k}: {v:.2f}', end=', ')
        print()  
        
        #New total score calculated
        new_sum = sum(unweighted_values[k] * new_weightings[k] for k in unweighted_values)
        
        #Results printed
        print(f'Sum of weightings after changing {key} by {change * 100:.2f}%: {total_weighting:.2f}')
        print(f'Sum of scores after changing {key} by {change * 100:.2f}%: {new_sum:.2f}')


# The following produces a graph of percentage changes and effect to score.

# In[11]:


import numpy as np
import matplotlib.pyplot as plt

#Input the weighted scores and initial weightings
spreadsheet_scores = {        'WoS': 29.98
                      ,    'A-News': 24.89
                      ,   'A-Social': 5.00
                      ,   'Finance': 10.53
                      , 'Employees': 11.81
                      ,   'Benefits': 9.00
                     }

initial_weightings = {'WoS': 0.30, 'A-News': 0.25, 'A-Social': 0.05, 'Finance': 0.15, 'Employees': 0.15, 'Benefits': 0.10}

#Finds unweighted values
unweighted_values = {key: spreadsheet_scores[key] / initial_weightings[key] for key in spreadsheet_scores}

#Input range of percentage changes and interval
percentage_changes = np.arange(-5, 5.01, 0.01) / 100  

#Float for max and min sums
max_sum = float('-inf')
min_sum = float('inf')

#Lists to store data for plot
x_vals = []
y_vals = []

#Sensitivty analysis begins
for key in spreadsheet_scores:
    key_x_vals = []
    key_y_vals = []
    for change in percentage_changes:
        #Current score weighting changed
        new_weightings = initial_weightings.copy()
        new_weightings[key] += change
        
        #Other scores need to be adjusted so the proportions remain the same 
        for other_key in new_weightings:
            if other_key != key:
                new_weightings[other_key] *= (1 - new_weightings[key]) / (1 - initial_weightings[key])
        
        #Checks that total new weighting equals 1
        total_weighting = sum(new_weightings.values())
        
        #New total score calculated
        new_sum = sum(unweighted_values[k] * new_weightings[k] for k in unweighted_values)
        
        #New max and min values
        max_sum = max(max_sum, new_sum)
        min_sum = min(min_sum, new_sum)
        
        #Data stored for plot
        key_x_vals.append(change * 100)  
        key_y_vals.append(new_sum)  
    
    
    x_vals.append(key_x_vals)
    y_vals.append(key_y_vals)

#Plot
plt.figure(figsize=(10, 6))
for key, x, y in zip(spreadsheet_scores.keys(), x_vals, y_vals):
    plt.plot(x, y, label=key)

#Graph characteristics
plt.xlabel('Change in weightings / %', size=22)
plt.ylabel('Final score / %', size=22)
plt.xticks(np.arange(-5, 6, 1), size=17)
plt.yticks(size=17)
plt.xlim(-5, 5)
plt.ylim(89.75,92.75)
plt.grid(True)

plt.legend(loc='upper center', fontsize=14)

#Print min and max score after sensitivty analysis
print(f"Maximum sum of scores: {max_sum:.2f}")
print(f"Minimum sum of scores: {min_sum:.2f}")

#Finds range
initial_sum = sum(spreadsheet_scores.values())
diff_to_max = max_sum - initial_sum
diff_to_min = initial_sum - min_sum

#Finds uncertainty = range/2
average_uncertainty = (diff_to_max + diff_to_min) / 2

#Prints uncertainty
print(f"Uncertainty: {average_uncertainty:.2f}")

plt.show()


# In[ ]:




