# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:17:05 2021

@author: Yefry López
"""
# Import create_engine, MetaData
from sqlalchemy import create_engine, MetaData

# Define an engine to connect to chapter5.sqlite: engine
engine = create_engine('sqlite:///./databaseschapter5.sqlite')

# Initialize MetaData: metadata
metadata = MetaData()