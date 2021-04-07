# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:35:37 2021

@author: Yefry Lopez
"""
# Create an empty list: values_list
import csv

def csv_file(url):
    
    with open(url) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        values_list = []

        # Iterate over the rows
        for row in csv_reader:
            # Create a dictionary with the values
            data = {'state': row[0], 'sex': row[1], 'age':row[2], 'pop2000': row[3],
                    'pop2008': row[4]}
            # Append the dictionary to the values list
            values_list.append(data)
            
    return values_list
    
data = csv_file('./databases/census.csv')