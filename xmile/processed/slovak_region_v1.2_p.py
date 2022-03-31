"""
Python model 'slovak_region_v1.2_p.py'
Translated using PySD
"""

import numpy as np

from pysd.py_backend.functions import lookup, if_then_else, step, ramp
from pysd.py_backend.statefuls import Integ, Initial, Smooth, DelayN

__pysd_version__ = "2.0.0-dev"

__data = {"scope": None, "time": lambda: 0}

_subscript_dict = {}

_namespace = {
    "TIME": "time",
    "Time": "time",
    "time": "time",
    "mean_working_period_for_farmers": "mean_working_period_for_farmers",
    "abandonment_ratio": "abandonment_ratio",
    "farmer_retirement": "farmer_retirement",
    "generational_transition_ratio": "generational_transition_ratio",
    "retirement_substitution": "retirement_substitution",
    "retirement_not_covered": "retirement_not_covered",
    "max_agricultural_land": "max_agricultural_land",
    "potential_land_transformation": "potential_land_transformation",
    "potential_new_farms": "potential_new_farms",
    "CAP_Eco-Schemes": "cap_ecoschemes",
    "farming_attraction_factor": "farming_attraction_factor",
    "average_farm_area": "average_farm_area",
    "agricultural_land": "agricultural_land",
    "agriculture_profitability": "agriculture_profitability",
    "CAP_direct_payment": "cap_direct_payment",
    "agriculture_jobs": "agriculture_jobs",
    "CAP_reform_direct_payments_decrease_2021": "cap_reform_direct_payments_decrease_2021",
    "CAP_mean_proportion_of_direct_payment_to_FNVA": "cap_mean_proportion_of_direct_payment_to_fnva",
    "Eco-schemes_effect_on_direct_payment": "ecoschemes_effect_on_direct_payment",
    "initial_mean_income_per_farm": "initial_mean_income_per_farm",
    "technical_obsolescence_time": "technical_obsolescence_time",
    "agricultural_obsolescence_covered": "agricultural_obsolescence_covered",
    "mean_jobs_per_farm": "mean_jobs_per_farm",
    "initial_number_of_farms": "initial_number_of_farms",
    "final_technical_obsolescence_time": "final_technical_obsolescence_time",
    "time_for_slope": "time_for_slope",
    "normal_technical_obsolescence_time": "normal_technical_obsolescence_time",
    "vocational_training_campaign": "vocational_training_campaign",
    "students_university_campaign": "students_university_campaign",
    "workforce_specialization": "workforce_specialization",
    "time_to_become_VT_professional": "time_to_become_vt_professional",
    "time_to_become_graduated_professional": "time_to_become_graduated_professional",
    "working_lifetime_duration_for_VT": "working_lifetime_duration_for_vt",
    "working_lifetime_duration_for_GP": "working_lifetime_duration_for_gp",
    "working_lifetime_duration_for_NSW": "working_lifetime_duration_for_nsw",
    "initial_fraction_VT": "initial_fraction_vt",
    "VT_fraction_objective": "vt_fraction_objective",
    "initial_fraction_university_students": "initial_fraction_university_students",
    "university_students_objective": "university_students_objective",
    "graduate_migrating_ratio": "graduate_migrating_ratio",
    "VT_migrating_ratio": "vt_migrating_ratio",
    "unskilled_migrating_ratio": "unskilled_migrating_ratio",
    "years_for_education_campaign": "years_for_education_campaign",
    "total_regional_employment": "total_regional_employment",
    "workforce_as_ratio_of_WAP": "workforce_as_ratio_of_wap",
    "structural_unemployment": "structural_unemployment",
    "employment_gap": "employment_gap",
    "relative_employment_gap": "relative_employment_gap",
    "total_workforce": "total_workforce",
    "total_employment": "total_employment",
    "total_services_job": "total_services_job",
    "tourism_jobs": "tourism_jobs",
    "services_ratio": "services_ratio",
    "primary_ratio": "primary_ratio",
    "industrial_ratio": "industrial_ratio",
    "total_industrial_jobs": "total_industrial_jobs",
    "Rest_of_primary_sector_jobs": "rest_of_primary_sector_jobs",
    "service_jobs": "service_jobs",
    "total_rural_population": "total_rural_population",
    "school_age_duration": "school_age_duration",
    "working_age_duration": "working_age_duration",
    "children_death_rate": "children_death_rate",
    "working_age_death_rate": "working_age_death_rate",
    "adapted_life_expectancy": "adapted_life_expectancy",
    "post_school_death_rate": "post_school_death_rate",
    "birth_rate": "birth_rate",
    "infant_duration": "infant_duration",
    "infant_death_rate": "infant_death_rate",
    "postschool_age_duration": "postschool_age_duration",
    "post_school_leaving_ratio_1": "post_school_leaving_ratio_1",
    "WA_leaving_ratio_1": "wa_leaving_ratio_1",
    "initial_rural_population": "initial_rural_population",
    "total_population_in_relation_to_initial_population": "total_population_in_relation_to_initial_population",
    "WA_migration_ratio": "wa_migration_ratio",
    "fertility_rate": "fertility_rate",
    "max_WA_population_living_rural_per_year": "max_wa_population_living_rural_per_year",
    "max_post_school_leaving_per_year": "max_post_school_leaving_per_year",
    "smooth_life_expectancy": "smooth_life_expectancy",
    "life_expectancy": "life_expectancy",
    "proportion_of_newcomers": "proportion_of_newcomers",
    "integration_time": "integration_time",
    "life_expectancy_drop_2020_-_2022": "life_expectancy_drop_2020__2022",
    "PS_moving": "ps_moving",
    "WA_moving": "wa_moving",
    "elderly_move_rural": "elderly_move_rural",
    "housing_accessibility": "housing_accessibility",
    "maximum_elderly_population_moving": "maximum_elderly_population_moving",
    "housing_accessibility_factor_for_young": "housing_accessibility_factor_for_young",
    "housing_accessibility_factor_for_WA": "housing_accessibility_factor_for_wa",
    "housing_accessibility_factor_for_elderly": "housing_accessibility_factor_for_elderly",
    "employment_gap_1": "employment_gap_1",
    "total_population_in_relation_with_initial_population": "total_population_in_relation_with_initial_population",
    "people_applying_employment_gap": "people_applying_employment_gap",
    "post_school_leaving_ratio": "post_school_leaving_ratio",
    "WA_leaving_ratio": "wa_leaving_ratio",
    "effect_of_employment_in_PS_leaving_ratio": "effect_of_employment_in_ps_leaving_ratio",
    "housing_factor_for_young": "housing_factor_for_young",
    "employment_factor_for_young": "employment_factor_for_young",
    "effect_of_employment_in_WA_leaving_ratio": "effect_of_employment_in_wa_leaving_ratio",
    "farms": "farms",
    "average_local_income_per_farm": "average_local_income_per_farm",
    "VT_STUDENTS": "vt_students",
    "UNIVERSITY_STUDENTS": "university_students",
    "UNSKILLED_WORKERS": "unskilled_workers",
    "VT_PROFESSIONALS": "vt_professionals",
    "GRADUATED_PROFESSIONALS": "graduated_professionals",
    "SCHOOL_AGE_POPULATION": "school_age_population",
    "WORKING_AGE_POPULATION": "working_age_population",
    "ELDERLY_POPULATION": "elderly_population",
    "POST_SCHOOL_POPULATION": "post_school_population",
    "INFANTS": "infants",
    "NEWCOMERS": "newcomers",
    "increasing_farms": "increasing_farms",
    "decreasing_farms": "decreasing_farms",
    "improving_income_per_farm": "improving_income_per_farm",
    "decreasing_income_per_farm": "decreasing_income_per_farm",
    "entering_VT": "entering_vt",
    "entering_university": "entering_university",
    "early_working_entrance": "early_working_entrance",
    "becoming_vt_professional": "becoming_vt_professional",
    "becoming_graduated_professional": "becoming_graduated_professional",
    "graduated_migration_net_flow": "graduated_migration_net_flow",
    "NSW_retitiring": "nsw_retitiring",
    "VTW_retiring": "vtw_retiring",
    "GradW_retiring": "gradw_retiring",
    "VT_professionals_leaving": "vt_professionals_leaving",
    "apfx_not_specialized_workers_leaving": "apfx_not_specialized_workers_leaving",
    "births": "births",
    "aging_1": "aging_1",
    "aging_3": "aging_3",
    "children_net_migration": "children_net_migration",
    "rural_children_deaths": "rural_children_deaths",
    "working_age_net_migration": "working_age_net_migration",
    "working_age_deaths": "working_age_deaths",
    "elderly_net_migration": "elderly_net_migration",
    "elderly_deaths": "elderly_deaths",
    "post_school_net_migration": "post_school_net_migration",
    "Rural_Post_school_age_deaths": "rural_post_school_age_deaths",
    "aging": "aging",
    "infant_net_migration": "infant_net_migration",
    "rural_infant_deaths": "rural_infant_deaths",
    "aging_2": "aging_2",
    "newcomers_arrival": "newcomers_arrival",
    "newcomers_integration": "newcomers_integration",
    "WORKING_AGE_RURAL_POPULATION": "working_age_rural_population",
}

_dependencies = {
    "mean_working_period_for_farmers": {},
    "abandonment_ratio": {"agriculture_profitability": 1},
    "farmer_retirement": {"farms": 1, "mean_working_period_for_farmers": 1},
    "generational_transition_ratio": {"time": 1},
    "retirement_substitution": {
        "farmer_retirement": 1,
        "generational_transition_ratio": 1,
    },
    "retirement_not_covered": {"farmer_retirement": 1, "retirement_substitution": 1},
    "max_agricultural_land": {},
    "potential_land_transformation": {
        "max_agricultural_land": 1,
        "agricultural_land": 1,
    },
    "potential_new_farms": {"potential_land_transformation": 1, "average_farm_area": 1},
    "cap_ecoschemes": {"time": 1},
    "farming_attraction_factor": {"agriculture_profitability": 1},
    "average_farm_area": {},
    "agricultural_land": {"farms": 1, "average_farm_area": 1},
    "agriculture_profitability": {
        "average_local_income_per_farm": 1,
        "cap_direct_payment": 1,
    },
    "cap_direct_payment": {
        "cap_mean_proportion_of_direct_payment_to_fnva": 1,
        "cap_reform_direct_payments_decrease_2021": 1,
        "time": 2,
        "ecoschemes_effect_on_direct_payment": 1,
    },
    "agriculture_jobs": {"farms": 1, "mean_jobs_per_farm": 1},
    "cap_reform_direct_payments_decrease_2021": {},
    "cap_mean_proportion_of_direct_payment_to_fnva": {},
    "ecoschemes_effect_on_direct_payment": {"cap_ecoschemes": 1},
    "initial_mean_income_per_farm": {},
    "technical_obsolescence_time": {
        "normal_technical_obsolescence_time": 2,
        "final_technical_obsolescence_time": 1,
        "time_for_slope": 1,
        "time": 1,
    },
    "agricultural_obsolescence_covered": {},
    "mean_jobs_per_farm": {},
    "initial_number_of_farms": {},
    "final_technical_obsolescence_time": {},
    "time_for_slope": {},
    "normal_technical_obsolescence_time": {},
    "vocational_training_campaign": {
        "initial_fraction_vt": 2,
        "vt_fraction_objective": 1,
        "time": 1,
    },
    "students_university_campaign": {
        "initial_fraction_university_students": 2,
        "university_students_objective": 1,
        "time": 1,
    },
    "workforce_specialization": {
        "vt_professionals": 2,
        "graduated_professionals": 2,
        "unskilled_workers": 1,
    },
    "time_to_become_vt_professional": {},
    "time_to_become_graduated_professional": {},
    "working_lifetime_duration_for_vt": {},
    "working_lifetime_duration_for_gp": {},
    "working_lifetime_duration_for_nsw": {},
    "initial_fraction_vt": {},
    "vt_fraction_objective": {},
    "initial_fraction_university_students": {},
    "university_students_objective": {},
    "graduate_migrating_ratio": {},
    "vt_migrating_ratio": {},
    "unskilled_migrating_ratio": {},
    "years_for_education_campaign": {},
    "total_regional_employment": {
        "agriculture_jobs": 1,
        "total_industrial_jobs": 1,
        "total_services_job": 1,
        "rest_of_primary_sector_jobs": 1,
    },
    "workforce_as_ratio_of_wap": {},
    "structural_unemployment": {"workforce_specialization": 1},
    "employment_gap": {"total_employment": 1, "total_workforce": 1},
    "relative_employment_gap": {"employment_gap": 1, "total_workforce": 1},
    "total_workforce": {
        "working_age_rural_population": 1,
        "workforce_as_ratio_of_wap": 1,
        "structural_unemployment": 1,
    },
    "total_employment": {"total_regional_employment": 1},
    "total_services_job": {"service_jobs": 1, "tourism_jobs": 1},
    "tourism_jobs": {"time": 1},
    "services_ratio": {"total_services_job": 1, "total_employment": 1},
    "primary_ratio": {
        "agriculture_jobs": 1,
        "rest_of_primary_sector_jobs": 1,
        "total_employment": 1,
    },
    "industrial_ratio": {"total_industrial_jobs": 1, "total_employment": 1},
    "total_industrial_jobs": {"time": 1},
    "rest_of_primary_sector_jobs": {"time": 1},
    "service_jobs": {"time": 1},
    "total_rural_population": {
        "infants": 1,
        "school_age_population": 1,
        "working_age_population": 1,
        "elderly_population": 1,
        "post_school_population": 1,
    },
    "school_age_duration": {},
    "working_age_duration": {},
    "children_death_rate": {},
    "working_age_death_rate": {},
    "adapted_life_expectancy": {
        "life_expectancy": 1,
        "smooth_life_expectancy": 2,
        "time": 2,
    },
    "post_school_death_rate": {},
    "birth_rate": {},
    "infant_duration": {},
    "infant_death_rate": {},
    "postschool_age_duration": {},
    "post_school_leaving_ratio_1": {"post_school_leaving_ratio": 1},
    "wa_leaving_ratio_1": {"wa_leaving_ratio": 1},
    "_initial_initial_rural_population": {
        "initial": {"total_rural_population": 1},
        "step": {},
    },
    "initial_rural_population": {"_initial_initial_rural_population": 1},
    "total_population_in_relation_to_initial_population": {
        "total_rural_population": 1,
        "initial_rural_population": 1,
    },
    "wa_migration_ratio": {"working_age_net_migration": 2, "working_age_population": 1},
    "fertility_rate": {},
    "max_wa_population_living_rural_per_year": {},
    "max_post_school_leaving_per_year": {},
    "_smooth_smooth_life_expectancy": {
        "initial": {"life_expectancy_drop_2020__2022": 1},
        "step": {"life_expectancy_drop_2020__2022": 1},
    },
    "smooth_life_expectancy": {"_smooth_smooth_life_expectancy": 1},
    "life_expectancy": {},
    "proportion_of_newcomers": {"newcomers": 1, "total_rural_population": 1},
    "integration_time": {},
    "life_expectancy_drop_2020__2022": {},
    "ps_moving": {
        "employment_gap_1": 2,
        "people_applying_employment_gap": 1,
        "housing_accessibility_factor_for_young": 1,
    },
    "wa_moving": {
        "employment_gap_1": 2,
        "people_applying_employment_gap": 1,
        "housing_accessibility_factor_for_wa": 1,
    },
    "elderly_move_rural": {
        "maximum_elderly_population_moving": 1,
        "housing_accessibility_factor_for_elderly": 1,
    },
    "housing_accessibility": {
        "total_population_in_relation_with_initial_population": 1
    },
    "maximum_elderly_population_moving": {},
    "housing_accessibility_factor_for_young": {"housing_accessibility": 1},
    "housing_accessibility_factor_for_wa": {"housing_accessibility": 1},
    "housing_accessibility_factor_for_elderly": {"housing_accessibility": 1},
    "employment_gap_1": {"employment_gap": 1},
    "total_population_in_relation_with_initial_population": {
        "total_population_in_relation_to_initial_population": 1
    },
    "people_applying_employment_gap": {},
    "post_school_leaving_ratio": {
        "housing_factor_for_young": 1,
        "employment_factor_for_young": 1,
    },
    "wa_leaving_ratio": {"effect_of_employment_in_wa_leaving_ratio": 1},
    "effect_of_employment_in_ps_leaving_ratio": {"relative_employment_gap": 1},
    "housing_factor_for_young": {"housing_accessibility": 1},
    "employment_factor_for_young": {"effect_of_employment_in_ps_leaving_ratio": 1},
    "effect_of_employment_in_wa_leaving_ratio": {"relative_employment_gap": 1},
    "increasing_farms": {"potential_new_farms": 1, "farming_attraction_factor": 1},
    "decreasing_farms": {
        "farms": 1,
        "abandonment_ratio": 1,
        "retirement_not_covered": 1,
    },
    "improving_income_per_farm": {
        "decreasing_income_per_farm": 1,
        "agricultural_obsolescence_covered": 1,
    },
    "decreasing_income_per_farm": {
        "average_local_income_per_farm": 1,
        "technical_obsolescence_time": 1,
    },
    "_delayn_entering_vt": {
        "initial": {
            "vocational_training_campaign": 1,
            "years_for_education_campaign": 1,
        },
        "step": {"vocational_training_campaign": 1, "years_for_education_campaign": 1},
    },
    "entering_vt": {"_delayn_entering_vt": 1},
    "_delayn_entering_university": {
        "initial": {
            "students_university_campaign": 1,
            "years_for_education_campaign": 1,
        },
        "step": {"students_university_campaign": 1, "years_for_education_campaign": 1},
    },
    "entering_university": {"_delayn_entering_university": 1},
    "early_working_entrance": {
        "aging_1": 1,
        "entering_vt": 1,
        "entering_university": 1,
    },
    "becoming_vt_professional": {"vt_students": 1, "time_to_become_vt_professional": 1},
    "becoming_graduated_professional": {
        "university_students": 1,
        "time_to_become_graduated_professional": 1,
    },
    "graduated_migration_net_flow": {
        "wa_migration_ratio": 1,
        "graduated_professionals": 1,
        "graduate_migrating_ratio": 1,
    },
    "nsw_retitiring": {"unskilled_workers": 1, "working_lifetime_duration_for_nsw": 1},
    "vtw_retiring": {"vt_professionals": 1, "working_lifetime_duration_for_vt": 1},
    "gradw_retiring": {
        "graduated_professionals": 1,
        "working_lifetime_duration_for_gp": 1,
    },
    "vt_professionals_leaving": {
        "wa_migration_ratio": 1,
        "vt_professionals": 1,
        "vt_migrating_ratio": 1,
    },
    "apfx_not_specialized_workers_leaving": {
        "wa_migration_ratio": 1,
        "unskilled_migrating_ratio": 1,
        "unskilled_workers": 1,
    },
    "births": {"total_rural_population": 1, "birth_rate": 1},
    "aging_1": {"school_age_population": 1, "school_age_duration": 1},
    "aging_3": {"working_age_population": 1, "working_age_duration": 1},
    "children_net_migration": {"working_age_net_migration": 1, "fertility_rate": 1},
    "rural_children_deaths": {"school_age_population": 1, "children_death_rate": 1},
    "working_age_net_migration": {
        "wa_moving": 1,
        "working_age_population": 1,
        "wa_leaving_ratio_1": 1,
        "max_wa_population_living_rural_per_year": 1,
    },
    "working_age_deaths": {"working_age_population": 1, "working_age_death_rate": 1},
    "elderly_net_migration": {"elderly_move_rural": 1},
    "_delayn_elderly_deaths": {
        "initial": {"adapted_life_expectancy": 1},
        "step": {"adapted_life_expectancy": 1},
    },
    "elderly_deaths": {"_delayn_elderly_deaths": 1},
    "post_school_net_migration": {
        "ps_moving": 1,
        "post_school_population": 1,
        "max_post_school_leaving_per_year": 1,
        "post_school_leaving_ratio_1": 1,
    },
    "rural_post_school_age_deaths": {
        "post_school_population": 1,
        "post_school_death_rate": 1,
    },
    "aging": {"infants": 1, "infant_duration": 1},
    "infant_net_migration": {"working_age_net_migration": 1, "fertility_rate": 1},
    "rural_infant_deaths": {"infants": 1, "infant_death_rate": 1},
    "aging_2": {"post_school_population": 1, "postschool_age_duration": 1},
    "newcomers_arrival": {
        "infant_net_migration": 1,
        "children_net_migration": 1,
        "ps_moving": 1,
        "wa_moving": 1,
        "elderly_move_rural": 1,
    },
    "newcomers_integration": {"newcomers": 1, "integration_time": 1},
    "working_age_rural_population": {"working_age_population": 1},
    "farms": {"_integ_farms": 1},
    "_integ_farms": {
        "initial": {"initial_number_of_farms": 1},
        "step": {"increasing_farms": 1, "decreasing_farms": 1},
    },
    "average_local_income_per_farm": {"_integ_average_local_income_per_farm": 1},
    "_integ_average_local_income_per_farm": {
        "initial": {"initial_mean_income_per_farm": 1},
        "step": {"improving_income_per_farm": 1, "decreasing_income_per_farm": 1},
    },
    "vt_students": {"_integ_vt_students": 1},
    "_integ_vt_students": {
        "initial": {},
        "step": {"entering_vt": 1, "becoming_vt_professional": 1},
    },
    "university_students": {"_integ_university_students": 1},
    "_integ_university_students": {
        "initial": {},
        "step": {"entering_university": 1, "becoming_graduated_professional": 1},
    },
    "unskilled_workers": {"_integ_unskilled_workers": 1},
    "_integ_unskilled_workers": {
        "initial": {},
        "step": {
            "early_working_entrance": 1,
            "nsw_retitiring": 1,
            "apfx_not_specialized_workers_leaving": 1,
        },
    },
    "vt_professionals": {"_integ_vt_professionals": 1},
    "_integ_vt_professionals": {
        "initial": {},
        "step": {
            "becoming_vt_professional": 1,
            "vtw_retiring": 1,
            "vt_professionals_leaving": 1,
        },
    },
    "graduated_professionals": {"_integ_graduated_professionals": 1},
    "_integ_graduated_professionals": {
        "initial": {},
        "step": {
            "becoming_graduated_professional": 1,
            "graduated_migration_net_flow": 1,
            "gradw_retiring": 1,
        },
    },
    "school_age_population": {"_integ_school_age_population": 1},
    "_integ_school_age_population": {
        "initial": {},
        "step": {
            "children_net_migration": 1,
            "aging": 1,
            "aging_1": 1,
            "rural_children_deaths": 1,
        },
    },
    "working_age_population": {"_integ_working_age_population": 1},
    "_integ_working_age_population": {
        "initial": {},
        "step": {
            "working_age_net_migration": 1,
            "aging_2": 1,
            "aging_3": 1,
            "working_age_deaths": 1,
        },
    },
    "elderly_population": {"_integ_elderly_population": 1},
    "_integ_elderly_population": {
        "initial": {},
        "step": {"aging_3": 1, "elderly_net_migration": 1, "elderly_deaths": 1},
    },
    "post_school_population": {"_integ_post_school_population": 1},
    "_integ_post_school_population": {
        "initial": {},
        "step": {
            "post_school_net_migration": 1,
            "aging_1": 1,
            "aging_2": 1,
            "rural_post_school_age_deaths": 1,
        },
    },
    "infants": {"_integ_infants": 1},
    "_integ_infants": {
        "initial": {},
        "step": {
            "births": 1,
            "infant_net_migration": 1,
            "aging": 1,
            "rural_infant_deaths": 1,
        },
    },
    "newcomers": {"_integ_newcomers": 1},
    "_integ_newcomers": {
        "initial": {},
        "step": {"newcomers_arrival": 1, "newcomers_integration": 1},
    },
    "initial_time": {},
    "final_time": {},
    "time_step": {},
    "saveper": {"time_step": 1},
}

##########################################################################
#                            CONTROL VARIABLES                           #
##########################################################################

_control_vars = {
    "initial_time": lambda: 2010,
    "final_time": lambda: 2040,
    "time_step": lambda: 1 / 4,
    "saveper": lambda: time_step(),
}


def _init_outer_references(data):
    for key in data:
        __data[key] = data[key]


def time():
    return __data["time"]()


def initial_time():
    """
    Real Name: INITIAL TIME
    Original Eqn: 2010
    Units: Years
    Limits: None
    Type: constant
    Subs: None

    The initial time for the simulation.
    """
    return __data["time"].initial_time()


def final_time():
    """
    Real Name: FINAL TIME
    Original Eqn: 2010
    Units: Years
    Limits: None
    Type: constant
    Subs: None

    The final time for the simulation.
    """
    return __data["time"].final_time()


def time_step():
    """
    Real Name: TIME STEP
    Original Eqn: 1/4
    Units: Years
    Limits: None
    Type: constant
    Subs: None

    The time step for the simulation.
    """
    return __data["time"].time_step()


def saveper():
    """
    Real Name: SAVEPER
    Original Eqn: 1/4
    Units: Years
    Limits: None
    Type: constant
    Subs: None

    The time step for the simulation.
    """
    return __data["time"].saveper()


##########################################################################
#                             MODEL VARIABLES                            #
##########################################################################


def mean_working_period_for_farmers():
    """
    Real Name: mean_working_period_for_farmers
    Original Eqn: 45
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 45


def abandonment_ratio(x=None):
    """
    Real Name: abandonment_ratio
    Original Eqn: agriculture_profitability
    Units: dmnl/year
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            agriculture_profitability(),
            [
                0.000,
                12.000,
                24.000,
                36.000,
                48.000,
                60.000,
                72.000,
                84.000,
                96.000,
                108.000,
                120.000,
            ],
            [
                0.998,
                0.995,
                0.980,
                0.931,
                0.786,
                0.500,
                0.214,
                0.069,
                0.020,
                0.005,
                0.002,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                0.000,
                12.000,
                24.000,
                36.000,
                48.000,
                60.000,
                72.000,
                84.000,
                96.000,
                108.000,
                120.000,
            ],
            [
                0.998,
                0.995,
                0.980,
                0.931,
                0.786,
                0.500,
                0.214,
                0.069,
                0.020,
                0.005,
                0.002,
            ],
        )
    )


def farmer_retirement():
    """
    Real Name: farmer_retirement
    Original Eqn: farms/mean_working_period_for_farmers
    Units: farm/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return farms() / mean_working_period_for_farmers()


def generational_transition_ratio(x=None):
    """
    Real Name: generational_transition_ratio
    Original Eqn: TIME
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    0-1
    """
    return (
        lookup(
            time(),
            [
                2010.000,
                2013.000,
                2016.000,
                2019.000,
                2022.000,
                2025.000,
                2028.000,
                2031.000,
                2034.000,
                2037.000,
                2040.000,
            ],
            [
                0.598,
                0.544,
                0.490,
                0.441,
                0.402,
                0.377,
                0.358,
                0.343,
                0.338,
                0.338,
                0.338,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                2010.000,
                2013.000,
                2016.000,
                2019.000,
                2022.000,
                2025.000,
                2028.000,
                2031.000,
                2034.000,
                2037.000,
                2040.000,
            ],
            [
                0.598,
                0.544,
                0.490,
                0.441,
                0.402,
                0.377,
                0.358,
                0.343,
                0.338,
                0.338,
                0.338,
            ],
        )
    )


def retirement_substitution():
    """
    Real Name: retirement_substitution
    Original Eqn: farmer_retirement*generational_transition_ratio
    Units: farm/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return farmer_retirement() * generational_transition_ratio()


def retirement_not_covered():
    """
    Real Name: retirement_not_covered
    Original Eqn: farmer_retirement-retirement_substitution
    Units: farm/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return farmer_retirement() - retirement_substitution()


def max_agricultural_land():
    """
    Real Name: max_agricultural_land
    Original Eqn: 1902100
    Units: ha
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 1902100


def potential_land_transformation():
    """
    Real Name: potential_land_transformation
    Original Eqn: MAX (0, max_agricultural_land-agricultural_land)
    Units: ha
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return max(0, max_agricultural_land() - agricultural_land())


def potential_new_farms():
    """
    Real Name: potential_new_farms
    Original Eqn: potential_land_transformation/average_farm_area
    Units: farm
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return potential_land_transformation() / average_farm_area()


def cap_ecoschemes(x=None):
    """
    Real Name: CAP_Eco-Schemes
    Original Eqn: TIME
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    0-5 over time
    """
    return (
        lookup(
            time(),
            [
                2021.000,
                2021.950,
                2022.900,
                2023.850,
                2024.800,
                2025.750,
                2026.700,
                2027.650,
                2028.600,
                2029.550,
                2030.500,
                2031.450,
                2032.400,
                2033.350,
                2034.300,
                2035.250,
                2036.200,
                2037.150,
                2038.100,
                2039.050,
                2040.000,
            ],
            [
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                2021.000,
                2021.950,
                2022.900,
                2023.850,
                2024.800,
                2025.750,
                2026.700,
                2027.650,
                2028.600,
                2029.550,
                2030.500,
                2031.450,
                2032.400,
                2033.350,
                2034.300,
                2035.250,
                2036.200,
                2037.150,
                2038.100,
                2039.050,
                2040.000,
            ],
            [
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
                2.000,
            ],
        )
    )


def farming_attraction_factor(x=None):
    """
        Real Name: farming_attraction_factor
        Original Eqn: agriculture_profitability
        Units: dmnl/year
        Limits: (None, None)
        Type: lookup
        Subs: None

        0 - 1
    for profitability*land access 0 - 100k
    """
    return (
        lookup(
            agriculture_profitability(),
            [
                0.000,
                12.500,
                25.000,
                37.500,
                50.000,
                62.500,
                75.000,
                87.500,
                100.000,
                112.500,
                125.000,
            ],
            [
                0.000,
                0.014,
                0.034,
                0.061,
                0.100,
                0.154,
                0.231,
                0.339,
                0.490,
                0.702,
                1.000,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                0.000,
                12.500,
                25.000,
                37.500,
                50.000,
                62.500,
                75.000,
                87.500,
                100.000,
                112.500,
                125.000,
            ],
            [
                0.000,
                0.014,
                0.034,
                0.061,
                0.100,
                0.154,
                0.231,
                0.339,
                0.490,
                0.702,
                1.000,
            ],
        )
    )


def average_farm_area():
    """
    Real Name: average_farm_area
    Original Eqn: 77.3
    Units: ha/farm
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 77.3


def agricultural_land():
    """
    Real Name: agricultural_land
    Original Eqn: farms*average_farm_area
    Units: ha
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return farms() * average_farm_area()


def agriculture_profitability():
    """
    Real Name: agriculture_profitability
    Original Eqn: average_local_income_per_farm*(1+CAP_direct_payment)
    Units: €/farm
    Limits: (None, None)
    Type: component
    Subs: None

    0 - 105 aprox

    """
    return average_local_income_per_farm() * (1 + cap_direct_payment())


def cap_direct_payment():
    """
    Real Name: CAP_direct_payment
    Original Eqn: CAP_mean_proportion_of_direct_payment_to_FNVA- STEP(CAP_reform_direct_payments_decrease_2021, 2021)+ STEP ("Eco-schemes_effect_on_direct_payment", 2021)
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        cap_mean_proportion_of_direct_payment_to_fnva()
        - step(__data["time"], cap_reform_direct_payments_decrease_2021(), 2021)
        + step(__data["time"], ecoschemes_effect_on_direct_payment(), 2021)
    )


def agriculture_jobs():
    """
    Real Name: agriculture_jobs
    Original Eqn: farms*mean_jobs_per_farm
    Units: job
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return farms() * mean_jobs_per_farm()


def cap_reform_direct_payments_decrease_2021():
    """
    Real Name: CAP_reform_direct_payments_decrease_2021
    Original Eqn: 0.50
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.50


def cap_mean_proportion_of_direct_payment_to_fnva():
    """
    Real Name: CAP_mean_proportion_of_direct_payment_to_FNVA
    Original Eqn: 0.68
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None

    FNVA farm net value added
    """
    return 0.68


def ecoschemes_effect_on_direct_payment(x=None):
    """
    Real Name: Eco-schemes_effect_on_direct_payment
    Original Eqn: "CAP_Eco-Schemes"
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            cap_ecoschemes(),
            [
                0.000,
                0.500,
                1.000,
                1.500,
                2.000,
                2.500,
                3.000,
                3.500,
                4.000,
                4.500,
                5.000,
            ],
            [
                0.000,
                0.003,
                0.006,
                0.010,
                0.014,
                0.019,
                0.024,
                0.029,
                0.036,
                0.042,
                0.050,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                0.000,
                0.500,
                1.000,
                1.500,
                2.000,
                2.500,
                3.000,
                3.500,
                4.000,
                4.500,
                5.000,
            ],
            [
                0.000,
                0.003,
                0.006,
                0.010,
                0.014,
                0.019,
                0.024,
                0.029,
                0.036,
                0.042,
                0.050,
            ],
        )
    )


def initial_mean_income_per_farm():
    """
    Real Name: initial_mean_income_per_farm
    Original Eqn: 59
    Units: €/farm
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 59


def technical_obsolescence_time():
    """
    Real Name: technical_obsolescence_time
    Original Eqn: normal_technical_obsolescence_time+ RAMP(((final_technical_obsolescence_time-normal_technical_obsolescence_time)/time_for_slope), 2021)
    Units: year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return normal_technical_obsolescence_time() + ramp(
        __data["time"],
        (
            (final_technical_obsolescence_time() - normal_technical_obsolescence_time())
            / time_for_slope()
        ),
        2021,
    )


def agricultural_obsolescence_covered():
    """
    Real Name: agricultural_obsolescence_covered
    Original Eqn: 2
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None

    0-1
    """
    return 2


def mean_jobs_per_farm():
    """
    Real Name: mean_jobs_per_farm
    Original Eqn: 3.72
    Units: job/farm
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 3.72


def initial_number_of_farms():
    """
    Real Name: initial_number_of_farms
    Original Eqn: 24460
    Units: farm
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 24460


def final_technical_obsolescence_time():
    """
    Real Name: final_technical_obsolescence_time
    Original Eqn: 15
    Units: year
    Limits: (2.0, 7.0)
    Type: constant
    Subs: None


    """
    return 15


def time_for_slope():
    """
    Real Name: time_for_slope
    Original Eqn: 19
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 19


def normal_technical_obsolescence_time():
    """
    Real Name: normal_technical_obsolescence_time
    Original Eqn: 15
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 15


def vocational_training_campaign():
    """
    Real Name: vocational_training_campaign
    Original Eqn: initial_fraction_VT+ STEP((VT_fraction_objective/100)-initial_fraction_VT, 2021)
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return initial_fraction_vt() + step(
        __data["time"], (vt_fraction_objective() / 100) - initial_fraction_vt(), 2021
    )


def students_university_campaign():
    """
    Real Name: students_university_campaign
    Original Eqn: initial_fraction_university_students+ STEP ((university_students_objective/100)-initial_fraction_university_students, 2021)
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return initial_fraction_university_students() + step(
        __data["time"],
        (university_students_objective() / 100)
        - initial_fraction_university_students(),
        2021,
    )


def workforce_specialization():
    """
    Real Name: workforce_specialization
    Original Eqn: (VT_PROFESSIONALS+GRADUATED_PROFESSIONALS)/(VT_PROFESSIONALS+GRADUATED_PROFESSIONALS+UNSKILLED_WORKERS)
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (vt_professionals() + graduated_professionals()) / (
        vt_professionals() + graduated_professionals() + unskilled_workers()
    )


def time_to_become_vt_professional():
    """
    Real Name: time_to_become_VT_professional
    Original Eqn: 3
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 3


def time_to_become_graduated_professional():
    """
    Real Name: time_to_become_graduated_professional
    Original Eqn: 5
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 5


def working_lifetime_duration_for_vt():
    """
    Real Name: working_lifetime_duration_for_VT
    Original Eqn: 42
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 42


def working_lifetime_duration_for_gp():
    """
    Real Name: working_lifetime_duration_for_GP
    Original Eqn: 40
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 40


def working_lifetime_duration_for_nsw():
    """
    Real Name: working_lifetime_duration_for_NSW
    Original Eqn: 45
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 45


def initial_fraction_vt():
    """
    Real Name: initial_fraction_VT
    Original Eqn: 0.62
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.62


def vt_fraction_objective():
    """
    Real Name: VT_fraction_objective
    Original Eqn: 62
    Units: dmnl
    Limits: (15.0, 30.0)
    Type: constant
    Subs: None


    """
    return 62


def initial_fraction_university_students():
    """
    Real Name: initial_fraction_university_students
    Original Eqn: 0.31
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.31


def university_students_objective():
    """
    Real Name: university_students_objective
    Original Eqn: 31
    Units: dmnl
    Limits: (5.0, 20.0)
    Type: constant
    Subs: None


    """
    return 31


def graduate_migrating_ratio():
    """
    Real Name: graduate_migrating_ratio
    Original Eqn: 0.6
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.6


def vt_migrating_ratio():
    """
    Real Name: VT_migrating_ratio
    Original Eqn: 0.3
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.3


def unskilled_migrating_ratio():
    """
    Real Name: unskilled_migrating_ratio
    Original Eqn: 0.1
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.1


def years_for_education_campaign():
    """
    Real Name: years_for_education_campaign
    Original Eqn: 2031-2021
    Units: year
    Limits: (3.0, 10.0)
    Type: component
    Subs: None

    Campaign starting in 2021. How many years? now it is fixed in 9
    """
    return 2031 - 2021


def total_regional_employment():
    """
    Real Name: total_regional_employment
    Original Eqn: agriculture_jobs+ total_industrial_jobs+ total_services_job+ Rest_of_primary_sector_jobs
    Units: job
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        agriculture_jobs()
        + total_industrial_jobs()
        + total_services_job()
        + rest_of_primary_sector_jobs()
    )


def workforce_as_ratio_of_wap():
    """
    Real Name: workforce_as_ratio_of_WAP
    Original Eqn: 0.84
    Units: job/person
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.84


def structural_unemployment(x=None):
    """
    Real Name: structural_unemployment
    Original Eqn: workforce_specialization
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    from 8% to 2% depending on workforce specialization
    """
    return (
        lookup(
            workforce_specialization(),
            [
                0.000,
                0.100,
                0.200,
                0.300,
                0.400,
                0.500,
                0.600,
                0.700,
                0.800,
                0.900,
                1.000,
            ],
            [
                0.080,
                0.080,
                0.079,
                0.076,
                0.067,
                0.050,
                0.033,
                0.024,
                0.021,
                0.020,
                0.020,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                0.000,
                0.100,
                0.200,
                0.300,
                0.400,
                0.500,
                0.600,
                0.700,
                0.800,
                0.900,
                1.000,
            ],
            [
                0.080,
                0.080,
                0.079,
                0.076,
                0.067,
                0.050,
                0.033,
                0.024,
                0.021,
                0.020,
                0.020,
            ],
        )
    )


def employment_gap():
    """
        Real Name: employment_gap
        Original Eqn: total_employment- total_workforce
        Units: job
        Limits: (None, None)
        Type: component
        Subs: None

        employment gap < 0 means unemployment
    employment gap > 0 you need people to work
    """
    return total_employment() - total_workforce()


def relative_employment_gap():
    """
    Real Name: relative_employment_gap
    Original Eqn: employment_gap/total_workforce
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return employment_gap() / total_workforce()


def total_workforce():
    """
    Real Name: total_workforce
    Original Eqn: WORKING_AGE_RURAL_POPULATION*workforce_as_ratio_of_WAP* (1-structural_unemployment)
    Units: job
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        working_age_rural_population()
        * workforce_as_ratio_of_wap()
        * (1 - structural_unemployment())
    )


def total_employment():
    """
    Real Name: total_employment
    Original Eqn: total_regional_employment
    Units: job
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return total_regional_employment()


def total_services_job():
    """
    Real Name: total_services_job
    Original Eqn: service_jobs +tourism_jobs
    Units: job
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return service_jobs() + tourism_jobs()


def tourism_jobs():
    """
    Real Name: tourism_jobs
    Original Eqn: (7576.9*LN(TIME-2009))+108435
    Units: job
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (7576.9 * np.log(time() - 2009)) + 108435


def services_ratio():
    """
    Real Name: services_ratio
    Original Eqn: total_services_job/total_employment
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return total_services_job() / total_employment()


def primary_ratio():
    """
    Real Name: primary_ratio
    Original Eqn: (agriculture_jobs+Rest_of_primary_sector_jobs)/total_employment
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (agriculture_jobs() + rest_of_primary_sector_jobs()) / total_employment()


def industrial_ratio():
    """
    Real Name: industrial_ratio
    Original Eqn: total_industrial_jobs/total_employment
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return total_industrial_jobs() / total_employment()


def total_industrial_jobs():
    """
    Real Name: total_industrial_jobs
    Original Eqn: (43987*LN(TIME-2009))+475821
    Units: job
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (43987 * np.log(time() - 2009)) + 475821


def rest_of_primary_sector_jobs():
    """
    Real Name: Rest_of_primary_sector_jobs
    Original Eqn: (-1763*LN(TIME-2009))+13705
    Units: job
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (-1763 * np.log(time() - 2009)) + 13705


def service_jobs():
    """
    Real Name: service_jobs
    Original Eqn: (11684*LN(TIME-2009))+557110
    Units: job
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (11684 * np.log(time() - 2009)) + 557110


def total_rural_population():
    """
    Real Name: total_rural_population
    Original Eqn: INFANTS+ SCHOOL_AGE_POPULATION+ WORKING_AGE_POPULATION+ ELDERLY_POPULATION+ POST_SCHOOL_POPULATION
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        infants()
        + school_age_population()
        + working_age_population()
        + elderly_population()
        + post_school_population()
    )


def school_age_duration():
    """
    Real Name: school_age_duration
    Original Eqn: 10
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 10


def working_age_duration():
    """
    Real Name: working_age_duration
    Original Eqn: 45
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 45


def children_death_rate():
    """
    Real Name: children_death_rate
    Original Eqn: 0.0000091
    Units: dmnl/year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.0000091


def working_age_death_rate():
    """
    Real Name: working_age_death_rate
    Original Eqn: 0.001755
    Units: dmnl/year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.001755


def adapted_life_expectancy():
    """
    Real Name: adapted_life_expectancy
    Original Eqn: (life_expectancy- STEP (smooth_life_expectancy, 2020)+ STEP(smooth_life_expectancy, 2022))- 65
    Units: year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        life_expectancy()
        - step(__data["time"], smooth_life_expectancy(), 2020)
        + step(__data["time"], smooth_life_expectancy(), 2022)
    ) - 65


def post_school_death_rate():
    """
    Real Name: post_school_death_rate
    Original Eqn: 0.00002475
    Units: dmnl/year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.00002475


def birth_rate():
    """
    Real Name: birth_rate
    Original Eqn: 0.011
    Units: dmnl/year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.011


def infant_duration():
    """
    Real Name: infant_duration
    Original Eqn: 5
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 5


def infant_death_rate():
    """
    Real Name: infant_death_rate
    Original Eqn: 0.0017
    Units: dmnl/year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.0017


def postschool_age_duration():
    """
    Real Name: postschool_age_duration
    Original Eqn: 5
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 5


def post_school_leaving_ratio_1():
    """
    Real Name: post_school_leaving_ratio_1
    Original Eqn: post_school_leaving_ratio
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return post_school_leaving_ratio()


def wa_leaving_ratio_1():
    """
    Real Name: WA_leaving_ratio_1
    Original Eqn: WA_leaving_ratio
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return wa_leaving_ratio()


_initial_initial_rural_population = Initial(
    lambda: total_rural_population(), "_initial_initial_rural_population"
)


def initial_rural_population():
    """
    Real Name: initial_rural_population
    Original Eqn: INIT (total_rural_population)
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _initial_initial_rural_population()


def total_population_in_relation_to_initial_population():
    """
    Real Name: total_population_in_relation_to_initial_population
    Original Eqn: total_rural_population/initial_rural_population
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return total_rural_population() / initial_rural_population()


def wa_migration_ratio():
    """
    Real Name: WA_migration_ratio
    Original Eqn: IF working_age_net_migration<0 THEN ABS(working_age_net_migration/WORKING_AGE_POPULATION) ELSE 0
    Units: dmnl/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return if_then_else(
        working_age_net_migration() < 0,
        lambda: abs(working_age_net_migration() / working_age_population()),
        lambda: 0,
    )


def fertility_rate():
    """
    Real Name: fertility_rate
    Original Eqn: 1.5
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 1.5


def max_wa_population_living_rural_per_year():
    """
    Real Name: max_WA_population_living_rural_per_year
    Original Eqn: 0.06
    Units: dmnl/year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.06


def max_post_school_leaving_per_year():
    """
    Real Name: max_post_school_leaving_per_year
    Original Eqn: 1
    Units: dmnl/year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 1


_smooth_smooth_life_expectancy = Smooth(
    lambda: life_expectancy_drop_2020__2022(),
    lambda: 5,
    lambda: life_expectancy_drop_2020__2022(),
    lambda: 3,
    "_smooth_smooth_life_expectancy",
)


def smooth_life_expectancy():
    """
    Real Name: smooth_life_expectancy
    Original Eqn: SMTH3("life_expectancy_drop_2020_-_2022", 5)
    Units: year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _smooth_smooth_life_expectancy()


def life_expectancy():
    """
    Real Name: life_expectancy
    Original Eqn: 77.7
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 77.7


def proportion_of_newcomers():
    """
    Real Name: proportion_of_newcomers
    Original Eqn: NEWCOMERS/total_rural_population
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return newcomers() / total_rural_population()


def integration_time():
    """
    Real Name: integration_time
    Original Eqn: 7
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 7


def life_expectancy_drop_2020__2022():
    """
    Real Name: life_expectancy_drop_2020_-_2022
    Original Eqn: 0
    Units: year
    Limits: (0.0, 3.0)
    Type: constant
    Subs: None


    """
    return 0


def ps_moving():
    """
    Real Name: PS_moving
    Original Eqn: IF employment_gap_1>0 THEN (employment_gap_1*people_applying_employment_gap)*0.1* housing_accessibility_factor_for_young ELSE 0
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None

    NCWFY + HAWFY = 0,5 (of the employment gap)
    """
    return if_then_else(
        employment_gap_1() > 0,
        lambda: (employment_gap_1() * people_applying_employment_gap())
        * 0.1
        * housing_accessibility_factor_for_young(),
        lambda: 0,
    )


def wa_moving():
    """
        Real Name: WA_moving
        Original Eqn: IF employment_gap_1>0 THEN employment_gap_1*people_applying_employment_gap*0.9*housing_accessibility_factor_for_WA ELSE 0
        Units: person/year
        Limits: (None, None)
        Type: component
        Subs: None

        WA MOVING RATIO weights = 0,52 (of the employment gap)
    TOTAL = 1,02
    """
    return if_then_else(
        employment_gap_1() > 0,
        lambda: employment_gap_1()
        * people_applying_employment_gap()
        * 0.9
        * housing_accessibility_factor_for_wa(),
        lambda: 0,
    )


def elderly_move_rural():
    """
    Real Name: elderly_move_rural
    Original Eqn: maximum_elderly_population_moving* housing_accessibility_factor_for_elderly
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        maximum_elderly_population_moving() * housing_accessibility_factor_for_elderly()
    )


def housing_accessibility(x=None):
    """
    Real Name: housing_accessibility
    Original Eqn: total_population_in_relation_with_initial_population
    Units: dmnl
    Limits: (0.0, 5.0)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            total_population_in_relation_with_initial_population(),
            [0.700, 0.811, 0.922, 1.033, 1.144, 1.256, 1.367, 1.478, 1.589, 1.700],
            [5.000, 4.902, 4.763, 4.568, 4.294, 3.908, 3.364, 2.598, 1.519, 0.000],
        )
        if x is None
        else lookup(
            x,
            [0.700, 0.811, 0.922, 1.033, 1.144, 1.256, 1.367, 1.478, 1.589, 1.700],
            [5.000, 4.902, 4.763, 4.568, 4.294, 3.908, 3.364, 2.598, 1.519, 0.000],
        )
    )


def maximum_elderly_population_moving():
    """
    Real Name: maximum_elderly_population_moving
    Original Eqn: 1000
    Units: person/year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 1000


def housing_accessibility_factor_for_young():
    """
    Real Name: housing_accessibility_factor_for_young
    Original Eqn: housing_accessibility/5
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return housing_accessibility() / 5


def housing_accessibility_factor_for_wa():
    """
    Real Name: housing_accessibility_factor_for_WA
    Original Eqn: housing_accessibility/5
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return housing_accessibility() / 5


def housing_accessibility_factor_for_elderly():
    """
    Real Name: housing_accessibility_factor_for_elderly
    Original Eqn: housing_accessibility/5
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return housing_accessibility() / 5


def employment_gap_1():
    """
    Real Name: employment_gap_1
    Original Eqn: employment_gap
    Units: job
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return employment_gap()


def total_population_in_relation_with_initial_population():
    """
    Real Name: total_population_in_relation_with_initial_population
    Original Eqn: total_population_in_relation_to_initial_population
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return total_population_in_relation_to_initial_population()


def people_applying_employment_gap():
    """
    Real Name: people_applying_employment_gap
    Original Eqn: 1
    Units: person/year/job
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 1


def post_school_leaving_ratio():
    """
    Real Name: post_school_leaving_ratio
    Original Eqn: 1- (housing_factor_for_young+ employment_factor_for_young)
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return 1 - (housing_factor_for_young() + employment_factor_for_young())


def wa_leaving_ratio():
    """
    Real Name: WA_leaving_ratio
    Original Eqn: effect_of_employment_in_WA_leaving_ratio
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return effect_of_employment_in_wa_leaving_ratio()


def effect_of_employment_in_ps_leaving_ratio(x=None):
    """
    Real Name: effect_of_employment_in_PS_leaving_ratio
    Original Eqn: relative_employment_gap
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            relative_employment_gap(),
            [
                -0.500,
                -0.400,
                -0.300,
                -0.200,
                -0.100,
                0.000,
                0.100,
                0.200,
                0.300,
                0.400,
                0.500,
            ],
            [
                3.000,
                3.672,
                4.122,
                4.424,
                4.626,
                4.762,
                4.852,
                4.913,
                4.954,
                4.982,
                5.000,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                -0.500,
                -0.400,
                -0.300,
                -0.200,
                -0.100,
                0.000,
                0.100,
                0.200,
                0.300,
                0.400,
                0.500,
            ],
            [
                3.000,
                3.672,
                4.122,
                4.424,
                4.626,
                4.762,
                4.852,
                4.913,
                4.954,
                4.982,
                5.000,
            ],
        )
    )


def housing_factor_for_young():
    """
    Real Name: housing_factor_for_young
    Original Eqn: (housing_accessibility/5)*0.5
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (housing_accessibility() / 5) * 0.5


def employment_factor_for_young():
    """
    Real Name: employment_factor_for_young
    Original Eqn: (effect_of_employment_in_PS_leaving_ratio/5)*0.5
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (effect_of_employment_in_ps_leaving_ratio() / 5) * 0.5


def effect_of_employment_in_wa_leaving_ratio(x=None):
    """
    Real Name: effect_of_employment_in_WA_leaving_ratio
    Original Eqn: relative_employment_gap
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            relative_employment_gap(),
            [
                -0.500,
                -0.400,
                -0.300,
                -0.200,
                -0.100,
                0.000,
                0.100,
                0.200,
                0.300,
                0.400,
                0.500,
            ],
            [
                1.000,
                0.998,
                0.994,
                0.989,
                0.982,
                0.970,
                0.953,
                0.928,
                0.890,
                0.834,
                0.750,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                -0.500,
                -0.400,
                -0.300,
                -0.200,
                -0.100,
                0.000,
                0.100,
                0.200,
                0.300,
                0.400,
                0.500,
            ],
            [
                1.000,
                0.998,
                0.994,
                0.989,
                0.982,
                0.970,
                0.953,
                0.928,
                0.890,
                0.834,
                0.750,
            ],
        )
    )


def increasing_farms():
    """
    Real Name: increasing_farms
    Original Eqn: potential_new_farms*farming_attraction_factor
    Units: farm/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return potential_new_farms() * farming_attraction_factor()


def decreasing_farms():
    """
    Real Name: decreasing_farms
    Original Eqn: (farms*abandonment_ratio)+retirement_not_covered
    Units: farm/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (farms() * abandonment_ratio()) + retirement_not_covered()


def improving_income_per_farm():
    """
    Real Name: improving_income_per_farm
    Original Eqn: (decreasing_income_per_farm*agricultural_obsolescence_covered)
    Units: €/farm/Years
    Limits: (None, None)
    Type: component
    Subs: None

    diversification can increase up to a 10% income (/50)
    """
    return decreasing_income_per_farm() * agricultural_obsolescence_covered()


def decreasing_income_per_farm():
    """
    Real Name: decreasing_income_per_farm
    Original Eqn: average_local_income_per_farm/technical_obsolescence_time
    Units: €/farm/Years
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return average_local_income_per_farm() / technical_obsolescence_time()


_delayn_entering_vt = DelayN(
    lambda: vocational_training_campaign(),
    lambda: years_for_education_campaign(),
    lambda: vocational_training_campaign(),
    lambda: 1,
    time_step,
    "_delayn_entering_vt",
)


def entering_vt():
    """
    Real Name: entering_VT
    Original Eqn: aging_1* DELAY1(vocational_training_campaign, years_for_education_campaign)
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return aging_1() * _delayn_entering_vt()


_delayn_entering_university = DelayN(
    lambda: students_university_campaign(),
    lambda: years_for_education_campaign(),
    lambda: students_university_campaign(),
    lambda: 1,
    time_step,
    "_delayn_entering_university",
)


def entering_university():
    """
    Real Name: entering_university
    Original Eqn: aging_1* DELAY1(students_university_campaign, years_for_education_campaign)
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return aging_1() * _delayn_entering_university()


def early_working_entrance():
    """
    Real Name: early_working_entrance
    Original Eqn: aging_1-entering_VT-entering_university
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return aging_1() - entering_vt() - entering_university()


def becoming_vt_professional():
    """
    Real Name: becoming_vt_professional
    Original Eqn: VT_STUDENTS/time_to_become_VT_professional
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return vt_students() / time_to_become_vt_professional()


def becoming_graduated_professional():
    """
    Real Name: becoming_graduated_professional
    Original Eqn: UNIVERSITY_STUDENTS/time_to_become_graduated_professional
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return university_students() / time_to_become_graduated_professional()


def graduated_migration_net_flow():
    """
    Real Name: graduated_migration_net_flow
    Original Eqn: WA_migration_ratio*GRADUATED_PROFESSIONALS*graduate_migrating_ratio
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return wa_migration_ratio() * graduated_professionals() * graduate_migrating_ratio()


def nsw_retitiring():
    """
    Real Name: NSW_retitiring
    Original Eqn: UNSKILLED_WORKERS/working_lifetime_duration_for_NSW
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return unskilled_workers() / working_lifetime_duration_for_nsw()


def vtw_retiring():
    """
    Real Name: VTW_retiring
    Original Eqn: VT_PROFESSIONALS/working_lifetime_duration_for_VT
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return vt_professionals() / working_lifetime_duration_for_vt()


def gradw_retiring():
    """
    Real Name: GradW_retiring
    Original Eqn: GRADUATED_PROFESSIONALS/working_lifetime_duration_for_GP
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return graduated_professionals() / working_lifetime_duration_for_gp()


def vt_professionals_leaving():
    """
    Real Name: VT_professionals_leaving
    Original Eqn: WA_migration_ratio*VT_PROFESSIONALS*VT_migrating_ratio
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return wa_migration_ratio() * vt_professionals() * vt_migrating_ratio()


def apfx_not_specialized_workers_leaving():
    """
    Real Name: apfx_not_specialized_workers_leaving
    Original Eqn: WA_migration_ratio*unskilled_migrating_ratio*UNSKILLED_WORKERS
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return wa_migration_ratio() * unskilled_migrating_ratio() * unskilled_workers()


def births():
    """
    Real Name: births
    Original Eqn: total_rural_population*birth_rate
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return total_rural_population() * birth_rate()


def aging_1():
    """
    Real Name: aging_1
    Original Eqn: SCHOOL_AGE_POPULATION/school_age_duration
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return school_age_population() / school_age_duration()


def aging_3():
    """
    Real Name: aging_3
    Original Eqn: WORKING_AGE_POPULATION/working_age_duration
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return working_age_population() / working_age_duration()


def children_net_migration():
    """
    Real Name: children_net_migration
    Original Eqn: working_age_net_migration*0.5*fertility_rate*2/3*1/250
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return working_age_net_migration() * 0.5 * fertility_rate() * 2 / 3 * 1 / 250


def rural_children_deaths():
    """
    Real Name: rural_children_deaths
    Original Eqn: SCHOOL_AGE_POPULATION*children_death_rate
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return school_age_population() * children_death_rate()


def working_age_net_migration():
    """
    Real Name: working_age_net_migration
    Original Eqn: WA_moving- (WORKING_AGE_POPULATION*WA_leaving_ratio_1*max_WA_population_living_rural_per_year)
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return wa_moving() - (
        working_age_population()
        * wa_leaving_ratio_1()
        * max_wa_population_living_rural_per_year()
    )


def working_age_deaths():
    """
    Real Name: working_age_deaths
    Original Eqn: WORKING_AGE_POPULATION*working_age_death_rate
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return working_age_population() * working_age_death_rate()


def elderly_net_migration():
    """
    Real Name: elderly_net_migration
    Original Eqn: elderly_move_rural
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return elderly_move_rural()


_delayn_elderly_deaths = DelayN(
    lambda: adapted_life_expectancy(),
    lambda: 1,
    lambda: adapted_life_expectancy(),
    lambda: 1,
    time_step,
    "_delayn_elderly_deaths",
)


def elderly_deaths():
    """
    Real Name: elderly_deaths
    Original Eqn: ELDERLY_POPULATION/ DELAY1(adapted_life_expectancy, 1)
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return elderly_population() / _delayn_elderly_deaths()


def post_school_net_migration():
    """
    Real Name: post_school_net_migration
    Original Eqn: PS_moving- (POST_SCHOOL_POPULATION*max_post_school_leaving_per_year* post_school_leaving_ratio_1)
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return ps_moving() - (
        post_school_population()
        * max_post_school_leaving_per_year()
        * post_school_leaving_ratio_1()
    )


def rural_post_school_age_deaths():
    """
    Real Name: Rural_Post_school_age_deaths
    Original Eqn: POST_SCHOOL_POPULATION*post_school_death_rate
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return post_school_population() * post_school_death_rate()


def aging():
    """
    Real Name: aging
    Original Eqn: INFANTS/infant_duration
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return infants() / infant_duration()


def infant_net_migration():
    """
    Real Name: infant_net_migration
    Original Eqn: working_age_net_migration*0.5*fertility_rate/2
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return working_age_net_migration() * 0.5 * fertility_rate() / 2


def rural_infant_deaths():
    """
    Real Name: rural_infant_deaths
    Original Eqn: INFANTS*infant_death_rate
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return infants() * infant_death_rate()


def aging_2():
    """
    Real Name: aging_2
    Original Eqn: POST_SCHOOL_POPULATION/postschool_age_duration
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return post_school_population() / postschool_age_duration()


def newcomers_arrival():
    """
    Real Name: newcomers_arrival
    Original Eqn: MAX (0, infant_net_migration)+ MAX (0, children_net_migration)+ PS_moving+ WA_moving+ elderly_move_rural
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        max(0, infant_net_migration())
        + max(0, children_net_migration())
        + ps_moving()
        + wa_moving()
        + elderly_move_rural()
    )


def newcomers_integration():
    """
    Real Name: newcomers_integration
    Original Eqn: NEWCOMERS/integration_time
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return newcomers() / integration_time()


def working_age_rural_population():
    """
    Real Name: WORKING_AGE_RURAL_POPULATION
    Original Eqn: WORKING_AGE_POPULATION
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return working_age_population()


def farms():
    """
    Real Name: farms
    Original Eqn: increasing_farms - decreasing_farms
    Units: farm
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_farms()


_integ_farms = Integ(
    lambda: increasing_farms() - decreasing_farms(),
    lambda: initial_number_of_farms(),
    "_integ_farms",
)


def average_local_income_per_farm():
    """
    Real Name: average_local_income_per_farm
    Original Eqn: improving_income_per_farm - decreasing_income_per_farm
    Units: €/farm
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_average_local_income_per_farm()


_integ_average_local_income_per_farm = Integ(
    lambda: improving_income_per_farm() - decreasing_income_per_farm(),
    lambda: initial_mean_income_per_farm(),
    "_integ_average_local_income_per_farm",
)


def vt_students():
    """
    Real Name: VT_STUDENTS
    Original Eqn: entering_VT - becoming_vt_professional
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_vt_students()


_integ_vt_students = Integ(
    lambda: entering_vt() - becoming_vt_professional(),
    lambda: 20270,
    "_integ_vt_students",
)


def university_students():
    """
    Real Name: UNIVERSITY_STUDENTS
    Original Eqn: entering_university - becoming_graduated_professional
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_university_students()


_integ_university_students = Integ(
    lambda: entering_university() - becoming_graduated_professional(),
    lambda: 6601,
    "_integ_university_students",
)


def unskilled_workers():
    """
    Real Name: UNSKILLED_WORKERS
    Original Eqn: early_working_entrance - NSW_retitiring - apfx_not_specialized_workers_leaving
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_unskilled_workers()


_integ_unskilled_workers = Integ(
    lambda: early_working_entrance()
    - nsw_retitiring()
    - apfx_not_specialized_workers_leaving(),
    lambda: 25220 * 0.07 * 45,
    "_integ_unskilled_workers",
)


def vt_professionals():
    """
    Real Name: VT_PROFESSIONALS
    Original Eqn: becoming_vt_professional - VTW_retiring - VT_professionals_leaving
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_vt_professionals()


_integ_vt_professionals = Integ(
    lambda: becoming_vt_professional() - vtw_retiring() - vt_professionals_leaving(),
    lambda: 6756 * 42,
    "_integ_vt_professionals",
)


def graduated_professionals():
    """
    Real Name: GRADUATED_PROFESSIONALS
    Original Eqn: becoming_graduated_professional - graduated_migration_net_flow - GradW_retiring
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_graduated_professionals()


_integ_graduated_professionals = Integ(
    lambda: becoming_graduated_professional()
    - graduated_migration_net_flow()
    - gradw_retiring(),
    lambda: 1320 * 40,
    "_integ_graduated_professionals",
)


def school_age_population():
    """
    Real Name: SCHOOL_AGE_POPULATION
    Original Eqn: children_net_migration + aging - aging_1 - rural_children_deaths
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_school_age_population()


_integ_school_age_population = Integ(
    lambda: children_net_migration() + aging() - aging_1() - rural_children_deaths(),
    lambda: 252200,
    "_integ_school_age_population",
)


def working_age_population():
    """
    Real Name: WORKING_AGE_POPULATION
    Original Eqn: working_age_net_migration + aging_2 - aging_3 - working_age_deaths
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_working_age_population()


_integ_working_age_population = Integ(
    lambda: working_age_net_migration() + aging_2() - aging_3() - working_age_deaths(),
    lambda: 1513683,
    "_integ_working_age_population",
)


def elderly_population():
    """
    Real Name: ELDERLY_POPULATION
    Original Eqn: aging_3 + elderly_net_migration - elderly_deaths
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_elderly_population()


_integ_elderly_population = Integ(
    lambda: aging_3() + elderly_net_migration() - elderly_deaths(),
    lambda: 346434,
    "_integ_elderly_population",
)


def post_school_population():
    """
    Real Name: POST_SCHOOL_POPULATION
    Original Eqn: post_school_net_migration + aging_1 - aging_2 - Rural_Post_school_age_deaths
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_post_school_population()


_integ_post_school_population = Integ(
    lambda: post_school_net_migration()
    + aging_1()
    - aging_2()
    - rural_post_school_age_deaths(),
    lambda: 172904,
    "_integ_post_school_population",
)


def infants():
    """
    Real Name: INFANTS
    Original Eqn: births + infant_net_migration - aging - rural_infant_deaths
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_infants()


_integ_infants = Integ(
    lambda: births() + infant_net_migration() - aging() - rural_infant_deaths(),
    lambda: 169827,
    "_integ_infants",
)


def newcomers():
    """
    Real Name: NEWCOMERS
    Original Eqn: newcomers_arrival - newcomers_integration
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_newcomers()


_integ_newcomers = Integ(
    lambda: newcomers_arrival() - newcomers_integration(),
    lambda: 200000,
    "_integ_newcomers",
)
