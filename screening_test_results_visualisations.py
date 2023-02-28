# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 12:59:41 2023

@author: b.tarran
"""
from screening_test_results_calculations import *
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# Edit these values as needed
sensitivity = 0.26
specificity = 0.91
sample_size = 1000
prevalence_rate = 0.76

# Calculate TP, FP, TN and FN counts
(true_positives, false_positives, true_negatives, false_negatives) = calculate_results(
    sensitivity, specificity, sample_size, prevalence_rate)

# Put into dataframe
df = pd.DataFrame([[true_positives, false_positives, true_negatives, false_negatives]], columns = (
    'True positives', 'False positives', 'True negatives', 'False negatives'), index = {'Results'})
print(df)

# Calculate proportions, put into dataframe
(true_positives_prop_all, false_positives_prop_all, true_negatives_prop_all,
 false_negatives_prop_all) = calculate_proportions(
    true_positives, false_positives, true_negatives, false_negatives, sample_size)
df2 = pd.DataFrame([[true_positives_prop_all, false_positives_prop_all, 
                     true_negatives_prop_all, false_negatives_prop_all]], columns = (
                         'True positives', 'False positives', 'True negatives',
                         'False negatives'), index = {'Proportion of all tests'})
print(df2)

# Override style defaults
my_dpi = 72
plt.rcParams['figure.figsize'] = ((800/my_dpi), (400/my_dpi))
plt.rcParams['legend.fontsize'] = 20
matplotlib.rc('xtick', labelsize=20) 
matplotlib.rc('ytick', labelsize=20)
matplotlib.rc('axes', titlesize=20)
matplotlib.style.use('ggplot')

# Plot Fig1
df2.plot.barh(stacked = True).legend(loc = 'upper center', ncol = 2)
plt.yticks([])
plt.xlim(0, 100)
plt.xlabel('Test results as % of all tests', fontsize = 20)
# plt.savefig('filename.png', dpi = my_dpi, bbox_inches = 'tight')
plt.show()

# Calculate proportion of TP and FP as % of all postive tests, put into dataframe
(true_positives_prop, false_positives_prop) = calculate_proportions_pos(true_positives,
                                                                        false_positives)
df3 = pd.DataFrame([[true_positives_prop, false_positives_prop]], columns = (
    'True positives', 'False positives'), index = {'Proportion of positive tests'})
print(df3)

# Plot Fig2
df3.plot.barh(stacked = True).legend(loc = 'upper center', ncol = 2)
plt.yticks([])
plt.xlim(0, 100)
plt.xlabel('Test results as % of all positive tests', fontsize = 20)
# plt.savefig('filename.png', dpi = my_dpi, bbox_inches = 'tight')
plt.show()