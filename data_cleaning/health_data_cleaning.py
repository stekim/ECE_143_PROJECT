# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 20:12:09 2021

@author: s
"""
from data_cleaning.health_data_cleaning import *

# Viz for health data
file_name = 'datasets/health.csv'
color = 'royalblue'
# data cleaning using helper function
new_df = heath_data_clean(file_name)