# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 10:15:16 2021

@author: Yefry Lopez
"""

from read_large_file import read_large_file

# Open a connection to the file
with open('./databases/WDIData.csv') as file:

    # Create a generator object for the file: gen_file
    gen_file = read_large_file(file)

    # Print the first three lines of the file
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))