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
all_state_reqs = state_reqs1.merge(state_reqs2, how="inner")
all_state_reqs = all_state_reqs.merge(state_reqs3, how="inner")

#Replacing with 1 = Yes and 0 = No. 
all_state_reqs = all_state_reqs.replace({"x":1, None:0})
all_state_reqs = all_state_reqs.drop([0,3,13,14,15])

#Transposing rows/columns. 
all_state_reqs = all_state_reqs.transpose()

#Renaming columns. 
all_state_reqs.columns = ['MS_required', 'HS_required', 'MS_minutes', 'HS_minutes', 'funding',
                'no_exemptions', 'no_subs', 'WH_punish', 'PE_punish', 'standards', 'test']
all_state_reqs = all_state_reqs.drop(index= "Unnamed: 0")
all_state_reqs = all_state_reqs.drop(index= "Total")
print(len(all_state_reqs))

HS_only = all_state_reqs.drop(columns = ['MS_required', 'MS_minutes'])
MS_only = all_state_reqs.drop(columns = ['HS_required', 'HS_minutes'])

#Adding scores.
HS_only["score"] = HS_only.sum(axis=1)
MS_only["score"] = MS_only.sum(axis=1)

all_state_reqs.to_csv("State_Reqs.csv")
HS_only.to_csv("HS_Reqs.csv")
MS_only.to_csv("MS_Reqs.csv")
