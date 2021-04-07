# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 19:10:19 2021
Goal: Determine the percentage of population by gender and state
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

# import case, cast and Float from sqlalchemy
from sqlalchemy import case, cast, Float

# Build a query to calculate the percentage of women in 2000: stmt
stmt = select([census.columns.state,
    (func.sum(
        case([
            (census.columns.sex == 'F', census.columns.pop2000)
        ], else_=0)) /
     cast(func.sum(census.columns.pop2000), Float) * 100).label('percent_female')
])

# Group By state
stmt = stmt.group_by(census.columns.state)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the percentage
for result in results:
    print(result.state, result.percent_female)