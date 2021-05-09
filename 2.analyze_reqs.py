#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 13:38:05 2021

@author: abby
"""

import pandas as pd

#Calling the data.
analyze = pd.read_csv("hs_reqs.csv")
rename = {"Unnamed: 0": "State"}
analyze.rename(columns=rename, inplace=True)

#Finding the most common policies. 
pols = []
for col in analyze.columns:
    count = analyze[col].value_counts()
    count.name = col
    pols.append(count)
policies = pd.concat(pols, axis=1)
policies = policies.drop(['State', 'score'], axis = 1)
bad = policies['HS_required'].isna()
policies = policies[bad == False]
print(policies)

grouped = analyze.groupby(["HS_required","standards"])

print( analyze.groupby(["no_subs", "test"]).size())
print( analyze.groupby(["funding", "test"]).size())
print( analyze.groupby(["HS_required", "HS_minutes"]).size())
print( analyze.groupby(["WH_punish", "PE_punish"]).size())

