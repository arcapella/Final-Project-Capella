#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 12:55:39 2021

@author: abby
"""
import pandas as pd

healthdata = pd.read_csv("health_data.csv")
healthdata = healthdata.set_index("State")
healthdata = healthdata.drop(["score"], axis=1)

reqs = pd.read_csv("hs_reqs.csv")
reqs = reqs.rename(columns = {"Unnamed: 0": "State"})
reqs = reqs.set_index("State")

statedata = healthdata.join(reqs)

statedata.to_csv("state_data")
statedata.to_stata("state_data.dta")
