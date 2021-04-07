# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 19:29:43 2021
Goal Determine the difference by state from the 2000 and 2008 censuses
@author: Yefry Lopez
"""
from sqlalchemy import create_engine, MetaData, Table, select, desc

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

# Build query to return state name and population difference from 2008 to 2000
stmt = select([census.columns.state,
     (census.columns.pop2008 -census.columns.pop2000).label('pop_change')
])

# Group by State
stmt = stmt.group_by(census.columns.state)

# Order by Population Change
stmt = stmt.order_by(desc('pop_change'))

# Limit to top 10
stmt = stmt.limit(10)

# Use connection to execute the statement and fetch all results
results = connection.execute(stmt).fetchall()

# Print the state and population change for each record
for result in results:
    print('{}:{}'.format(result.state, result.pop_change))