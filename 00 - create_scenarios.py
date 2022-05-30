import pysd
import pandas as pd
import numpy as np
import logging

t = pd.read_excel("D:\\Desktop\\Polirural\\Experiment2 (version 2).xlsx", "Sheet1")

model_names = t["model"].drop_duplicates()
scenario_names = t["scenario"].drop_duplicates()

print (scenario_names)
scenarios = {}

for sn in scenario_names:
    scenarios[sn] = []  
    for mn in model_names:
        selection = t.loc[(t["model"] == mn) & (t["scenario"] == sn)].copy()
        if mn == "segobriga_v2_p":
            selection = selection.rename(columns={"inst_support_evolution": "additional_institutional_support"})
        if mn == "vidzeme_v2_p":
            selection = selection.drop(columns=["infrastructures_objective"])

        for ridx, row in selection.iterrows():
            rowdata = row.copy()
            rowdata = rowdata.dropna()
            del rowdata["name"]
            del rowdata["scenario"]
            scenarios[sn].append(rowdata.to_dict())
print(scenarios)