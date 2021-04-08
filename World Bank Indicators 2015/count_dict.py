# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 10:20:01 2021

@author: Yefry Lopez
"""

from read_large_file import read_large_file
from procesing_to_dict import lists2dict


# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Open a connection to the file
with open('./databases/WDIData.csv') as file:

    # Iterate over the generator from read_large_file()
    for line in read_large_file(file):

        row = line.split(',')
        first_col = row[0]

        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1

# Print            
print(counts_dict)