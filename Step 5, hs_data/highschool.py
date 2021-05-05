#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 19:42:24 2021

@author: abby
"""

import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

#Importing HS requirements and health data.
reqs = pd.read_csv("HS_Reqs.csv")
yrsb = pd.read_csv("YRBS2019_HS.csv")

reqs = reqs.rename({"Unnamed: 0":"State"}, axis=1)

#Merging requirements and health data.
hs_data = reqs.merge(yrsb, how="outer", indicator = True)
hs_data.set_index('State', inplace=True)
print(hs_data['score'].value_counts())
print(hs_data["_merge"].value_counts())
hs_data = hs_data.drop("_merge", axis = 1)

#Dropping states with no data.
state_bad = hs_data['HS_sleep'].isna()
hs_data = hs_data[state_bad == False]

#Saving as .csv
hs_data.to_csv("hs_data.csv")
hs_data.to_stata("hs_data.dta")

#Creating dataframe with means.
means = hs_data.groupby('score',).mean()
means.reset_index(inplace=True)


x = hs_data.groupby(["HS_required", "HS_minutes", "funding"]).size() 


#Creating graphs to show relationship between requirements and health data.fig, ax1 = plt.subplots(dpi=300)
fig, ax1 = plt.subplots(dpi=300)
sns.scatterplot(data= hs_data, y='score', x= "HS_Obesity")
fig.suptitle("Average Obesity Rates Based on State Score")
ax1.set_xlabel("Average Rate of Obesity")
ax1.set_ylabel("Scores")
ax1.axhline(5)
ax1.axvline(16)
fig.tight_layout()
fig.savefig("scores_obesity_HS.png")

#Creating graphs to show relationship between requirements and health data.fig, ax1 = plt.subplots(dpi=300)
sns.barplot(data= means, y='HS_Obesity', x= "score")
fig.suptitle("Average Obesity Rates Based on State Score")
ax1.set_xlabel("Scores")
ax1.set_ylabel("Average Rate of Obesity")
fig.tight_layout()
fig.savefig("scores_obesity_HS.png")

fig, ax1 = plt.subplots(dpi=300)
sns.barplot(data= means, y='HS_sleep', x= "score")
fig.suptitle("Adolescent Sleep Patterns Based on State Score")
ax1.set_xlabel("Scores")
ax1.set_ylabel("% Students Sleeping < 8 Hours/Night")
fig.tight_layout()
fig.savefig("scores_sleep_HS.png")


fig, ax1 = plt.subplots(dpi=300)
sns.barplot(data= means, y='HS_daily', x= "score")
fig.suptitle("Average Rates of Daily Physical Activity Based on State Score")
ax1.set_xlabel("Scores")
ax1.set_ylabel("Avg. Rate of Students Without Daily P.A. ")
fig.tight_layout()
fig.savefig("scores_daily_HS.png")

fig, ax1 = plt.subplots(dpi=300)
sns.barplot(data= means, y='HS_suicide', x= "score")
fig.suptitle("Average Rates of Considering Suicide Based on State Score")
ax1.set_xlabel("Scores")
ax1.set_ylabel("Avg. Rate of Students that Seriously Considered Attempting Suicide ")
fig.tight_layout()
fig.savefig("scores_suicide_HS.png")


fig, ax1 = plt.subplots(dpi=300)
sns.barplot(data= means, y='HS_one_day', x= "score")
fig.suptitle("Average Rates of Less Than 1 day of Physical Activity Based on State Score")
ax1.set_xlabel("Scores")
ax1.set_ylabel("Avg. Rate of Students w/ < 1 Day of P.A. ")
fig.tight_layout()
fig.savefig("scores_1day_HS.png")

fig, ax1 = plt.subplots(dpi=300)
sns.barplot(data= means, y='HS_5_days', x= "score")
fig.suptitle("Average Rates of Less Than 5 days of Physical Activity Based on State Score")
ax1.set_xlabel("Scores")
ax1.set_ylabel("Avg. Rate of Students w/ < 5 Days of P.A. ")
fig.tight_layout()
fig.savefig("scores_5days_HS.png")

fig, ax1 = plt.subplots(dpi=300)
ax = sns.boxenplot(data=hs_data, x="HS_minutes", y="HS_sleep", showfliers=False)
ax = sns.stripplot(data=hs_data, x="HS_minutes", y="HS_sleep", hue = 'score')

fig, ax1 = plt.subplots(dpi=300)
ax = sns.boxenplot(data=hs_data, x="no_subs", y="HS_one_day", showfliers=False)
ax = sns.stripplot(data=hs_data, x="no_subs", y="HS_one_day", hue = 'score')
