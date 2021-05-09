#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 19:02:41 2021

@author: abby
"""

import pandas as pd

state_reqs1 = pd.read_csv("P1.csv")
state_reqs2 = pd.read_csv("P2.csv")
state_reqs3 = pd.read_csv("P3.csv")

#Merging data into one dataframe.
all_state_reqs = state_reqs1.merge(state_reqs2, how="inner", on = "Unnamed: 0")
all_state_reqs = all_state_reqs.merge(state_reqs3, how="inner")

#Replacing with 1 = Yes and 0 = No. 
all_state_reqs = all_state_reqs.replace({"x":1, None:0})

#Dropping columns we are not interested in.
hs_data = all_state_reqs.drop([0,1,3,4,13,14,15])

#Transposing rows/columns. 
hs_data = hs_data.transpose()

#Renaming columns. 
hs_data.columns = ['HS_required', 'HS_minutes', 'funding',
                'no_exemptions', 'no_subs', 'WH_punish', 'PE_punish', 'standards', 'test']
hs_data = hs_data.drop(index= "Unnamed: 0")
hs_data = hs_data.drop(index= "Total")
print(len(hs_data))

#Adding scores.
hs_data["score"] = hs_data.sum(axis=1)

hs_data.to_csv("hs_reqs.csv")


