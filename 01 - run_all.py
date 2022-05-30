import pysd
import pandas as pd
import numpy as np
import logging

dfo = pd.DataFrame()
logging.basicConfig(level=logging.DEBUG)

scenarios = {'INFR mix': [{'model': 'monaghan_v2_p', 'infrastructures_objective': 3000.0, 'population_covered_objective': 95.0}, {'model': 'galilee_v2_p', 'infrastructures_objective': 2000.0, 'population_covered_objective': 70.0}, {'model': 'segobriga_v2_p', 'infrastructures_objective': 1000.0, 'population_covered_objective': 85.0, 'akis_evolution': 3.2, 'cap_ecoschemes': 4.0, 'additional_institutional_support': 70.0}, {'model': 'vidzeme_v2_p', 'population_covered_objective': 95.0}, {'model': 'hame_v2_p', 'infrastructures_objective': 2000.0, 'population_covered_objective': 90.0}, {'model': 'central_greece_v3_p', 'infrastructures_objective': 12000.0, 'population_covered_objective': 75.0}, {'model': 'apulia_v2_p', 'infrastructures_objective': 450.0, 'population_covered_objective': 90.0}, {'model': 'central_bohemia_p', 'infrastructures_objective': 12000.0, 'population_covered_objective': 80.0}], 'INFR Focus Broadband': [{'model': 'monaghan_v2_p', 'infrastructures_objective': 2500.0, 'population_covered_objective': 100.0}, {'model': 'galilee_v2_p', 'infrastructures_objective': 1500.0, 'population_covered_objective': 100.0}, {'model': 'segobriga_v2_p', 'infrastructures_objective': 900.0, 'population_covered_objective': 100.0}, {'model': 'vidzeme_v2_p', 'population_covered_objective': 100.0}, {'model': 'hame_v2_p', 'infrastructures_objective': 1550.0, 'population_covered_objective': 100.0}, {'model': 'central_greece_v3_p', 'infrastructures_objective': 9500.0, 'population_covered_objective': 100.0}, {'model': 'apulia_v2_p', 'infrastructures_objective': 350.0, 'population_covered_objective': 100.0}, {'model': 'central_bohemia_p', 'infrastructures_objective': 10000.0, 'population_covered_objective': 100.0}], 'INFR Focus Roads': [{'model': 'monaghan_v2_p', 'infrastructures_objective': 3200.0, 'population_covered_objective': 53.0}, {'model': 'galilee_v2_p', 'infrastructures_objective': 2500.0, 'population_covered_objective': 50.0}, {'model': 'segobriga_v2_p', 'infrastructures_objective': 1500.0, 'population_covered_objective': 70.0}, {'model': 'vidzeme_v2_p', 'population_covered_objective': 89.0}, {'model': 'hame_v2_p', 'infrastructures_objective': 2500.0, 'population_covered_objective': 70.0}, {'model': 'central_greece_v3_p', 'infrastructures_objective': 17000.0, 'population_covered_objective': 50.0}, {'model': 'apulia_v2_p', 'infrastructures_objective': 600.0, 'population_covered_objective': 80.0}, {'model': 'central_bohemia_p', 'infrastructures_objective': 16000.0, 'population_covered_objective': 55.0}], 'AGRI Focus AKIS': [{'model': 'monaghan_v2_p', 'akis_evolution': 4.0, 'cap_ecoschemes': 2.5}, {'model': 'galilee_v2_p', 'akis_evolution': 4.5, 'cap_ecoschemes': 2.5}, {'model': 'segobriga_v2_p', 'akis_evolution': 3.5, 'cap_ecoschemes': 2.0}, {'model': 'vidzeme_v2_p', 'akis_evolution': 4.5, 'cap_ecoschemes': 2.5}, {'model': 'hame_v2_p', 'akis_evolution': 5.0, 'cap_ecoschemes': 2.0}, {'model': 'central_greece_v3_p', 'akis_evolution': 5.0, 'cap_ecoschemes': 2.0}, {'model': 'apulia_v2_p', 'akis_evolution': 5.0, 'cap_ecoschemes': 2.0}, {'model': 'central_bohemia_p'}], 'AGRI Focus Eco-Schemes': [{'model': 'monaghan_v2_p', 'akis_evolution': 3.0, 'cap_ecoschemes': 3.5}, {'model': 'galilee_v2_p', 'akis_evolution': 3.0, 'cap_ecoschemes': 5.0}, {'model': 'segobriga_v2_p', 'akis_evolution': 2.5, 'cap_ecoschemes': 5.0}, {'model': 'vidzeme_v2_p', 'akis_evolution': 3.0, 'cap_ecoschemes': 5.0}, {'model': 'hame_v2_p', 'akis_evolution': 3.0, 'cap_ecoschemes': 5.0}, {'model': 'central_greece_v3_p', 'akis_evolution': 3.0, 'cap_ecoschemes': 5.0}, {'model': 'apulia_v2_p', 'akis_evolution': 3.0, 'cap_ecoschemes': 5.0}, {'model': 'central_bohemia_p'}], 'AGRI Mix': [{'model': 'monaghan_v2_p', 'akis_evolution': 3.5, 'cap_ecoschemes': 2.8}, {'model': 'galilee_v2_p', 'akis_evolution': 3.6, 'cap_ecoschemes': 4.0}, {'model': 'segobriga_v2_p', 'akis_evolution': 3.0, 'cap_ecoschemes': 3.0}, {'model': 'vidzeme_v2_p', 'akis_evolution': 3.5, 'cap_ecoschemes': 3.5}, {'model': 'hame_v2_p', 'akis_evolution': 4.0, 'cap_ecoschemes': 4.0}, {'model': 'central_greece_v3_p', 'akis_evolution': 4.0, 'cap_ecoschemes': 3.0}, {'model': 'apulia_v2_p', 'akis_evolution': 4.0, 'cap_ecoschemes': 4.0}, {'model': 'central_bohemia_p'}], 'ENTRP High': [{'model': 'monaghan_v2_p', 'inst_support_evolution': 3500000.0}, {'model': 'galilee_v2_p', 'inst_support_evolution': 5.0}, {'model': 'segobriga_v2_p', 'additional_institutional_support': 75.0}, {'model': 'vidzeme_v2_p', 'inst_support_evolution': 2000000.0}, {'model': 'hame_v2_p', 'inst_support_evolution': 0.75}, {'model': 'central_greece_v3_p', 'inst_support_evolution': 21000000.0}, {'model': 'apulia_v2_p', 'inst_support_evolution': 4.0}, {'model': 'central_bohemia_p', 'inst_support_evolution': 3.0}], 'ENTRP Medium': [{'model': 'monaghan_v2_p', 'inst_support_evolution': 2000000.0}, {'model': 'galilee_v2_p', 'inst_support_evolution': 3.5}, {'model': 'segobriga_v2_p', 'additional_institutional_support': 50.0}, {'model': 'vidzeme_v2_p', 'inst_support_evolution': 1500000.0}, {'model': 'hame_v2_p', 'inst_support_evolution': 0.45}, {'model': 'central_greece_v3_p', 'inst_support_evolution': 14000000.0}, {'model': 'apulia_v2_p', 'inst_support_evolution': 3.0}, {'model': 'central_bohemia_p', 'inst_support_evolution': 2.0}], 'ENTRP Low': [{'model': 'monaghan_v2_p', 'inst_support_evolution': 1000000.0}, {'model': 'galilee_v2_p', 'inst_support_evolution': 2.0}, {'model': 'segobriga_v2_p', 'additional_institutional_support': 25.0}, {'model': 'vidzeme_v2_p', 'inst_support_evolution': 700000.0}, {'model': 'hame_v2_p', 'inst_support_evolution': 0.2}, {'model': 'central_greece_v3_p', 'inst_support_evolution': 7000000.0}, {'model': 'apulia_v2_p', 'inst_support_evolution': 2.0}, {'model': 'central_bohemia_p', 'inst_support_evolution': 1.0}]}

scenarios["baseline"] = None

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


def create_lookup(value):
    def lookupFunc(x=None):
        return value
    return lookupFunc


for model in models:

    logging.info("Processing %s", model[1])

    pysd_model = pysd.load(f'models/{model[0]}.py', missing_values="warning")

    for scenario in scenarios:
        parameters = scenarios.get(scenario)
        parameters = next((x for x in parameters if x.get(
            "model") == model[0]), None) if parameters != None else None
        if parameters != None:                
            del parameters["model"]
            for k, v in parameters.items():
                parameters[k] = float(v)
                if k in ["akis_evolution", "inst_support_evolution", "cap_ecoschemes", "additional_institutional_support"]:
                    parameters[k] = create_lookup(float(v))

        logging.info("Processing scenario %s", scenario)
        stocks = pysd_model.run() if parameters == None else pysd_model.run(params=parameters)

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
        stocks["scenario"] = scenario

        stocks["proportion_INFANTS"] = stocks["INFANTS"] / \
            stocks["total_rural_population"]
        stocks["proportion_ELDERLY_POPULATION"] = stocks["ELDERLY_POPULATION"] / \
            stocks["total_rural_population"]
        stocks["proportion_SCHOOL_AGE_POPULATION"] = stocks["SCHOOL_AGE_POPULATION"] / \
            stocks["total_rural_population"]
        stocks["proportion_POST_SCHOOL_POPULATION"] = stocks["POST_SCHOOL_POPULATION"] / \
            stocks["total_rural_population"]
        stocks["proportion_WORKING_AGE_POPULATION"] = stocks["WORKING_AGE_POPULATION"] / \
            stocks["total_rural_population"]
        stocks["proportion_NEWCOMERS"] = stocks["NEWCOMERS"] / \
            stocks["total_rural_population"]

        stocks["TIME_STEP"] = stocks.index
        stocks.insert(0, 'TIME_STEP', stocks.pop('TIME_STEP'))
        stocks["domain"] = stocks["scenario"].apply(lambda s: s.split(' ')[0])

        dfo = dfo.append(stocks)
    # stocks.index.rename('TIME_STEP', inplace=True)

dfo = dfo[(dfo["TIME_STEP"] >= 2015) & (dfo["TIME_STEP"] <= 2040)]

dfo.to_csv("./tmp/all_data.csv", index=False)
