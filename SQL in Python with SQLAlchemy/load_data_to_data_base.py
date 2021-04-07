# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:47:20 2021

@author: Yefry Lopez 
"""
# Import insert
from sqlalchemy import insert
# Import create_engine, MetaData
from sqlalchemy import create_engine, MetaData, Table

from read_data import csv_file

values_list = csv_file('./databases/census.csv')

# Define an engine to connect to chapter5.sqlite: engine
engine = create_engine('sqlite:///./databases/chapter5.sqlite')

#conecction
connection = engine.connect()

# Initialize MetaData: metadata
metadata = MetaData()

# Reflect census table from the engine: census
census = Table('census', metadata, autoload = True, autoload_with = engine)

# Build insert statement: stmt
stmt = insert(census)

# Use values_list to insert data: results
results = connection.execute(stmt, values_list)

# Print rowcount
print(results.rowcount)