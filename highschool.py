#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 19:42:24 2021

@author: abby
"""

import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

reqs = pd.read_csv("HS_Reqs.csv")
yrsb = pd.read_csv("YRBS2019_HS.csv")

reqs = reqs.rename({"Unnamed: 0":"State"}, axis=1)

hs_data = reqs.merge(yrsb, how="outer")
hs_data.set_index('State')

fig, ax1 = plt.subplots(dpi=300)
sns.scatterplot(data=hs_data, x="score", y="HS_Obesity", ax=ax1)

