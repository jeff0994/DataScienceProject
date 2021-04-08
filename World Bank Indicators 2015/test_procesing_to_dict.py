# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 10:02:06 2021

@author: Yefry Lopez
"""
from procesing_to_dict import lists2dict


feature_names = ['CountryName',
 'CountryCode',
 'IndicatorName',
 'IndicatorCode',
 'Year',
 'Value']

row_vals = ['Arab World',
 'ARB',
 'Adolescent fertility rate (births per 1,000 women ages 15-19)',
 'SP.ADO.TFRT',
 '1960',
 '133.56090740552298']

# Call lists2dict: rs_fxn
rs_fxn = lists2dict(feature_names,row_vals)

# Print rs_fxn
print(rs_fxn)
