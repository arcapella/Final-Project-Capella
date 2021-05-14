#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 17:32:19 2021

@author: abby
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

corr = pd.read_csv("correlations.csv")
corr = corr.drop(9)
rename = {"Unnamed: 0" : "Requirement"}
corr = corr.rename(columns=rename)
corr=corr.set_index("Requirement")

fig, ax1 = plt.subplots(dpi=300, figsize = (5,5))
sns.heatmap(corr, annot=True, ax=ax1, cmap="RdYlBu")
ax1.set_xlabel("Health Outcome")
ax1.set_ylabel("Requirement")

fig.savefig("reg_heatmap.png",dpi=300, bbox_inches = "tight")

