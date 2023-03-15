# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 12:52:29 2023

@author: b.tarran
"""

def calculate_results(sensitivity, specificity, sample_size, prevalence_rate):
    true_positives = sensitivity * prevalence_rate * sample_size
    false_positives = (1 - specificity) * (1 - prevalence_rate) * sample_size
    true_negatives = specificity * (1 - prevalence_rate) * sample_size
    false_negatives = (1 - sensitivity) * prevalence_rate * sample_size
    return true_positives, false_positives, true_negatives, false_negatives

def calculate_proportions(true_positives, false_positives, true_negatives, false_negatives, sample_size):
    true_positives_prop_all = (true_positives / sample_size) * 100
    false_positives_prop_all = (false_positives / sample_size) * 100
    true_negatives_prop_all = (true_negatives / sample_size) * 100
    false_negatives_prop_all = (false_negatives / sample_size) * 100
    return true_positives_prop_all, false_positives_prop_all, true_negatives_prop_all, false_negatives_prop_all

def calculate_proportions_pos(true_positives, false_positives):
    true_positives_prop = true_positives / (true_positives + false_positives) * 100
    false_positives_prop = false_positives / (true_positives + false_positives) * 100
    return true_positives_prop, false_positives_prop