#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 20:55:53 2021

@author: abby
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Read and clean health data.
state = pd.read_csv("state_health.csv")
print(len(state))


#Heatmaps of health characteristics.
state = state.set_index("State")

drop1 = ["HS_sleep", "HS_Obesity", "HS_suicide", "no_day"]
graph1 = state.drop(drop1, axis=1)

drop2 = [ "HS_sleep", "over_5", "over1_not5"]
graph2 = state.drop(drop2, axis=1)

drop3 = ["HS_Obesity", "no_day", "over_5", "over1_not5", "HS_suicide"]
graph3 = state.drop(drop3, axis=1)

fig = plt.figure(figsize = (15,30)) # width x heigh
ax1 = fig.add_subplot(3, 3, 1) # row, column, position
ax2 = fig.add_subplot(3, 3, 2)
ax3 = fig.add_subplot(3, 3, 3)
sns.heatmap(graph1, annot=True, ax=ax1, cmap="coolwarm")
ax1.set_xlabel("Health")
ax1.set_ylabel("State")
sns.heatmap(graph2, annot=True, ax=ax2, cmap="coolwarm")
ax2.set_xlabel("Health")
ax2.set_ylabel("State")
sns.heatmap(graph3, annot=True, ax=ax3, cmap="coolwarm")
ax3.set_xlabel("Health")
ax3.set_ylabel("State")
fig.tight_layout()
fig.savefig("HealthbyState.png")

#Read req data, create score column, keep scores. 
reqs = pd.read_csv("hs_reqs.csv")
rename = {"Unnamed: 0": "State"}
reqs.rename(columns=rename, inplace=True)
keep = ["State", "score"]
reqs = reqs[keep]

#Merging health data with policy data.
statedata = state.merge(reqs, how = "inner", on = "State", indicator = True)
print(statedata["_merge"].value_counts())
statedata = statedata.drop("_merge", axis = 1)

statedata.to_csv("health_data.csv", index = False)


#Scatter states quadrants. 

labels = pd.read_csv("labels.csv")
labels=labels.replace({None:" "})

#1: Obesity
fig, ax1 = plt.subplots(dpi=300)
obesity = sns.scatterplot(data= statedata, y='score', x= "HS_Obesity")
fig.suptitle("Average Obesity Rates Based on State Score")
ax1.set_xlabel("Average Rate of Obesity")
ax1.set_ylabel("Score")
ax1.axhline(4.5)
ax1.axvline(statedata["HS_Obesity"].median())
for line in range(0,statedata.shape[0]):
        obesity.text(statedata["HS_Obesity"][line]+0.01, statedata["score"][line], 
                labels["label1"][line], horizontalalignment='left', 
                size='medium', color='black', weight='semibold')
fig.tight_layout()
fig.savefig("scores_obesity.png")

#2: Less than 1 day of activity.
fig, ax1 = plt.subplots(dpi=300)
daily = sns.scatterplot(data= statedata, y='score', x= "no_day")
fig.suptitle("Average % of No P.A. Based on State Score")
ax1.set_xlabel("Avg. Rate of Students With <1 day of P.A.")
ax1.set_ylabel("Score")
ax1.axhline(4.5)
ax1.axvline(statedata["no_day"].median())
for line in range(0,statedata.shape[0]):
        daily.text(statedata["no_day"][line]+0.01, statedata["score"][line], 
                labels["label2"][line], horizontalalignment='left', 
                size='medium', color='black', weight='semibold')
fig.tight_layout()
fig.savefig("scores_not1.png")

#3: Suicide. 
fig, ax1 = plt.subplots(dpi=300)
suicide = sns.scatterplot(data= statedata, y='score', x= "HS_suicide")
fig.suptitle("Avg. % Considering Suicide Based on State Score")
ax1.set_xlabel("Avg. % Students that Seriously Considered Attempting Suicide ")
ax1.set_ylabel("Score")
ax1.axhline(4.5)
ax1.axvline(statedata["HS_suicide"].median())
for line in range(0,statedata.shape[0]):
        suicide.text(statedata["HS_suicide"][line]+0.01, statedata["score"][line], 
                labels["label3"][line], horizontalalignment='left', 
                size='medium', color='black', weight='semibold')
fig.tight_layout()
fig.savefig("scores_suicide.png")

#4: Activity less than 5 days but more than 1.
fig, ax1 = plt.subplots(dpi=300)
suicide = sns.scatterplot(data= statedata, y='score', x= "over1_not5")
fig.suptitle("Avg. % More than 1 day but less than 5 of P.A. Based on State Score")
ax1.set_xlabel("Avg.% Students w/ More Than 1 Day but less than 5 of P.A. Per Week")
ax1.set_ylabel("Score")
ax1.axhline(4.5)
ax1.axvline(statedata["over1_not5"].median())
for line in range(0,statedata.shape[0]):
        suicide.text(statedata["over1_not5"][line]+0.01, statedata["score"][line], 
                labels["label4"][line], horizontalalignment='left', 
                size='medium', color='black', weight='semibold')
fig.tight_layout()
fig.savefig("scores_1to5.png")

#5: Sleep.
fig, ax1 = plt.subplots(dpi=300)
suicide = sns.scatterplot(data= statedata, y='score', x= "HS_sleep")
fig.suptitle("HS Sleep Patterns Based on State Score")
ax1.set_xlabel("Avg. % Students Sleeping less than 8 Hours/Night")
ax1.set_ylabel("Score")
ax1.axhline(4.5)
ax1.axvline(statedata["HS_sleep"].median())
for line in range(0,statedata.shape[0]):
        suicide.text(statedata["HS_sleep"][line]+0.01, statedata["score"][line], 
                labels["label5"][line], horizontalalignment='left', 
                size='medium', color='black', weight='semibold')
fig.tight_layout()
fig.savefig("scores_sleep.png")

#6: Over 5 Days of PA.
fig, ax1 = plt.subplots(dpi=300)
suicide = sns.scatterplot(data= statedata, y='score', x= "over_5")
fig.suptitle("Avg. % More Than 5 Days of P.A. Based on State Score")
ax1.set_xlabel("Avg.% Students w/ More Than 5 Days of P.A. per Week")
ax1.set_ylabel("Score")
ax1.axhline(4.5)
ax1.axvline(statedata["over_5"].median())
for line in range(0,statedata.shape[0]):
        suicide.text(statedata["over_5"][line]+0.01, statedata["score"][line], 
                labels["label6"][line], horizontalalignment='left', 
                size='medium', color='black', weight='semibold')
fig.tight_layout()
fig.savefig("scores_over5.png")


