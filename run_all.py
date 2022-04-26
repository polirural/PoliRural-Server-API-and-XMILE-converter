import pysd
import pandas as pd
import numpy as np
import logging

dfo = pd.DataFrame()
logging.basicConfig(level=logging.DEBUG)

#   calcAggregatedIndex(regionData) {
#     let weightedSum = 0;
#     let sumWeight = 0;
#     for (const key of Object.keys(regionData) as any) {
#       if (key === 'MODEL' || key === 'TIME_STEP') {
#         continue;
#       }
#       const factorValues = regionData[key];
#       let sumValue = 0;
#       let n = 0;
#       for (const ds of factorValues.datasets) {
#         sumValue += ds.value;
#         n += 1;
#       }
#       weightedSum += sumValue * factorValues['weight'];
#       sumWeight += n * factorValues['weight'];
#     }
#     return weightedSum / sumWeight;
#   }


for model in [
        ["apulia_v2_p", "Apulia"],
        ["central_bohemia_p", "Central Bohemia"],
        ["central_greece_v2_p", "Central Greece"],
        ["galilee_v2_p", "Galilee"],
        ["gevgelija_v2_p", "Gevgelija"],
        ["hame_v2_p", "Hame"], 
        ["monaghan_v2_p", "Monaghan"],
        ["segobriga_v2_p", "Segobriga"],
        ["vidzeme_v2_p", "Vidzeme"]
    ]:
    
    logging.info("Processing %s" , model[1])

    pysd_model = pysd.load(f'models/{model[0]}.py', missing_values="warning")
    stocks = pysd_model.run()
    stocks = stocks[[
        "farms",
        "Natural_Capital",
        "NEWCOMERS",
        "broadband_infrastructure_population_covered",
        "proportion_of_newcomers",
        "shared_knowledge",
        "social_innovation",
        "tourist_visitors",
        "workforce_specialization",
        "INFANTS",
        "ELDERLY_POPULATION",
        "SCHOOL_AGE_POPULATION",
        "POST_SCHOOL_POPULATION",
        "WORKING_AGE_POPULATION",
        "WORKING_AGE_RURAL_POPULATION",
        "total_rural_population"
    ]]
    stocks["MODEL"] = model[1]
    
    stocks["proportion_INFANTS"] = stocks["INFANTS"] / stocks["total_rural_population"]
    stocks["proportion_ELDERLY_POPULATION"] = stocks["ELDERLY_POPULATION"] / stocks["total_rural_population"]
    stocks["proportion_SCHOOL_AGE_POPULATION"] = stocks["SCHOOL_AGE_POPULATION"] / stocks["total_rural_population"]
    stocks["proportion_POST_SCHOOL_POPULATION"] = stocks["POST_SCHOOL_POPULATION"] / stocks["total_rural_population"]
    stocks["proportion_WORKING_AGE_POPULATION"] = stocks["WORKING_AGE_POPULATION"] / stocks["total_rural_population"]
    stocks["proportion_NEWCOMERS"] = stocks["NEWCOMERS"] / stocks["total_rural_population"]
    
    stocks["TIME_STEP"] = stocks.index
    stocks.insert(0, 'TIME_STEP', stocks.pop('TIME_STEP'))

    dfo = dfo.append(stocks)
    # stocks.index.rename('TIME_STEP', inplace=True)

dfo = dfo[(dfo["TIME_STEP"] >= 2015) & (dfo["TIME_STEP"] <= 2040)]

dfo.to_csv("./tmp/all_data.csv", index=False)
