#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 12:55:39 2021

@author: abby
"""
import pandas as pd
import geopandas

healthdata = pd.read_csv("health_data.csv")
healthdata = healthdata.set_index("State")
healthdata = healthdata.drop(["score"], axis=1)

reqs = pd.read_csv("hs_reqs.csv")
reqs = reqs.rename(columns = {"Unnamed: 0": "State"})
reqs = reqs.set_index("State")

statedata = healthdata.join(reqs)

statedata.to_csv("state_data")
statedata.to_stata("state_data.dta")

#Exporting for map.

states = geopandas.read_file("zip://tl_2020_us_state.zip")

statedata = statedata.reset_index()
statedata = statedata.rename(columns={"State":"STUSPS"})
states_map = states.merge(statedata, on = "STUSPS", how = 'outer', indicator = True)
print(states_map["_merge"].value_counts())
states_map = states_map.drop(["_merge"], axis=1)


states_map.to_file("statedata.gpkg", driver = "GPKG")

