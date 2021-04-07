# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:58:12 2021
Goal: Determine the average age by population
@author: Yefry Lopez
"""
from sqlalchemy import create_engine, MetaData, Table

# Define an engine to connect to chapter5.sqlite: engine
engine = create_engine('sqlite:///./databases/chapter5.sqlite')

#conecction
connection = engine.connect()

# Initialize MetaData: metadata
metadata = MetaData()

# Reflect census table from the engine: census
census = Table('census', metadata, autoload = True, autoload_with = engine)

# Print table names
print(engine.table_names())

# Import select and func
from sqlalchemy import select, func

# Select sex and average age weighted by 2000 population
stmt = select([(func.sum(census.columns.pop2000 * census.columns.age) 
  					/ func.sum(census.columns.pop2000)).label('average_age'),
               census.columns.sex
			  ])

# Group by sex
stmt = stmt.group_by(census.columns.sex)

# Execute the query and fetch all the results
results = connection.execute(stmt).fetchall()

# Print the sex and average age column for each result
for result in results:
    print(result.sex, result.average_age)