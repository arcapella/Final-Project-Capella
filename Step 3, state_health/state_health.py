#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 20:22:32 2021

@author: abby
"""

import pandas as pd
import seaborn as sns

#Reading health data into dataframe.
state = pd.read_csv("YRBS2019_HS.csv")

#Dropping empty values.
badstate = state['HS_sleep'].isna()
state = state[badstate == False]

#Chaning columns/cleaning data.
state ["no_day"] = state["HS_one_day"]
state ["over1_not5"] = state["HS_5_days"] - state["HS_one_day"]
state ["over_5"] = 100 - state["HS_5_days"]

drop2 = ["HS_one_day", "HS_5_days", "HS_daily"]
state = state.drop(columns = drop2)

#Save file.
state.to_csv("state_health.csv", index = False)

#Defining data for pair plot.
pairplot = ["no_day", "over1_not5", "over_5", "HS_Obesity","HS_sleep", "HS_suicide"]
plot = state[pairplot]

#Pair plot. 
pairs = sns.pairplot(plot)
pairs.savefig("scatterhealth.png", dpi = 300)
