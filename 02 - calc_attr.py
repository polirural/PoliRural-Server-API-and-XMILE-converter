import pysd
import pandas as pd
import numpy as np
import logging

models = [
    ["apulia_v2_p", "Apulia"],
    ["central_bohemia_p", "Central Bohemia"],
    ["central_greece_v3_p", "Central Greece"],
    ["galilee_v2_p", "Galilee"],
    ["gevgelija_v2_p", "Gevgelija"],
    ["hame_v2_p", "Hame"],
    ["monaghan_v2_p", "Monaghan"],
    ["segobriga_v2_p", "Segobriga"],
    ["vidzeme_v2_p", "Vidzeme"]
]

factors = [
    "broadband_infrastructure_population_covered",
    "workforce_specialization",
    "farms",
    "tourist_visitors",
    "Natural_Capital",
    "proportion_of_newcomers",
    "shared_knowledge",
    "social_innovation",
    "proportion_INFANTS",
    "proportion_ELDERLY_POPULATION",
    "proportion_SCHOOL_AGE_POPULATION",
    "proportion_POST_SCHOOL_POPULATION",
    "proportion_WORKING_AGE_POPULATION",
    "proportion_NEWCOMERS"]

pillar_environmental = [
    "Natural_Capital"
]

pillar_economy = [
    "broadband_infrastructure_population_covered",
    "workforce_specialization",
    "farms",
    "tourist_visitors",
    "Natural_Capital"]

pillar_social = [
    "proportion_of_newcomers",
    "shared_knowledge",
    "social_innovation",
    "proportion_INFANTS",
    "proportion_ELDERLY_POPULATION",
    "proportion_SCHOOL_AGE_POPULATION",
    "proportion_POST_SCHOOL_POPULATION",
    "proportion_WORKING_AGE_POPULATION",
    "proportion_NEWCOMERS"]

pillar_anthropic = [
    "broadband_infrastructure_population_covered",
]

pillars = {
    "environmental_attr": pillar_environmental,
    "economy_attr": pillar_economy,
    "social_attr": pillar_social,
    "anthropic_attr": pillar_anthropic
}

dfo = pd.read_csv("./tmp/all_data.csv")

scenario_names = [
    "baseline",
    "infrastructure",
    "agriculture",
    "entrepreneurship"
]

scenario_names = dfo["scenario"].drop_duplicates().to_list()


def drange(start, stop, step):
    o = []
    c = start
    while c <= stop:
        o.append(c)
        c += step
    return o


for tstep in drange(2015, 2040, 0.25):
    print(tstep)

    for scenario in scenario_names:

        sum_factors = 0
        sum_weights = 0

        for factor in factors:
            # print(factor)

            selection = dfo[(dfo["scenario"] == scenario)
                            & (dfo["TIME_STEP"] == tstep)]
            mean = selection[factor].mean()
            max = selection[factor].max()
            min = selection[factor].min()
            norm_val = (selection[factor] - min) / (max - min)
            sum_factors += selection[factor].sum()
            sum_weights += 1
            dfo.loc[(dfo["scenario"] == scenario) & (
                dfo["TIME_STEP"] == tstep), factor] = norm_val

        rur_attr = dfo[factors].sum(axis=1) / dfo[factors].count(axis=1)
        dfo.loc[(dfo["scenario"] == scenario) & (
            dfo["TIME_STEP"] == tstep), "rur_attr"] = rur_attr

        for pillar in pillars:
            pillar_attr = dfo[pillars.get(pillar)].sum(axis=1) / dfo[pillars.get(pillar)].count(axis=1)
            dfo.loc[(dfo["scenario"] == scenario) & (
                dfo["TIME_STEP"] == tstep), pillar] = pillar_attr


dfo.to_csv("./tmp/norm_data.csv", index=False,
           columns=["MODEL", "domain", "scenario", "TIME_STEP", "rur_attr", "environmental_attr", "economy_attr", "social_attr", "anthropic_attr"] + factors)
