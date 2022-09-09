#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 11:39:57 2022

@author: kamranali
"""

import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt

#method one to read json data.
json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2 to read json data.
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)

#transfrom to dataframe:

loan_data = pd.DataFrame(data)

#using exponent function.
income = np.exp(loan_data['log.annual.inc'])
loan_data['Annnualincome'] = income

fico = 300

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 601 and fico < 660:
    ficocat = 'Fair' 
elif fico >= 660 and fico < 700:
    ficocat = 'Good'
elif fico >= 700:
    ficocat ='Excellent'
else:
    ficocat = 'Unknown'
print(ficocat)

length = len(loan_data)

ficocat = []
for x in range(0, length):
    category = loan_data['fico'][x]
    if category >= 300 and category < 400:
        cat = 'Very Poor'
    elif category >= 400 and category < 600:
        cat = 'Poor'
    elif category >= 601 and category < 660:
        cat = 'Fair' 
    elif category >= 660 and category < 700:
        cat = 'Good'
    elif category >= 700:
        cat ='Excellent' 
    else:
        cat = 'Unknown'
    ficocat.append(cat)
    
ficocat = pd.Series(ficocat)

loan_data['Fico_Category'] = ficocat

loan_data.loc[loan_data['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loan_data.loc[loan_data['int.rate'] <=  0.12, 'int.rate.type'] = 'Low'

catplot = loan_data.groupby(['Fico_Category']).size()
purposecount = loan_data.groupby(['purpose']).size()

catplot.plot.bar(color = 'green', width = 0.1)

#saving
loan_data.to_csv('loan_cleaned.csv', index = True)