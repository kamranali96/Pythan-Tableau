#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 10:47:06 2022

@author: kamranali
"""
import pandas as pd

data = pd.read_csv('transaction.csv', sep=';')

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberofItemsPurchased*ProfitPerItem
CostPerTransaction = NumberofItemsPurchased*CostPerItem
SellingPricePerItemTransaction = NumberofItemsPurchased * SellingPricePerItem

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerTransaction * NumberofItemsPurchased

data["CostPerTransaction"] = data['CostPerItem'] * data['NumberOfItemsPurchased']

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data["NumberOfItemsPurchased"]

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data["CostPerTransaction"]

data['Markup'] = (data['SalesPerTransaction'] - data["CostPerTransaction"]) / data["CostPerTransaction"]

#rounding markinng

roundmarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'], 2)

#change columns type 
day = data['Day'].astype(str)
year = data['Year'].astype(str)

MyDate = day+'-'+data['Month']+'-'+year
data['Date'] = MyDate

split_col = data['ClientKeywords'].str.split(',', expand = True)
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']','')

data['ItemDescription'] = data['ItemDescription'].str.lower()

#merging values
Sdata = pd.read_csv('value_inc_seasons.csv', sep = ';')

data = pd.merge(data, Sdata, on = 'Month')

data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop(['Year', 'Month'], axis = 1)

#Export Csv

data.to_csv('ValueInc_Cleaned.csv', index=False)