# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 10:31:32 2021

@author: Yefry Lopez
"""
# Import the pandas package
import pandas as pd

feature_names = ['Country Name',
 'Country Code',
 'Indicator Name',
 'Indicator Code',
 '1960']

# Initialize reader object: df_reader
df_reader = pd.read_csv('./databases/WDIData.csv', chunksize=10, usecols =feature_names )

# Print two chunks
print(next(df_reader))
print(next(df_reader))