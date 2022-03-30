import pysd
import pandas as pd
import numpy as np
import logging

dfo = pd.DataFrame()
logging.basicConfig(level=logging.DEBUG)

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
        "ELDERLY_POPULATION",
        "farms",
        #"institutional_support",
        #"mean_local_income_per_farm",
        #"mobility_infrastructures",
        "Natural_Capital",
        "NEWCOMERS",
        "broadband_infrastructure_population_covered",
        "POST_SCHOOL_POPULATION",
        "proportion_of_newcomers",
        "SCHOOL_AGE_POPULATION",
        "shared_knowledge",
        "social_innovation",
        #"total_employment",
        "tourist_visitors",
        "workforce_specialization",
        "WORKING_AGE_POPULATION",
        "WORKING_AGE_RURAL_POPULATION"
    ]]
    stocks["MODEL"] = model[1]
    dfo = dfo.append(stocks)
    stocks.index.rename('TIME_STEP', inplace=True)

dfo.to_csv("./tmp/all_data.csv", index_label="TIME_STEP")
