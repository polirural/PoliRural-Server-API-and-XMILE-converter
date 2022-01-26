"""
Python model 'central_greece_v2_p.py'
Translated using PySD
"""

import numpy as np

from pysd.py_backend.functions import if_then_else, ramp, step, lookup, previous
from pysd.py_backend.statefuls import Integ, DelayN, Initial, Smooth

__pysd_version__ = "2.0.0-dev"

__data = {"scope": None, "time": lambda: 0}

_subscript_dict = {}

_namespace = {
    "TIME": "time",
    "Time": "time",
    "time": "time",
    "mean_working_period_for_farmers": "mean_working_period_for_farmers",
    "abandonment_ratio": "abandonment_ratio",
    "Jobs_per_farm": "jobs_per_farm",
    "diversification/_multifunctionality": "diversification_multifunctionality",
    "farmer_retirement": "farmer_retirement",
    "generational_transition_ratio": "generational_transition_ratio",
    "retirement_substitution": "retirement_substitution",
    "retirement_not_covered": "retirement_not_covered",
    "land_access": "land_access",
    "new_forms_of_property": "new_forms_of_property",
    "max_agricultural_land": "max_agricultural_land",
    "potential_land_transformation": "potential_land_transformation",
    "potential_new_farms": "potential_new_farms",
    "CAP_Eco-Schemes": "cap_ecoschemes",
    "farming_attraction_factor": "farming_attraction_factor",
    "social_innovation_/_potential_initiatives": "social_innovation__potential_initiatives",
    "average_farm_area": "average_farm_area",
    "agricultural_land": "agricultural_land",
    "agriculture_profitability": "agriculture_profitability",
    "CAP_direct_payment": "cap_direct_payment",
    "agriculture_jobs": "agriculture_jobs",
    "effect_of_tourism_on_diversification": "effect_of_tourism_on_diversification",
    "AKIS_effect": "akis_effect",
    "CAP_reform_direct_payments_decrease_2021": "cap_reform_direct_payments_decrease_2021",
    "CAP_mean_proportion_of_direct_payment_to_FNVA": "cap_mean_proportion_of_direct_payment_to_fnva",
    "Eco-schemes_effect_on_direct_payment": "ecoschemes_effect_on_direct_payment",
    "initial_mean_income_per_farm": "initial_mean_income_per_farm",
    "technical_obsolescence_time": "technical_obsolescence_time",
    "agricultural_obsolescence_covered": "agricultural_obsolescence_covered",
    "mean_jobs_per_farm": "mean_jobs_per_farm",
    "max_improvement_per_diversification": "max_improvement_per_diversification",
    "initial_number_of_farms": "initial_number_of_farms",
    "final_technical_obsolescence_time": "final_technical_obsolescence_time",
    "time_for_slope": "time_for_slope",
    "normal_technical_obsolescence_time": "normal_technical_obsolescence_time",
    "AKIS_evolution": "akis_evolution",
    "other_national_funding": "other_national_funding",
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
    "unskilled_ratio": "unskilled_ratio",
    "total_regional_employment": "total_regional_employment",
    "workforce_as_ratio_of_WAP": "workforce_as_ratio_of_wap",
    "employment_gap": "employment_gap",
    "relative_employment_gap": "relative_employment_gap",
    "primary_jobs_viability_ratio": "primary_jobs_viability_ratio",
    "new_industrial_job_viability_ratio": "new_industrial_job_viability_ratio",
    "total_employment": "total_employment",
    "Previous_population": "previous_population",
    "Difference_of_population": "difference_of_population",
    "ratio_population_services": "ratio_population_services",
    "endogenous_primary_job_creation_ratio": "endogenous_primary_job_creation_ratio",
    "endogenous_industrial_job_creation_ratio": "endogenous_industrial_job_creation_ratio",
    "endogenous_service_jobs_creation_ratio": "endogenous_service_jobs_creation_ratio",
    "total_services_job": "total_services_job",
    "new_services_viability_ratio": "new_services_viability_ratio",
    "resulting_average_life_for_industrial_business": "resulting_average_life_for_industrial_business",
    "resulting_average_life_for_services": "resulting_average_life_for_services",
    "average_life_of_a_primary_sector_business": "average_life_of_a_primary_sector_business",
    "Drop_in_the_service_average_life_due_to_COVID": "drop_in_the_service_average_life_due_to_covid",
    "jobs_per_tourism": "jobs_per_tourism",
    "visitors_per_tourism_workplace": "visitors_per_tourism_workplace",
    "primary_ratio": "primary_ratio",
    "industrial_ratio": "industrial_ratio",
    "average_life_of_a_service_business": "average_life_of_a_service_business",
    "average_life_of_an_industrial_business": "average_life_of_an_industrial_business",
    "drop_in_the_industrial_average_life_due_to_COVID": "drop_in_the_industrial_average_life_due_to_covid",
    "services_ratio": "services_ratio",
    "total_workforce": "total_workforce",
    "total_industrial_jobs": "total_industrial_jobs",
    "natural_land_variation": "natural_land_variation",
    "potential_visitors_as_a_function_of_Natural_Capital": "potential_visitors_as_a_function_of_natural_capital",
    "ratio_effect_of_agriculture_on_Natural_Capital": "ratio_effect_of_agriculture_on_natural_capital",
    "natural_land_objective": "natural_land_objective",
    "tourist_visitors": "tourist_visitors",
    "attraction_ratio_for_tourists": "attraction_ratio_for_tourists",
    "effect_of_tourism_on_natural_capital": "effect_of_tourism_on_natural_capital",
    "relative_natural_capital": "relative_natural_capital",
    "natural_capital_perception": "natural_capital_perception",
    "years_for_completing_natural_land_objective": "years_for_completing_natural_land_objective",
    "previous_agricultural_land": "previous_agricultural_land",
    "difference_of_agricultural_land": "difference_of_agricultural_land",
    "effect_of_agriculture_on_Natural_Capital": "effect_of_agriculture_on_natural_capital",
    "normal_attraction_ratio": "normal_attraction_ratio",
    "attraction_ratio_objective": "attraction_ratio_objective",
    "time_to_complete_campaign": "time_to_complete_campaign",
    "tourist_campaign": "tourist_campaign",
    "initial_natural_land": "initial_natural_land",
    "initial_Natural_capital": "initial_natural_capital",
    "relative_tourist_visits": "relative_tourist_visits",
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
    "elderly_leaving_ratio_1": "elderly_leaving_ratio_1",
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
    "health_centers_accessibility": "health_centers_accessibility",
    "VT_centers_accessibility": "vt_centers_accessibility",
    "University_Accessibility": "university_accessibility",
    "community_activity_and_networks": "community_activity_and_networks",
    "social_capital": "social_capital",
    "social_innovation": "social_innovation",
    "city_and_regional_connections_access": "city_and_regional_connections_access",
    "cultural_appeal": "cultural_appeal",
    "institutional_support": "institutional_support",
    "infrastructures_depletion_time": "infrastructures_depletion_time",
    "potential_initiatives_active_time": "potential_initiatives_active_time",
    "population_covered_objective": "population_covered_objective",
    "broadband_infrastructures_depletion_time": "broadband_infrastructures_depletion_time",
    "endogenous_primary_job_creation": "endogenous_primary_job_creation",
    "endogenous_industrial_job_creation": "endogenous_industrial_job_creation",
    "endogenous_service_job_creation": "endogenous_service_job_creation",
    "time_to_implement_initiatives": "time_to_implement_initiatives",
    "infrastructures_objective": "infrastructures_objective",
    "community_and_public_services_accessibility": "community_and_public_services_accessibility",
    "time_to_build_effective_shared_knowledge": "time_to_build_effective_shared_knowledge",
    "effect_of_social_innovation_in_creating_initiatives_ratio": "effect_of_social_innovation_in_creating_initiatives_ratio",
    "effect_of_broadband_in_creating_potential_initiatives": "effect_of_broadband_in_creating_potential_initiatives",
    "year_initiating_infrastructures_plan": "year_initiating_infrastructures_plan",
    "year_initiating_broadband_plan": "year_initiating_broadband_plan",
    "shared_knowledge_loss_time": "shared_knowledge_loss_time",
    "community_climate": "community_climate",
    "max_km_year_infrastructures": "max_km_year_infrastructures",
    "broadband_gap": "broadband_gap",
    "average_jobs_per_service_initiative": "average_jobs_per_service_initiative",
    "average_jobs_per_primary_initiative": "average_jobs_per_primary_initiative",
    "average_jobs_per_industrial_initiative": "average_jobs_per_industrial_initiative",
    "broadband_effect_on_retention": "broadband_effect_on_retention",
    "social_capital_effect_on_retention": "social_capital_effect_on_retention",
    "effect_of_c&r_connections_on_retention": "effect_of_cr_connections_on_retention",
    "infrastructures_gap": "infrastructures_gap",
    "initial_mobility_infrastructures": "initial_mobility_infrastructures",
    "initial_population_covered": "initial_population_covered",
    "infrastructure_campaign": "infrastructure_campaign",
    "time_for_infrastructure_campaign_extension": "time_for_infrastructure_campaign_extension",
    "broadband_campaign": "broadband_campaign",
    "time_to_complete_broadband_campaign": "time_to_complete_broadband_campaign",
    "inst_support_evolution": "inst_support_evolution",
    "WA_moving": "wa_moving",
    "elderly_move_rural": "elderly_move_rural",
    "housing_accessibility": "housing_accessibility",
    "maximum_elderly_population_moving": "maximum_elderly_population_moving",
    "natural_capital_weight_for_young": "natural_capital_weight_for_young",
    "cultural_appeal_weight_for_WA": "cultural_appeal_weight_for_wa",
    "natural_capital_weight_for_WA": "natural_capital_weight_for_wa",
    "housing_accessibility_weight_for_WA": "housing_accessibility_weight_for_wa",
    "medical_and_care_services_weight": "medical_and_care_services_weight",
    "cultural_appeal_weight_for_elderly": "cultural_appeal_weight_for_elderly",
    "natural_capital_weight_for_elderly": "natural_capital_weight_for_elderly",
    "housing_accessibility_weight_for_elderly": "housing_accessibility_weight_for_elderly",
    "housing_accessibility_factor_for_young": "housing_accessibility_factor_for_young",
    "natural_capital_factor_for_young": "natural_capital_factor_for_young",
    "housing_accessibility_factor_for_WA": "housing_accessibility_factor_for_wa",
    "housing_accessibility_factor_for_elderly": "housing_accessibility_factor_for_elderly",
    "medical_and_care_services_factor": "medical_and_care_services_factor",
    "natural_capital_factor_for_WA": "natural_capital_factor_for_wa",
    "cultural_appeal_factor_for_WA": "cultural_appeal_factor_for_wa",
    "cultural_appeal_factor_for_elderly": "cultural_appeal_factor_for_elderly",
    "natural_capital_factor_for_elderly": "natural_capital_factor_for_elderly",
    "employment_gap_1": "employment_gap_1",
    "total_population_in_relation_with_initial_population": "total_population_in_relation_with_initial_population",
    "public_services_factor_for_WA_attraction": "public_services_factor_for_wa_attraction",
    "public_services_weight_in_WA_attraction": "public_services_weight_in_wa_attraction",
    "PS_moving": "ps_moving",
    "young_applying_employment_gap": "young_applying_employment_gap",
    "WA_applying_employment_gap": "wa_applying_employment_gap",
    "post_school_leaving_ratio": "post_school_leaving_ratio",
    "WA_leaving_ratio": "wa_leaving_ratio",
    "elderly_leaving_ratio": "elderly_leaving_ratio",
    "maximum_ratio_elderly_population_leaving": "maximum_ratio_elderly_population_leaving",
    "higher_education_weight": "higher_education_weight",
    "broadband_weight_for_young": "broadband_weight_for_young",
    "housing_accessibility_weight_for_young": "housing_accessibility_weight_for_young",
    "social_capital_weight_for_young": "social_capital_weight_for_young",
    "broadband_weight_for_WA": "broadband_weight_for_wa",
    "c&r_connections_weight": "cr_connections_weight",
    "social_capital_weight_for_WA": "social_capital_weight_for_wa",
    "medical_and_care_weight": "medical_and_care_weight",
    "social_capital_weight_for_elderly": "social_capital_weight_for_elderly",
    "employment_weight_for_young": "employment_weight_for_young",
    "effect_of_employment_in_PS_retention_ratio": "effect_of_employment_in_ps_retention_ratio",
    "higher_education_factor": "higher_education_factor",
    "broadband_factor_for_young": "broadband_factor_for_young",
    "housing_factor_for_young": "housing_factor_for_young",
    "social_capital_factor_for_young": "social_capital_factor_for_young",
    "employment_factor_for_young": "employment_factor_for_young",
    "broadband_factor_for_WA": "broadband_factor_for_wa",
    "social_capital_factor_for_WA": "social_capital_factor_for_wa",
    "c&r_factor": "cr_factor",
    "social_capital_factor_for_elderly": "social_capital_factor_for_elderly",
    "medical_and_care_factor": "medical_and_care_factor",
    "retention_factor": "retention_factor",
    "effect_of_employment_in_WA_leaving_ratio": "effect_of_employment_in_wa_leaving_ratio",
    "public_services_weight_for_WA_retention": "public_services_weight_for_wa_retention",
    "public_services_retention": "public_services_retention",
    "farms": "farms",
    "mean_local_income_per_farm": "mean_local_income_per_farm",
    "VT_STUDENTS": "vt_students",
    "UNIVERSITY_STUDENTS": "university_students",
    "UNSKILLED_WORKERS": "unskilled_workers",
    "VT_PROFESSIONALS": "vt_professionals",
    "GRADUATED_PROFESSIONALS": "graduated_professionals",
    "Rest_of_primary_sector_jobs": "rest_of_primary_sector_jobs",
    "Industrial_jobs": "industrial_jobs",
    "service_jobs": "service_jobs",
    "population_services": "population_services",
    "Natural_Capital": "natural_capital",
    "SCHOOL_AGE_POPULATION": "school_age_population",
    "WORKING_AGE_POPULATION": "working_age_population",
    "ELDERLY_POPULATION": "elderly_population",
    "POST_SCHOOL_POPULATION": "post_school_population",
    "INFANTS": "infants",
    "NEWCOMERS": "newcomers",
    "mobility_infrastructures": "mobility_infrastructures",
    "broadband_infrastructure_population_covered": "broadband_infrastructure_population_covered",
    "potential_initiatives": "potential_initiatives",
    "implemented_initiatives": "implemented_initiatives",
    "shared_knowledge": "shared_knowledge",
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
    "creation_of_primary_jobs": "creation_of_primary_jobs",
    "destruction_of_primary_jobs": "destruction_of_primary_jobs",
    "creation_of_industrial_jobs": "creation_of_industrial_jobs",
    "destruction_of_industrial_jobs": "destruction_of_industrial_jobs",
    "creation_of_services_jobs": "creation_of_services_jobs",
    "destruction_of_services_jobs": "destruction_of_services_jobs",
    "change_in_population_services": "change_in_population_services",
    "natural_capital_net_variation": "natural_capital_net_variation",
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
    "building_mobility_infrastructures": "building_mobility_infrastructures",
    "mobility_infrastructures_depletion": "mobility_infrastructures_depletion",
    "building_infrastructure": "building_infrastructure",
    "broadband_infrastructure_depletion": "broadband_infrastructure_depletion",
    "creating_potential_initiatives": "creating_potential_initiatives",
    "planning_initiatives": "planning_initiatives",
    "dismissing_potential_initiatives": "dismissing_potential_initiatives",
    "becoming_stablished_jobs": "becoming_stablished_jobs",
    "building_shared_knowledge": "building_shared_knowledge",
    "shared_knowledge_loss": "shared_knowledge_loss",
    "WORKING_AGE_RURAL_POPULATION": "working_age_rural_population",
}

_dependencies = {
    "mean_working_period_for_farmers": {},
    "abandonment_ratio": {"agriculture_profitability": 1},
    "jobs_per_farm": {"mean_jobs_per_farm": 1, "diversification_multifunctionality": 1},
    "diversification_multifunctionality": {
        "effect_of_tourism_on_diversification": 1,
        "cap_ecoschemes": 1,
    },
    "farmer_retirement": {"farms": 1, "mean_working_period_for_farmers": 1},
    "generational_transition_ratio": {"social_capital": 1},
    "retirement_substitution": {
        "farmer_retirement": 1,
        "generational_transition_ratio": 1,
    },
    "retirement_not_covered": {"farmer_retirement": 1, "retirement_substitution": 1},
    "land_access": {"new_forms_of_property": 1},
    "new_forms_of_property": {
        "social_innovation__potential_initiatives": 1,
        "akis_effect": 1,
    },
    "max_agricultural_land": {},
    "potential_land_transformation": {
        "max_agricultural_land": 1,
        "agricultural_land": 1,
    },
    "potential_new_farms": {"potential_land_transformation": 1, "average_farm_area": 1},
    "cap_ecoschemes": {"time": 1},
    "farming_attraction_factor": {"land_access": 1, "agriculture_profitability": 1},
    "social_innovation__potential_initiatives": {"social_innovation": 1},
    "average_farm_area": {"akis_evolution": 1},
    "agricultural_land": {"farms": 1, "average_farm_area": 1},
    "agriculture_profitability": {
        "mean_local_income_per_farm": 1,
        "cap_direct_payment": 1,
        "other_national_funding": 1,
    },
    "cap_direct_payment": {
        "cap_mean_proportion_of_direct_payment_to_fnva": 1,
        "cap_reform_direct_payments_decrease_2021": 1,
        "time": 2,
        "ecoschemes_effect_on_direct_payment": 1,
    },
    "agriculture_jobs": {"farms": 1, "jobs_per_farm": 1},
    "effect_of_tourism_on_diversification": {
        "tourist_visitors": 1,
        "total_rural_population": 1,
    },
    "akis_effect": {"akis_evolution": 1},
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
    "agricultural_obsolescence_covered": {"akis_effect": 1},
    "mean_jobs_per_farm": {"average_farm_area": 1},
    "max_improvement_per_diversification": {},
    "initial_number_of_farms": {},
    "final_technical_obsolescence_time": {},
    "time_for_slope": {},
    "normal_technical_obsolescence_time": {"average_farm_area": 1},
    "akis_evolution": {"time": 1},
    "other_national_funding": {"time": 1},
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
    "unskilled_ratio": {"unskilled_workers": 1, "total_workforce": 1},
    "total_regional_employment": {
        "agriculture_jobs": 1,
        "total_industrial_jobs": 1,
        "total_services_job": 1,
        "rest_of_primary_sector_jobs": 1,
    },
    "workforce_as_ratio_of_wap": {},
    "employment_gap": {"total_employment": 1, "total_workforce": 1},
    "relative_employment_gap": {"employment_gap": 1, "total_workforce": 1},
    "primary_jobs_viability_ratio": {},
    "new_industrial_job_viability_ratio": {},
    "total_employment": {"total_regional_employment": 1},
    "previous_population": {"total_rural_population": 1, "time": 1},
    "difference_of_population": {"total_rural_population": 1, "previous_population": 1},
    "ratio_population_services": {},
    "endogenous_primary_job_creation_ratio": {"endogenous_primary_job_creation": 1},
    "endogenous_industrial_job_creation_ratio": {
        "endogenous_industrial_job_creation": 1
    },
    "endogenous_service_jobs_creation_ratio": {"endogenous_service_job_creation": 1},
    "total_services_job": {
        "population_services": 1,
        "service_jobs": 1,
        "jobs_per_tourism": 1,
    },
    "new_services_viability_ratio": {},
    "resulting_average_life_for_industrial_business": {
        "average_life_of_an_industrial_business": 1,
        "drop_in_the_industrial_average_life_due_to_covid": 1,
        "time": 1,
    },
    "resulting_average_life_for_services": {
        "average_life_of_a_service_business": 1,
        "drop_in_the_service_average_life_due_to_covid": 1,
        "time": 1,
    },
    "average_life_of_a_primary_sector_business": {},
    "drop_in_the_service_average_life_due_to_covid": {"time": 1},
    "jobs_per_tourism": {"tourist_visitors": 1, "visitors_per_tourism_workplace": 1},
    "visitors_per_tourism_workplace": {},
    "primary_ratio": {
        "agriculture_jobs": 1,
        "rest_of_primary_sector_jobs": 1,
        "total_employment": 1,
    },
    "industrial_ratio": {"total_industrial_jobs": 1, "total_employment": 1},
    "average_life_of_a_service_business": {},
    "average_life_of_an_industrial_business": {},
    "drop_in_the_industrial_average_life_due_to_covid": {"time": 1},
    "services_ratio": {"total_services_job": 1, "total_employment": 1},
    "total_workforce": {
        "workforce_as_ratio_of_wap": 1,
        "working_age_rural_population": 1,
    },
    "total_industrial_jobs": {"industrial_jobs": 1},
    "natural_land_variation": {
        "natural_land_objective": 1,
        "initial_natural_land": 1,
        "years_for_completing_natural_land_objective": 1,
        "time": 1,
    },
    "potential_visitors_as_a_function_of_natural_capital": {"natural_capital": 1},
    "ratio_effect_of_agriculture_on_natural_capital": {
        "diversification_multifunctionality": 1
    },
    "natural_land_objective": {},
    "_delayn_tourist_visitors": {
        "initial": {
            "attraction_ratio_for_tourists": 1,
            "city_and_regional_connections_access": 1,
            "potential_visitors_as_a_function_of_natural_capital": 1,
        },
        "step": {
            "attraction_ratio_for_tourists": 1,
            "city_and_regional_connections_access": 1,
            "potential_visitors_as_a_function_of_natural_capital": 1,
        },
    },
    "tourist_visitors": {"_delayn_tourist_visitors": 1},
    "_delayn_attraction_ratio_for_tourists": {
        "initial": {"tourist_campaign": 1, "time_to_complete_campaign": 1},
        "step": {"tourist_campaign": 1, "time_to_complete_campaign": 1},
    },
    "attraction_ratio_for_tourists": {"_delayn_attraction_ratio_for_tourists": 1},
    "effect_of_tourism_on_natural_capital": {"relative_tourist_visits": 1},
    "relative_natural_capital": {"natural_capital": 1, "initial_natural_capital": 1},
    "natural_capital_perception": {"relative_natural_capital": 1},
    "years_for_completing_natural_land_objective": {},
    "previous_agricultural_land": {
        "agricultural_land": 1,
        "initial_number_of_farms": 1,
        "average_farm_area": 1,
        "time": 1,
    },
    "difference_of_agricultural_land": {
        "agricultural_land": 1,
        "previous_agricultural_land": 1,
    },
    "effect_of_agriculture_on_natural_capital": {
        "difference_of_agricultural_land": 3,
        "ratio_effect_of_agriculture_on_natural_capital": 3,
    },
    "normal_attraction_ratio": {"time": 1},
    "attraction_ratio_objective": {},
    "time_to_complete_campaign": {},
    "tourist_campaign": {
        "normal_attraction_ratio": 2,
        "attraction_ratio_objective": 1,
        "time": 1,
    },
    "initial_natural_land": {},
    "_initial_initial_natural_capital": {"initial": {"natural_capital": 1}, "step": {}},
    "initial_natural_capital": {"_initial_initial_natural_capital": 1},
    "relative_tourist_visits": {"tourist_visitors": 1, "total_rural_population": 1},
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
    "birth_rate": {"time": 1},
    "infant_duration": {},
    "infant_death_rate": {},
    "postschool_age_duration": {},
    "post_school_leaving_ratio_1": {"post_school_leaving_ratio": 1},
    "wa_leaving_ratio_1": {"wa_leaving_ratio": 1},
    "elderly_leaving_ratio_1": {"elderly_leaving_ratio": 1},
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
    "health_centers_accessibility": {"mobility_infrastructures": 1},
    "vt_centers_accessibility": {"mobility_infrastructures": 1},
    "university_accessibility": {"mobility_infrastructures": 1},
    "community_activity_and_networks": {
        "community_and_public_services_accessibility": 1,
        "community_climate": 1,
    },
    "social_capital": {"shared_knowledge": 1},
    "social_innovation": {"social_capital": 1, "workforce_specialization": 1},
    "city_and_regional_connections_access": {"mobility_infrastructures": 1},
    "cultural_appeal": {"shared_knowledge": 1},
    "institutional_support": {"inst_support_evolution": 1},
    "infrastructures_depletion_time": {},
    "potential_initiatives_active_time": {},
    "population_covered_objective": {},
    "broadband_infrastructures_depletion_time": {},
    "endogenous_primary_job_creation": {
        "becoming_stablished_jobs": 1,
        "average_jobs_per_primary_initiative": 1,
    },
    "endogenous_industrial_job_creation": {
        "becoming_stablished_jobs": 1,
        "average_jobs_per_industrial_initiative": 1,
    },
    "endogenous_service_job_creation": {
        "becoming_stablished_jobs": 1,
        "average_jobs_per_service_initiative": 1,
    },
    "time_to_implement_initiatives": {},
    "infrastructures_objective": {},
    "community_and_public_services_accessibility": {"mobility_infrastructures": 1},
    "time_to_build_effective_shared_knowledge": {"proportion_of_newcomers": 1},
    "effect_of_social_innovation_in_creating_initiatives_ratio": {
        "social_innovation": 1
    },
    "effect_of_broadband_in_creating_potential_initiatives": {
        "broadband_infrastructure_population_covered": 1
    },
    "year_initiating_infrastructures_plan": {},
    "year_initiating_broadband_plan": {},
    "shared_knowledge_loss_time": {},
    "community_climate": {"time": 1},
    "max_km_year_infrastructures": {},
    "broadband_gap": {
        "population_covered_objective": 1,
        "broadband_infrastructure_population_covered": 1,
    },
    "average_jobs_per_service_initiative": {},
    "average_jobs_per_primary_initiative": {},
    "average_jobs_per_industrial_initiative": {},
    "broadband_effect_on_retention": {"broadband_infrastructure_population_covered": 1},
    "social_capital_effect_on_retention": {"social_capital": 1},
    "effect_of_cr_connections_on_retention": {
        "city_and_regional_connections_access": 1
    },
    "infrastructures_gap": {
        "infrastructures_objective": 1,
        "initial_mobility_infrastructures": 1,
    },
    "initial_mobility_infrastructures": {},
    "initial_population_covered": {},
    "infrastructure_campaign": {
        "infrastructures_gap": 1,
        "time_for_infrastructure_campaign_extension": 1,
    },
    "time_for_infrastructure_campaign_extension": {},
    "broadband_campaign": {
        "broadband_gap": 1,
        "time_to_complete_broadband_campaign": 1,
    },
    "time_to_complete_broadband_campaign": {},
    "inst_support_evolution": {"time": 1},
    "wa_moving": {
        "employment_gap_1": 2,
        "wa_applying_employment_gap": 1,
        "housing_accessibility_factor_for_wa": 1,
        "natural_capital_factor_for_wa": 1,
        "cultural_appeal_factor_for_wa": 1,
        "public_services_factor_for_wa_attraction": 1,
    },
    "elderly_move_rural": {
        "maximum_elderly_population_moving": 1,
        "natural_capital_factor_for_elderly": 1,
        "cultural_appeal_factor_for_elderly": 1,
        "housing_accessibility_factor_for_elderly": 1,
        "medical_and_care_services_factor": 1,
    },
    "housing_accessibility": {
        "total_population_in_relation_with_initial_population": 1
    },
    "maximum_elderly_population_moving": {},
    "natural_capital_weight_for_young": {},
    "cultural_appeal_weight_for_wa": {},
    "natural_capital_weight_for_wa": {},
    "housing_accessibility_weight_for_wa": {},
    "medical_and_care_services_weight": {},
    "cultural_appeal_weight_for_elderly": {},
    "natural_capital_weight_for_elderly": {},
    "housing_accessibility_weight_for_elderly": {},
    "housing_accessibility_factor_for_young": {
        "housing_accessibility_weight_for_young": 1,
        "housing_accessibility": 1,
    },
    "natural_capital_factor_for_young": {
        "natural_capital_weight_for_young": 1,
        "natural_capital_perception": 1,
    },
    "housing_accessibility_factor_for_wa": {
        "housing_accessibility_weight_for_wa": 1,
        "housing_accessibility": 1,
    },
    "housing_accessibility_factor_for_elderly": {
        "housing_accessibility_weight_for_elderly": 1,
        "housing_accessibility": 1,
    },
    "medical_and_care_services_factor": {
        "health_centers_accessibility": 1,
        "medical_and_care_services_weight": 1,
    },
    "natural_capital_factor_for_wa": {
        "natural_capital_weight_for_wa": 1,
        "natural_capital_perception": 1,
    },
    "cultural_appeal_factor_for_wa": {
        "cultural_appeal_weight_for_wa": 1,
        "cultural_appeal": 1,
    },
    "cultural_appeal_factor_for_elderly": {
        "cultural_appeal_weight_for_elderly": 1,
        "cultural_appeal": 1,
    },
    "natural_capital_factor_for_elderly": {
        "natural_capital_perception": 1,
        "natural_capital_weight_for_elderly": 1,
    },
    "employment_gap_1": {"employment_gap": 1},
    "total_population_in_relation_with_initial_population": {
        "total_population_in_relation_to_initial_population": 1
    },
    "public_services_factor_for_wa_attraction": {
        "community_and_public_services_accessibility": 1,
        "public_services_weight_in_wa_attraction": 1,
    },
    "public_services_weight_in_wa_attraction": {},
    "ps_moving": {
        "employment_gap_1": 2,
        "young_applying_employment_gap": 1,
        "housing_accessibility_factor_for_young": 1,
        "natural_capital_factor_for_young": 1,
        "social_capital_factor_for_young": 1,
    },
    "young_applying_employment_gap": {},
    "wa_applying_employment_gap": {},
    "post_school_leaving_ratio": {
        "higher_education_factor": 1,
        "broadband_factor_for_young": 1,
        "social_capital_factor_for_young": 1,
        "housing_factor_for_young": 1,
        "employment_factor_for_young": 1,
    },
    "wa_leaving_ratio": {
        "retention_factor": 1,
        "effect_of_employment_in_wa_leaving_ratio": 1,
    },
    "elderly_leaving_ratio": {
        "maximum_ratio_elderly_population_leaving": 1,
        "medical_and_care_factor": 1,
        "social_capital_factor_for_elderly": 1,
    },
    "maximum_ratio_elderly_population_leaving": {},
    "higher_education_weight": {},
    "broadband_weight_for_young": {},
    "housing_accessibility_weight_for_young": {},
    "social_capital_weight_for_young": {},
    "broadband_weight_for_wa": {},
    "cr_connections_weight": {},
    "social_capital_weight_for_wa": {},
    "medical_and_care_weight": {},
    "social_capital_weight_for_elderly": {},
    "employment_weight_for_young": {},
    "effect_of_employment_in_ps_retention_ratio": {"relative_employment_gap": 1},
    "higher_education_factor": {
        "vt_centers_accessibility": 1,
        "university_accessibility": 1,
        "higher_education_weight": 1,
    },
    "broadband_factor_for_young": {
        "broadband_weight_for_young": 1,
        "broadband_effect_on_retention": 1,
    },
    "housing_factor_for_young": {
        "housing_accessibility_weight_for_young": 1,
        "housing_accessibility": 1,
    },
    "social_capital_factor_for_young": {
        "social_capital_weight_for_young": 1,
        "social_capital_effect_on_retention": 1,
    },
    "employment_factor_for_young": {
        "employment_weight_for_young": 1,
        "effect_of_employment_in_ps_retention_ratio": 1,
    },
    "broadband_factor_for_wa": {
        "broadband_weight_for_wa": 1,
        "broadband_effect_on_retention": 1,
    },
    "social_capital_factor_for_wa": {
        "social_capital_weight_for_wa": 1,
        "social_capital_effect_on_retention": 1,
    },
    "cr_factor": {
        "city_and_regional_connections_access": 1,
        "cr_connections_weight": 1,
    },
    "social_capital_factor_for_elderly": {
        "social_capital_weight_for_elderly": 1,
        "social_capital_effect_on_retention": 1,
    },
    "medical_and_care_factor": {
        "medical_and_care_weight": 1,
        "health_centers_accessibility": 1,
    },
    "retention_factor": {
        "social_capital_factor_for_wa": 1,
        "broadband_factor_for_wa": 1,
        "cr_factor": 1,
        "public_services_retention": 1,
    },
    "effect_of_employment_in_wa_leaving_ratio": {"relative_employment_gap": 1},
    "public_services_weight_for_wa_retention": {},
    "public_services_retention": {
        "public_services_weight_for_wa_retention": 1,
        "community_and_public_services_accessibility": 1,
    },
    "increasing_farms": {"potential_new_farms": 1, "farming_attraction_factor": 1},
    "decreasing_farms": {
        "farms": 1,
        "abandonment_ratio": 1,
        "retirement_not_covered": 1,
    },
    "improving_income_per_farm": {
        "decreasing_income_per_farm": 1,
        "agricultural_obsolescence_covered": 1,
        "diversification_multifunctionality": 1,
        "mean_local_income_per_farm": 1,
        "max_improvement_per_diversification": 1,
    },
    "decreasing_income_per_farm": {
        "mean_local_income_per_farm": 1,
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
    "creation_of_primary_jobs": {"endogenous_primary_job_creation_ratio": 1},
    "destruction_of_primary_jobs": {
        "endogenous_primary_job_creation_ratio": 1,
        "primary_jobs_viability_ratio": 1,
        "rest_of_primary_sector_jobs": 1,
        "average_life_of_a_primary_sector_business": 1,
    },
    "creation_of_industrial_jobs": {"endogenous_industrial_job_creation_ratio": 1},
    "destruction_of_industrial_jobs": {
        "industrial_jobs": 1,
        "resulting_average_life_for_industrial_business": 1,
        "endogenous_industrial_job_creation_ratio": 1,
        "new_industrial_job_viability_ratio": 1,
    },
    "creation_of_services_jobs": {"endogenous_service_jobs_creation_ratio": 1},
    "destruction_of_services_jobs": {
        "service_jobs": 1,
        "resulting_average_life_for_services": 1,
        "endogenous_service_jobs_creation_ratio": 1,
        "new_services_viability_ratio": 1,
        "time": 1,
    },
    "change_in_population_services": {
        "difference_of_population": 1,
        "ratio_population_services": 1,
    },
    "_delayn_natural_capital_net_variation": {
        "initial": {
            "natural_land_variation": 1,
            "years_for_completing_natural_land_objective": 1,
        },
        "step": {
            "natural_land_variation": 1,
            "years_for_completing_natural_land_objective": 1,
        },
    },
    "natural_capital_net_variation": {
        "_delayn_natural_capital_net_variation": 1,
        "natural_capital": 1,
        "effect_of_tourism_on_natural_capital": 1,
        "effect_of_agriculture_on_natural_capital": 1,
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
    "elderly_net_migration": {
        "elderly_move_rural": 1,
        "elderly_population": 1,
        "elderly_leaving_ratio_1": 1,
    },
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
    "building_mobility_infrastructures": {
        "max_km_year_infrastructures": 1,
        "mobility_infrastructures_depletion": 1,
        "infrastructure_campaign": 2,
        "year_initiating_infrastructures_plan": 2,
        "time": 2,
        "time_for_infrastructure_campaign_extension": 1,
    },
    "mobility_infrastructures_depletion": {
        "mobility_infrastructures": 1,
        "infrastructures_depletion_time": 1,
    },
    "building_infrastructure": {
        "broadband_infrastructure_depletion": 1,
        "broadband_campaign": 1,
        "year_initiating_broadband_plan": 1,
        "time": 1,
    },
    "broadband_infrastructure_depletion": {
        "broadband_infrastructure_population_covered": 1,
        "broadband_infrastructures_depletion_time": 1,
    },
    "creating_potential_initiatives": {
        "effect_of_social_innovation_in_creating_initiatives_ratio": 1,
        "effect_of_broadband_in_creating_potential_initiatives": 1,
        "working_age_population": 1,
    },
    "planning_initiatives": {"potential_initiatives": 1, "institutional_support": 1},
    "dismissing_potential_initiatives": {
        "potential_initiatives": 1,
        "potential_initiatives_active_time": 1,
    },
    "becoming_stablished_jobs": {
        "implemented_initiatives": 1,
        "time_to_implement_initiatives": 1,
    },
    "building_shared_knowledge": {
        "community_activity_and_networks": 1,
        "time_to_build_effective_shared_knowledge": 1,
    },
    "shared_knowledge_loss": {"shared_knowledge": 1, "shared_knowledge_loss_time": 1},
    "working_age_rural_population": {"working_age_population": 1},
    "farms": {"_integ_farms": 1},
    "_integ_farms": {
        "initial": {"initial_number_of_farms": 1},
        "step": {"increasing_farms": 1, "decreasing_farms": 1},
    },
    "mean_local_income_per_farm": {"_integ_mean_local_income_per_farm": 1},
    "_integ_mean_local_income_per_farm": {
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
    "rest_of_primary_sector_jobs": {"_integ_rest_of_primary_sector_jobs": 1},
    "_integ_rest_of_primary_sector_jobs": {
        "initial": {},
        "step": {"creation_of_primary_jobs": 1, "destruction_of_primary_jobs": 1},
    },
    "industrial_jobs": {"_integ_industrial_jobs": 1},
    "_integ_industrial_jobs": {
        "initial": {},
        "step": {"creation_of_industrial_jobs": 1, "destruction_of_industrial_jobs": 1},
    },
    "service_jobs": {"_integ_service_jobs": 1},
    "_integ_service_jobs": {
        "initial": {},
        "step": {"creation_of_services_jobs": 1, "destruction_of_services_jobs": 1},
    },
    "population_services": {"_integ_population_services": 1},
    "_integ_population_services": {
        "initial": {},
        "step": {"change_in_population_services": 1},
    },
    "natural_capital": {"_integ_natural_capital": 1},
    "_integ_natural_capital": {
        "initial": {"initial_natural_land": 1},
        "step": {"natural_capital_net_variation": 1},
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
    "mobility_infrastructures": {"_integ_mobility_infrastructures": 1},
    "_integ_mobility_infrastructures": {
        "initial": {"initial_mobility_infrastructures": 1},
        "step": {
            "building_mobility_infrastructures": 1,
            "mobility_infrastructures_depletion": 1,
        },
    },
    "broadband_infrastructure_population_covered": {
        "_integ_broadband_infrastructure_population_covered": 1
    },
    "_integ_broadband_infrastructure_population_covered": {
        "initial": {"initial_population_covered": 1},
        "step": {"building_infrastructure": 1, "broadband_infrastructure_depletion": 1},
    },
    "potential_initiatives": {"_integ_potential_initiatives": 1},
    "_integ_potential_initiatives": {
        "initial": {},
        "step": {
            "creating_potential_initiatives": 1,
            "planning_initiatives": 1,
            "dismissing_potential_initiatives": 1,
        },
    },
    "implemented_initiatives": {"_integ_implemented_initiatives": 1},
    "_integ_implemented_initiatives": {
        "initial": {},
        "step": {"planning_initiatives": 1, "becoming_stablished_jobs": 1},
    },
    "shared_knowledge": {"_integ_shared_knowledge": 1},
    "_integ_shared_knowledge": {
        "initial": {},
        "step": {"building_shared_knowledge": 1, "shared_knowledge_loss": 1},
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
                2888.889,
                5777.778,
                8666.667,
                11555.556,
                14444.444,
                17333.333,
                20222.222,
                23111.111,
                26000.000,
            ],
            [1.000, 0.533, 0.284, 0.152, 0.081, 0.043, 0.023, 0.012, 0.007, 0.003],
        )
        if x is None
        else lookup(
            x,
            [
                0.000,
                2888.889,
                5777.778,
                8666.667,
                11555.556,
                14444.444,
                17333.333,
                20222.222,
                23111.111,
                26000.000,
            ],
            [1.000, 0.533, 0.284, 0.152, 0.081, 0.043, 0.023, 0.012, 0.007, 0.003],
        )
    )


def jobs_per_farm():
    """
        Real Name: Jobs_per_farm
        Original Eqn: mean_jobs_per_farm*MAX(1, "diversification/_multifunctionality"/4)
        Units: job/farm
        Limits: (None, None)
        Type: component
        Subs: None

        1,1 Greece - 12,4 Slovakia
    mean 1,5
    """
    return mean_jobs_per_farm() * max(1, diversification_multifunctionality() / 4)


def diversification_multifunctionality():
    """
    Real Name: diversification/_multifunctionality
    Original Eqn: (effect_of_tourism_on_diversification+"CAP_Eco-Schemes")/2
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    0-5
    """
    return (effect_of_tourism_on_diversification() + cap_ecoschemes()) / 2


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
    Original Eqn: social_capital
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    0-1
    """
    return (
        lookup(
            social_capital(),
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
                0.316,
                0.534,
                0.686,
                0.790,
                0.863,
                0.913,
                0.948,
                0.972,
                0.988,
                1.000,
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
                0.316,
                0.534,
                0.686,
                0.790,
                0.863,
                0.913,
                0.948,
                0.972,
                0.988,
                1.000,
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


def land_access():
    """
    Real Name: land_access
    Original Eqn: MIN(0.6, new_forms_of_property)
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    0,6 - 1,2
    """
    return min(0.6, new_forms_of_property())


def new_forms_of_property():
    """
    Real Name: new_forms_of_property
    Original Eqn: "social_innovation_/_potential_initiatives"*AKIS_effect/5
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    0-1,2
    """
    return social_innovation__potential_initiatives() * akis_effect() / 5


def max_agricultural_land():
    """
    Real Name: max_agricultural_land
    Original Eqn: 350000
    Units: ha
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 350000


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
        Original Eqn: land_access*agriculture_profitability
        Units: dmnl/year
        Limits: (None, None)
        Type: lookup
        Subs: None

        0 - 1
    for profitability*land access 0 - 100k
    """
    return (
        lookup(
            land_access() * agriculture_profitability(),
            [
                0.000,
                10000.000,
                20000.000,
                30000.000,
                40000.000,
                50000.000,
                60000.000,
                70000.000,
                80000.000,
                90000.000,
                100000.000,
            ],
            [
                0.000,
                0.003,
                0.008,
                0.017,
                0.032,
                0.059,
                0.106,
                0.187,
                0.328,
                0.573,
                1.000,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                0.000,
                10000.000,
                20000.000,
                30000.000,
                40000.000,
                50000.000,
                60000.000,
                70000.000,
                80000.000,
                90000.000,
                100000.000,
            ],
            [
                0.000,
                0.003,
                0.008,
                0.017,
                0.032,
                0.059,
                0.106,
                0.187,
                0.328,
                0.573,
                1.000,
            ],
        )
    )


def social_innovation__potential_initiatives():
    """
    Real Name: social_innovation_/_potential_initiatives
    Original Eqn: social_innovation
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return social_innovation()


def average_farm_area(x=None):
    """
    Real Name: average_farm_area
    Original Eqn: AKIS_evolution
    Units: ha/farm
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            akis_evolution(),
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
                2.450,
                2.550,
                2.700,
                2.970,
                3.670,
                4.210,
                4.390,
                4.910,
                6.970,
                10.910,
                14.910,
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
                2.450,
                2.550,
                2.700,
                2.970,
                3.670,
                4.210,
                4.390,
                4.910,
                6.970,
                10.910,
                14.910,
            ],
        )
    )


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
    Original Eqn: mean_local_income_per_farm*(1+CAP_direct_payment+other_national_funding)
    Units: €/farm
    Limits: (None, None)
    Type: component
    Subs: None

    0 - 105 aprox

    """
    return mean_local_income_per_farm() * (
        1 + cap_direct_payment() + other_national_funding()
    )


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
    Original Eqn: farms*Jobs_per_farm
    Units: job
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return farms() * jobs_per_farm()


def effect_of_tourism_on_diversification(x=None):
    """
        Real Name: effect_of_tourism_on_diversification
        Original Eqn: tourist_visitors/total_rural_population
        Units: dmnl
        Limits: (None, None)
        Type: lookup
        Subs: None

        0-5
    10 times visitors = 0
    0 times visitors = 2,5
    """
    return (
        lookup(
            tourist_visitors() / total_rural_population(),
            [0.000, 1.111, 2.222, 3.333, 4.444, 5.556, 6.667, 7.778, 8.889, 10.000],
            [2.473, 4.069, 4.628, 4.734, 5.000, 5.000, 4.654, 1.277, 0.505, 0.000],
        )
        if x is None
        else lookup(
            x,
            [0.000, 1.111, 2.222, 3.333, 4.444, 5.556, 6.667, 7.778, 8.889, 10.000],
            [2.473, 4.069, 4.628, 4.734, 5.000, 5.000, 4.654, 1.277, 0.505, 0.000],
        )
    )


def akis_effect():
    """
    Real Name: AKIS_effect
    Original Eqn: AKIS_evolution*0.22
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    0,7-1,2 over time
    """
    return akis_evolution() * 0.22


def cap_reform_direct_payments_decrease_2021():
    """
    Real Name: CAP_reform_direct_payments_decrease_2021
    Original Eqn: 0.05
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.05


def cap_mean_proportion_of_direct_payment_to_fnva():
    """
    Real Name: CAP_mean_proportion_of_direct_payment_to_FNVA
    Original Eqn: 0.44
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None

    FNVA farm net value added
    """
    return 0.44


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
    Original Eqn: 14055
    Units: €/farm
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 14055


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
    Original Eqn: MAX (0.6, AKIS_effect)
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    0-1
    """
    return max(0.6, akis_effect())


def mean_jobs_per_farm(x=None):
    """
    Real Name: mean_jobs_per_farm
    Original Eqn: average_farm_area
    Units: job/farm
    Limits: (None, None)
    Type: lookup
    Subs: None

    1,29
    """
    return (
        lookup(
            average_farm_area(),
            [
                4.000,
                4.410,
                6.200,
                7.300,
                8.400,
                9.500,
                10.600,
                11.700,
                12.800,
                13.900,
                15.000,
            ],
            [
                1.202,
                1.240,
                1.455,
                1.576,
                1.818,
                2.085,
                2.358,
                2.672,
                2.779,
                2.910,
                2.967,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                4.000,
                4.410,
                6.200,
                7.300,
                8.400,
                9.500,
                10.600,
                11.700,
                12.800,
                13.900,
                15.000,
            ],
            [
                1.202,
                1.240,
                1.455,
                1.576,
                1.818,
                2.085,
                2.358,
                2.672,
                2.779,
                2.910,
                2.967,
            ],
        )
    )


def max_improvement_per_diversification():
    """
    Real Name: max_improvement_per_diversification
    Original Eqn: 0.015
    Units: dmnl/year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.015


def initial_number_of_farms():
    """
    Real Name: initial_number_of_farms
    Original Eqn: 70460
    Units: farm
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 70460


def final_technical_obsolescence_time():
    """
    Real Name: final_technical_obsolescence_time
    Original Eqn: 7
    Units: year
    Limits: (2.0, 7.0)
    Type: constant
    Subs: None


    """
    return 7


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


def normal_technical_obsolescence_time(x=None):
    """
    Real Name: normal_technical_obsolescence_time
    Original Eqn: average_farm_area
    Units: year
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            average_farm_area(),
            [
                0.000,
                1.500,
                3.000,
                4.500,
                6.000,
                7.500,
                9.000,
                10.500,
                12.000,
                13.500,
                15.000,
            ],
            [
                4.290,
                4.780,
                5.920,
                7.000,
                7.350,
                7.560,
                8.150,
                9.620,
                10.790,
                11.390,
                11.930,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                0.000,
                1.500,
                3.000,
                4.500,
                6.000,
                7.500,
                9.000,
                10.500,
                12.000,
                13.500,
                15.000,
            ],
            [
                4.290,
                4.780,
                5.920,
                7.000,
                7.350,
                7.560,
                8.150,
                9.620,
                10.790,
                11.390,
                11.930,
            ],
        )
    )


def akis_evolution(x=None):
    """
    Real Name: AKIS_evolution
    Original Eqn: TIME
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            time(),
            [
                2022.000,
                2023.000,
                2024.000,
                2025.000,
                2026.000,
                2027.000,
                2028.000,
                2029.000,
                2030.000,
                2031.000,
                2032.000,
                2033.000,
                2034.000,
                2035.000,
                2036.000,
                2037.000,
                2038.000,
                2039.000,
                2040.000,
            ],
            [
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                2022.000,
                2023.000,
                2024.000,
                2025.000,
                2026.000,
                2027.000,
                2028.000,
                2029.000,
                2030.000,
                2031.000,
                2032.000,
                2033.000,
                2034.000,
                2035.000,
                2036.000,
                2037.000,
                2038.000,
                2039.000,
                2040.000,
            ],
            [
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
            ],
        )
    )


def other_national_funding(x=None):
    """
    Real Name: other_national_funding
    Original Eqn: TIME
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            time(),
            [
                2010.000,
                2011.000,
                2012.000,
                2013.000,
                2014.000,
                2015.000,
                2016.000,
                2017.000,
                2018.000,
                2019.000,
                2020.000,
                2021.000,
                2022.000,
                2023.000,
                2024.000,
                2025.000,
                2026.000,
                2027.000,
                2028.000,
                2029.000,
                2030.000,
                2031.000,
                2032.000,
                2033.000,
                2034.000,
                2035.000,
                2036.000,
                2037.000,
                2038.000,
                2039.000,
                2040.000,
            ],
            [
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                2010.000,
                2011.000,
                2012.000,
                2013.000,
                2014.000,
                2015.000,
                2016.000,
                2017.000,
                2018.000,
                2019.000,
                2020.000,
                2021.000,
                2022.000,
                2023.000,
                2024.000,
                2025.000,
                2026.000,
                2027.000,
                2028.000,
                2029.000,
                2030.000,
                2031.000,
                2032.000,
                2033.000,
                2034.000,
                2035.000,
                2036.000,
                2037.000,
                2038.000,
                2039.000,
                2040.000,
            ],
            [
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
                0.100,
            ],
        )
    )


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
    Original Eqn: 0.54
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.54


def vt_fraction_objective():
    """
    Real Name: VT_fraction_objective
    Original Eqn: 46
    Units: dmnl
    Limits: (0.0, 100.0)
    Type: constant
    Subs: None


    """
    return 46


def initial_fraction_university_students():
    """
    Real Name: initial_fraction_university_students
    Original Eqn: 0.30
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.30


def university_students_objective():
    """
    Real Name: university_students_objective
    Original Eqn: 36
    Units: dmnl
    Limits: (0.0, 100.0)
    Type: constant
    Subs: None


    """
    return 36


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


def unskilled_ratio():
    """
    Real Name: unskilled_ratio
    Original Eqn: UNSKILLED_WORKERS/total_workforce
    Units: person/job
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return unskilled_workers() / total_workforce()


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
    Original Eqn: 0.83
    Units: job/person
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.83


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


def primary_jobs_viability_ratio():
    """
    Real Name: primary_jobs_viability_ratio
    Original Eqn: 0.8
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.8


def new_industrial_job_viability_ratio():
    """
    Real Name: new_industrial_job_viability_ratio
    Original Eqn: 0.6
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.6


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


def previous_population():
    """
    Real Name: Previous_population
    Original Eqn: PREVIOUS(total_rural_population, 535000)
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return previous(
        lambda: total_rural_population(), 535000, __data["time"], __data["scope"]
    )


def difference_of_population():
    """
    Real Name: Difference_of_population
    Original Eqn: total_rural_population-Previous_population
    Units: person
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return total_rural_population() - previous_population()


def ratio_population_services():
    """
        Real Name: ratio_population_services
        Original Eqn: 0.04
        Units: job/person/year
        Limits: (None, None)
        Type: constant
        Subs: None

        Value?
    4%?
    """
    return 0.04


def endogenous_primary_job_creation_ratio():
    """
    Real Name: endogenous_primary_job_creation_ratio
    Original Eqn: endogenous_primary_job_creation
    Units: job/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return endogenous_primary_job_creation()


def endogenous_industrial_job_creation_ratio():
    """
    Real Name: endogenous_industrial_job_creation_ratio
    Original Eqn: endogenous_industrial_job_creation
    Units: job/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return endogenous_industrial_job_creation()


def endogenous_service_jobs_creation_ratio():
    """
    Real Name: endogenous_service_jobs_creation_ratio
    Original Eqn: endogenous_service_job_creation
    Units: job/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return endogenous_service_job_creation()


def total_services_job():
    """
    Real Name: total_services_job
    Original Eqn: population_services+service_jobs +jobs_per_tourism
    Units: job
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return population_services() + service_jobs() + jobs_per_tourism()


def new_services_viability_ratio():
    """
    Real Name: new_services_viability_ratio
    Original Eqn: 0.6
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None

    0-1
    """
    return 0.6


def resulting_average_life_for_industrial_business():
    """
    Real Name: resulting_average_life_for_industrial_business
    Original Eqn: average_life_of_an_industrial_business- STEP (drop_in_the_industrial_average_life_due_to_COVID, 2021)
    Units: year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return average_life_of_an_industrial_business() - step(
        __data["time"], drop_in_the_industrial_average_life_due_to_covid(), 2021
    )


def resulting_average_life_for_services():
    """
    Real Name: resulting_average_life_for_services
    Original Eqn: average_life_of_a_service_business- STEP (Drop_in_the_service_average_life_due_to_COVID, 2021)
    Units: year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return average_life_of_a_service_business() - step(
        __data["time"], drop_in_the_service_average_life_due_to_covid(), 2021
    )


def average_life_of_a_primary_sector_business():
    """
    Real Name: average_life_of_a_primary_sector_business
    Original Eqn: 14
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 14


def drop_in_the_service_average_life_due_to_covid(x=None):
    """
    Real Name: Drop_in_the_service_average_life_due_to_COVID
    Original Eqn: TIME
    Units: year
    Limits: (0.0, 8.0)
    Type: lookup
    Subs: None

    Subtract to the original obsolescence time
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
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
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
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
            ],
        )
    )


def jobs_per_tourism():
    """
    Real Name: jobs_per_tourism
    Original Eqn: tourist_visitors/visitors_per_tourism_workplace
    Units: job
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return tourist_visitors() / visitors_per_tourism_workplace()


def visitors_per_tourism_workplace():
    """
    Real Name: visitors_per_tourism_workplace
    Original Eqn: 36.53
    Units: person/job/year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 36.53


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


def average_life_of_a_service_business():
    """
    Real Name: average_life_of_a_service_business
    Original Eqn: 15
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 15


def average_life_of_an_industrial_business():
    """
    Real Name: average_life_of_an_industrial_business
    Original Eqn: 20
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 20


def drop_in_the_industrial_average_life_due_to_covid(x=None):
    """
    Real Name: drop_in_the_industrial_average_life_due_to_COVID
    Original Eqn: TIME
    Units: year
    Limits: (0.0, 8.0)
    Type: lookup
    Subs: None

    Subtract to the original obsolescence time
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
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
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
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
                0.000,
            ],
        )
    )


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


def total_workforce():
    """
    Real Name: total_workforce
    Original Eqn: workforce_as_ratio_of_WAP*WORKING_AGE_RURAL_POPULATION
    Units: job
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return workforce_as_ratio_of_wap() * working_age_rural_population()


def total_industrial_jobs():
    """
    Real Name: total_industrial_jobs
    Original Eqn: Industrial_jobs
    Units: job
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return industrial_jobs()


def natural_land_variation():
    """
    Real Name: natural_land_variation
    Original Eqn: STEP((natural_land_objective-initial_natural_land)/years_for_completing_natural_land_objective, 2021)
    Units: ha/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return step(
        __data["time"],
        (natural_land_objective() - initial_natural_land())
        / years_for_completing_natural_land_objective(),
        2021,
    )


def potential_visitors_as_a_function_of_natural_capital(x=None):
    """
    Real Name: potential_visitors_as_a_function_of_Natural_Capital
    Original Eqn: Natural_Capital
    Units: person
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            natural_capital(),
            [
                0.000,
                100000.000,
                200000.000,
                300000.000,
                400000.000,
                500000.000,
                600000.000,
                700000.000,
                800000.000,
                900000.000,
                1000000.000,
            ],
            [
                77069.387,
                267714.037,
                919094.796,
                3034327.201,
                8908005.553,
                20000000.000,
                31091994.447,
                36965672.799,
                39080905.204,
                39732285.963,
                39922930.613,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                0.000,
                100000.000,
                200000.000,
                300000.000,
                400000.000,
                500000.000,
                600000.000,
                700000.000,
                800000.000,
                900000.000,
                1000000.000,
            ],
            [
                77069.387,
                267714.037,
                919094.796,
                3034327.201,
                8908005.553,
                20000000.000,
                31091994.447,
                36965672.799,
                39080905.204,
                39732285.963,
                39922930.613,
            ],
        )
    )


def ratio_effect_of_agriculture_on_natural_capital(x=None):
    """
    Real Name: ratio_effect_of_agriculture_on_Natural_Capital
    Original Eqn: "diversification/_multifunctionality"
    Units: dmnl/year
    Limits: (None, None)
    Type: lookup
    Subs: None

    -10% to 10% of agricultural land
    """
    return (
        lookup(
            diversification_multifunctionality(),
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
                -0.197,
                -0.193,
                -0.181,
                -0.152,
                -0.092,
                0.000,
                0.092,
                0.152,
                0.181,
                0.193,
                0.197,
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
                -0.197,
                -0.193,
                -0.181,
                -0.152,
                -0.092,
                0.000,
                0.092,
                0.152,
                0.181,
                0.193,
                0.197,
            ],
        )
    )


def natural_land_objective():
    """
    Real Name: natural_land_objective
    Original Eqn: 502903
    Units: ha
    Limits: (400000.0, 550000.0)
    Type: constant
    Subs: None


    """
    return 502903


_delayn_tourist_visitors = DelayN(
    lambda: (
        attraction_ratio_for_tourists() * (city_and_regional_connections_access() / 5)
    )
    * potential_visitors_as_a_function_of_natural_capital(),
    lambda: 3,
    lambda: (
        attraction_ratio_for_tourists() * (city_and_regional_connections_access() / 5)
    )
    * potential_visitors_as_a_function_of_natural_capital(),
    lambda: 1,
    time_step,
    "_delayn_tourist_visitors",
)


def tourist_visitors():
    """
    Real Name: tourist_visitors
    Original Eqn: DELAY1((attraction_ratio_for_tourists*(city_and_regional_connections_access/5))*potential_visitors_as_a_function_of_Natural_Capital, 3)
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _delayn_tourist_visitors()


_delayn_attraction_ratio_for_tourists = DelayN(
    lambda: tourist_campaign(),
    lambda: time_to_complete_campaign(),
    lambda: tourist_campaign(),
    lambda: 1,
    time_step,
    "_delayn_attraction_ratio_for_tourists",
)


def attraction_ratio_for_tourists():
    """
    Real Name: attraction_ratio_for_tourists
    Original Eqn: DELAY1(tourist_campaign, time_to_complete_campaign)
    Units: dmnl/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _delayn_attraction_ratio_for_tourists()


def effect_of_tourism_on_natural_capital(x=None):
    """
    Real Name: effect_of_tourism_on_natural_capital
    Original Eqn: relative_tourist_visits
    Units: dmnl/year
    Limits: (None, None)
    Type: lookup
    Subs: None

    -10% to 5% of the Natural Capital
    """
    return (
        lookup(
            relative_tourist_visits(),
            [
                0.000,
                0.714,
                1.429,
                2.143,
                2.857,
                3.571,
                4.286,
                5.000,
                5.714,
                6.429,
                7.143,
                7.857,
                8.571,
                9.286,
                10.000,
            ],
            [
                0.004,
                0.008,
                0.013,
                0.015,
                0.015,
                0.013,
                -0.001,
                -0.005,
                -0.008,
                -0.010,
                -0.011,
                -0.012,
                -0.013,
                -0.014,
                -0.015,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                0.000,
                0.714,
                1.429,
                2.143,
                2.857,
                3.571,
                4.286,
                5.000,
                5.714,
                6.429,
                7.143,
                7.857,
                8.571,
                9.286,
                10.000,
            ],
            [
                0.004,
                0.008,
                0.013,
                0.015,
                0.015,
                0.013,
                -0.001,
                -0.005,
                -0.008,
                -0.010,
                -0.011,
                -0.012,
                -0.013,
                -0.014,
                -0.015,
            ],
        )
    )


def relative_natural_capital():
    """
    Real Name: relative_natural_capital
    Original Eqn: Natural_Capital/initial_Natural_capital
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return natural_capital() / initial_natural_capital()


def natural_capital_perception(x=None):
    """
    Real Name: natural_capital_perception
    Original Eqn: relative_natural_capital
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            relative_natural_capital(),
            [
                0.000,
                0.200,
                0.400,
                0.600,
                0.800,
                1.000,
                1.200,
                1.400,
                1.600,
                1.800,
                2.000,
            ],
            [
                0.033,
                0.090,
                0.237,
                0.596,
                1.345,
                2.500,
                3.655,
                4.404,
                4.763,
                4.910,
                4.967,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                0.000,
                0.200,
                0.400,
                0.600,
                0.800,
                1.000,
                1.200,
                1.400,
                1.600,
                1.800,
                2.000,
            ],
            [
                0.033,
                0.090,
                0.237,
                0.596,
                1.345,
                2.500,
                3.655,
                4.404,
                4.763,
                4.910,
                4.967,
            ],
        )
    )


def years_for_completing_natural_land_objective():
    """
    Real Name: years_for_completing_natural_land_objective
    Original Eqn: 10
    Units: year
    Limits: (3.0, 10.0)
    Type: constant
    Subs: None


    """
    return 10


def previous_agricultural_land():
    """
    Real Name: previous_agricultural_land
    Original Eqn: PREVIOUS(agricultural_land, initial_number_of_farms*average_farm_area)
    Units: ha
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return previous(
        lambda: agricultural_land(),
        initial_number_of_farms() * average_farm_area(),
        __data["time"],
        __data["scope"],
    )


def difference_of_agricultural_land():
    """
    Real Name: difference_of_agricultural_land
    Original Eqn: agricultural_land-previous_agricultural_land
    Units: ha
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return agricultural_land() - previous_agricultural_land()


def effect_of_agriculture_on_natural_capital():
    """
    Real Name: effect_of_agriculture_on_Natural_Capital
    Original Eqn: IF difference_of_agricultural_land<0 AND ratio_effect_of_agriculture_on_Natural_Capital<0 THEN ABS (difference_of_agricultural_land)* ratio_effect_of_agriculture_on_Natural_Capital ELSE difference_of_agricultural_land* ratio_effect_of_agriculture_on_Natural_Capital
    Units: ha/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return if_then_else(
        difference_of_agricultural_land() < 0
        and ratio_effect_of_agriculture_on_natural_capital() < 0,
        lambda: abs(difference_of_agricultural_land())
        * ratio_effect_of_agriculture_on_natural_capital(),
        lambda: difference_of_agricultural_land()
        * ratio_effect_of_agriculture_on_natural_capital(),
    )


def normal_attraction_ratio(x=None):
    """
    Real Name: normal_attraction_ratio
    Original Eqn: TIME
    Units: dmnl/year
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            time(),
            [2012.000, 2013.500, 2015.000, 2016.500, 2018.000, 2019.500, 2021.000],
            [0.087, 0.089, 0.132, 0.146, 0.152, 0.161, 0.174],
        )
        if x is None
        else lookup(
            x,
            [2012.000, 2013.500, 2015.000, 2016.500, 2018.000, 2019.500, 2021.000],
            [0.087, 0.089, 0.132, 0.146, 0.152, 0.161, 0.174],
        )
    )


def attraction_ratio_objective():
    """
    Real Name: attraction_ratio_objective
    Original Eqn: 17
    Units: dmnl/year
    Limits: (5.0, 25.0)
    Type: constant
    Subs: None


    """
    return 17


def time_to_complete_campaign():
    """
    Real Name: time_to_complete_campaign
    Original Eqn: 4
    Units: year
    Limits: (2.0, 10.0)
    Type: constant
    Subs: None


    """
    return 4


def tourist_campaign():
    """
    Real Name: tourist_campaign
    Original Eqn: normal_attraction_ratio+ STEP ((attraction_ratio_objective/100)-normal_attraction_ratio, 2021)
    Units: dmnl/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return normal_attraction_ratio() + step(
        __data["time"],
        (attraction_ratio_objective() / 100) - normal_attraction_ratio(),
        2021,
    )


def initial_natural_land():
    """
    Real Name: initial_natural_land
    Original Eqn: 502903
    Units: ha
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 502903


_initial_initial_natural_capital = Initial(
    lambda: natural_capital(), "_initial_initial_natural_capital"
)


def initial_natural_capital():
    """
    Real Name: initial_Natural_capital
    Original Eqn: INIT(Natural_Capital)
    Units: ha
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _initial_initial_natural_capital()


def relative_tourist_visits():
    """
    Real Name: relative_tourist_visits
    Original Eqn: tourist_visitors/total_rural_population
    Units: dmnl/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return tourist_visitors() / total_rural_population()


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
    Original Eqn: 40
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 40


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


def birth_rate(x=None):
    """
    Real Name: birth_rate
    Original Eqn: TIME
    Units: dmnl/year
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            time(),
            [
                2010.000,
                2011.000,
                2012.000,
                2013.000,
                2014.000,
                2015.000,
                2016.000,
                2017.000,
                2018.000,
                2019.000,
                2020.000,
                2021.000,
                2022.000,
                2023.000,
                2024.000,
                2025.000,
                2026.000,
                2027.000,
                2028.000,
                2029.000,
                2030.000,
                2031.000,
                2032.000,
                2033.000,
                2034.000,
                2035.000,
                2036.000,
                2037.000,
                2038.000,
                2039.000,
                2040.000,
            ],
            [
                0.010,
                0.009,
                0.009,
                0.009,
                0.009,
                0.008,
                0.008,
                0.008,
                0.008,
                0.008,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                2010.000,
                2011.000,
                2012.000,
                2013.000,
                2014.000,
                2015.000,
                2016.000,
                2017.000,
                2018.000,
                2019.000,
                2020.000,
                2021.000,
                2022.000,
                2023.000,
                2024.000,
                2025.000,
                2026.000,
                2027.000,
                2028.000,
                2029.000,
                2030.000,
                2031.000,
                2032.000,
                2033.000,
                2034.000,
                2035.000,
                2036.000,
                2037.000,
                2038.000,
                2039.000,
                2040.000,
            ],
            [
                0.010,
                0.009,
                0.009,
                0.009,
                0.009,
                0.008,
                0.008,
                0.008,
                0.008,
                0.008,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
                0.007,
            ],
        )
    )


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
    Original Eqn: 10
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 10


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


def elderly_leaving_ratio_1():
    """
    Real Name: elderly_leaving_ratio_1
    Original Eqn: elderly_leaving_ratio
    Units: dmnl/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return elderly_leaving_ratio()


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
    Original Eqn: 1.27
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 1.27


def max_wa_population_living_rural_per_year():
    """
    Real Name: max_WA_population_living_rural_per_year
    Original Eqn: 0.23
    Units: dmnl/year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.23


def max_post_school_leaving_per_year():
    """
    Real Name: max_post_school_leaving_per_year
    Original Eqn: 0.50
    Units: dmnl/year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.50


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
    Original Eqn: 81.7
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 81.7


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


def health_centers_accessibility(x=None):
    """
    Real Name: health_centers_accessibility
    Original Eqn: mobility_infrastructures
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            mobility_infrastructures(),
            [
                0.000,
                2000.000,
                4000.000,
                6000.000,
                8000.000,
                10000.000,
                12000.000,
                14000.000,
                16000.000,
                18000.000,
                20000.000,
            ],
            [
                0.000,
                0.148,
                0.333,
                0.565,
                0.856,
                1.221,
                1.678,
                2.251,
                2.970,
                3.871,
                5.000,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                0.000,
                2000.000,
                4000.000,
                6000.000,
                8000.000,
                10000.000,
                12000.000,
                14000.000,
                16000.000,
                18000.000,
                20000.000,
            ],
            [
                0.000,
                0.148,
                0.333,
                0.565,
                0.856,
                1.221,
                1.678,
                2.251,
                2.970,
                3.871,
                5.000,
            ],
        )
    )


def vt_centers_accessibility(x=None):
    """
    Real Name: VT_centers_accessibility
    Original Eqn: mobility_infrastructures
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            mobility_infrastructures(),
            [
                0.000,
                2000.000,
                4000.000,
                6000.000,
                8000.000,
                10000.000,
                12000.000,
                14000.000,
                16000.000,
                18000.000,
                20000.000,
            ],
            [
                0.000,
                1.934,
                3.126,
                3.860,
                4.313,
                4.592,
                4.764,
                4.870,
                4.935,
                4.975,
                5.000,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                0.000,
                2000.000,
                4000.000,
                6000.000,
                8000.000,
                10000.000,
                12000.000,
                14000.000,
                16000.000,
                18000.000,
                20000.000,
            ],
            [
                0.000,
                1.934,
                3.126,
                3.860,
                4.313,
                4.592,
                4.764,
                4.870,
                4.935,
                4.975,
                5.000,
            ],
        )
    )


def university_accessibility(x=None):
    """
    Real Name: University_Accessibility
    Original Eqn: mobility_infrastructures
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            mobility_infrastructures(),
            [
                0.000,
                2000.000,
                4000.000,
                6000.000,
                8000.000,
                10000.000,
                12000.000,
                14000.000,
                16000.000,
                18000.000,
                20000.000,
            ],
            [
                0.000,
                1.862,
                3.038,
                3.780,
                4.249,
                4.544,
                4.731,
                4.849,
                4.923,
                4.970,
                5.000,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                0.000,
                2000.000,
                4000.000,
                6000.000,
                8000.000,
                10000.000,
                12000.000,
                14000.000,
                16000.000,
                18000.000,
                20000.000,
            ],
            [
                0.000,
                1.862,
                3.038,
                3.780,
                4.249,
                4.544,
                4.731,
                4.849,
                4.923,
                4.970,
                5.000,
            ],
        )
    )


def community_activity_and_networks():
    """
    Real Name: community_activity_and_networks
    Original Eqn: community_and_public_services_accessibility*community_climate
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return community_and_public_services_accessibility() * community_climate()


def social_capital(x=None):
    """
    Real Name: social_capital
    Original Eqn: shared_knowledge
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            shared_knowledge(),
            [
                0.000,
                0.667,
                1.333,
                2.000,
                2.667,
                3.333,
                4.000,
                4.667,
                5.333,
                6.000,
                6.667,
                7.333,
                8.000,
                8.667,
                9.333,
                10.000,
            ],
            [
                1.000,
                1.267,
                1.533,
                1.800,
                2.067,
                2.333,
                2.600,
                2.867,
                3.133,
                3.400,
                3.667,
                3.933,
                4.200,
                4.467,
                4.733,
                5.000,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                0.000,
                0.667,
                1.333,
                2.000,
                2.667,
                3.333,
                4.000,
                4.667,
                5.333,
                6.000,
                6.667,
                7.333,
                8.000,
                8.667,
                9.333,
                10.000,
            ],
            [
                1.000,
                1.267,
                1.533,
                1.800,
                2.067,
                2.333,
                2.600,
                2.867,
                3.133,
                3.400,
                3.667,
                3.933,
                4.200,
                4.467,
                4.733,
                5.000,
            ],
        )
    )


def social_innovation():
    """
    Real Name: social_innovation
    Original Eqn: social_capital*workforce_specialization
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    0-5
    """
    return social_capital() * workforce_specialization()


def city_and_regional_connections_access(x=None):
    """
    Real Name: city_and_regional_connections_access
    Original Eqn: mobility_infrastructures
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            mobility_infrastructures(),
            [
                0.000,
                2000.000,
                4000.000,
                6000.000,
                8000.000,
                10000.000,
                12000.000,
                14000.000,
                16000.000,
                18000.000,
                20000.000,
            ],
            [
                0.000,
                1.679,
                2.805,
                3.559,
                4.065,
                4.404,
                4.631,
                4.784,
                4.886,
                4.954,
                5.000,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                0.000,
                2000.000,
                4000.000,
                6000.000,
                8000.000,
                10000.000,
                12000.000,
                14000.000,
                16000.000,
                18000.000,
                20000.000,
            ],
            [
                0.000,
                1.679,
                2.805,
                3.559,
                4.065,
                4.404,
                4.631,
                4.784,
                4.886,
                4.954,
                5.000,
            ],
        )
    )


def cultural_appeal(x=None):
    """
    Real Name: cultural_appeal
    Original Eqn: shared_knowledge
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            shared_knowledge(),
            [
                0.000,
                4.000,
                8.000,
                12.000,
                16.000,
                20.000,
                24.000,
                28.000,
                32.000,
                36.000,
                40.000,
            ],
            [
                0.000,
                1.679,
                2.805,
                3.559,
                4.065,
                4.404,
                4.631,
                4.784,
                4.886,
                4.954,
                5.000,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                0.000,
                4.000,
                8.000,
                12.000,
                16.000,
                20.000,
                24.000,
                28.000,
                32.000,
                36.000,
                40.000,
            ],
            [
                0.000,
                1.679,
                2.805,
                3.559,
                4.065,
                4.404,
                4.631,
                4.784,
                4.886,
                4.954,
                5.000,
            ],
        )
    )


def institutional_support(x=None):
    """
    Real Name: institutional_support
    Original Eqn: LOG10(inst_support_evolution)
    Units: dmnl/year
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            np.log10(inst_support_evolution()),
            [
                0.000,
                1.000,
                2.000,
                3.000,
                4.000,
                5.000,
                6.000,
                7.000,
                8.000,
                9.000,
                10.000,
            ],
            [
                0.150,
                0.184,
                0.206,
                0.221,
                0.231,
                0.238,
                0.243,
                0.246,
                0.248,
                0.249,
                0.250,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                0.000,
                1.000,
                2.000,
                3.000,
                4.000,
                5.000,
                6.000,
                7.000,
                8.000,
                9.000,
                10.000,
            ],
            [
                0.150,
                0.184,
                0.206,
                0.221,
                0.231,
                0.238,
                0.243,
                0.246,
                0.248,
                0.249,
                0.250,
            ],
        )
    )


def infrastructures_depletion_time():
    """
    Real Name: infrastructures_depletion_time
    Original Eqn: 30
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 30


def potential_initiatives_active_time():
    """
    Real Name: potential_initiatives_active_time
    Original Eqn: 2
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 2


def population_covered_objective():
    """
    Real Name: population_covered_objective
    Original Eqn: 66
    Units: dmnl
    Limits: (65.0, 100.0)
    Type: constant
    Subs: None


    """
    return 66


def broadband_infrastructures_depletion_time():
    """
    Real Name: broadband_infrastructures_depletion_time
    Original Eqn: 10
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 10


def endogenous_primary_job_creation():
    """
    Real Name: endogenous_primary_job_creation
    Original Eqn: becoming_stablished_jobs*0.15*average_jobs_per_primary_initiative
    Units: job/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return becoming_stablished_jobs() * 0.15 * average_jobs_per_primary_initiative()


def endogenous_industrial_job_creation():
    """
    Real Name: endogenous_industrial_job_creation
    Original Eqn: becoming_stablished_jobs*0.15*average_jobs_per_industrial_initiative
    Units: job/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return becoming_stablished_jobs() * 0.15 * average_jobs_per_industrial_initiative()


def endogenous_service_job_creation():
    """
    Real Name: endogenous_service_job_creation
    Original Eqn: becoming_stablished_jobs*0.7*average_jobs_per_service_initiative
    Units: job/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return becoming_stablished_jobs() * 0.7 * average_jobs_per_service_initiative()


def time_to_implement_initiatives():
    """
    Real Name: time_to_implement_initiatives
    Original Eqn: 1
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 1


def infrastructures_objective():
    """
    Real Name: infrastructures_objective
    Original Eqn: 9000
    Units: km
    Limits: (9000.0, 20000.0)
    Type: constant
    Subs: None


    """
    return 9000


def community_and_public_services_accessibility(x=None):
    """
    Real Name: community_and_public_services_accessibility
    Original Eqn: mobility_infrastructures
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            mobility_infrastructures(),
            [
                0.000,
                2000.000,
                4000.000,
                6000.000,
                8000.000,
                10000.000,
                12000.000,
                14000.000,
                16000.000,
                18000.000,
                20000.000,
            ],
            [
                0.000,
                0.230,
                0.412,
                0.556,
                0.671,
                0.761,
                0.833,
                0.890,
                0.936,
                0.972,
                1.000,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                0.000,
                2000.000,
                4000.000,
                6000.000,
                8000.000,
                10000.000,
                12000.000,
                14000.000,
                16000.000,
                18000.000,
                20000.000,
            ],
            [
                0.000,
                0.230,
                0.412,
                0.556,
                0.671,
                0.761,
                0.833,
                0.890,
                0.936,
                0.972,
                1.000,
            ],
        )
    )


def time_to_build_effective_shared_knowledge(x=None):
    """
    Real Name: time_to_build_effective_shared_knowledge
    Original Eqn: proportion_of_newcomers
    Units: year
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            proportion_of_newcomers(),
            [
                0.000,
                0.070,
                0.140,
                0.210,
                0.280,
                0.350,
                0.420,
                0.490,
                0.560,
                0.630,
                0.700,
            ],
            [
                1.027,
                1.072,
                1.190,
                1.477,
                2.076,
                3.000,
                3.924,
                4.523,
                4.810,
                4.928,
                4.973,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                0.000,
                0.070,
                0.140,
                0.210,
                0.280,
                0.350,
                0.420,
                0.490,
                0.560,
                0.630,
                0.700,
            ],
            [
                1.027,
                1.072,
                1.190,
                1.477,
                2.076,
                3.000,
                3.924,
                4.523,
                4.810,
                4.928,
                4.973,
            ],
        )
    )


def effect_of_social_innovation_in_creating_initiatives_ratio(x=None):
    """
    Real Name: effect_of_social_innovation_in_creating_initiatives_ratio
    Original Eqn: social_innovation
    Units: initiative/person/year
    Limits: (None, None)
    Type: lookup
    Subs: None

    social innovation 0 - 5
    """
    return (
        lookup(
            social_innovation(),
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
                0.010,
                0.017,
                0.021,
                0.024,
                0.026,
                0.028,
                0.029,
                0.029,
                0.030,
                0.030,
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
                0.010,
                0.017,
                0.021,
                0.024,
                0.026,
                0.028,
                0.029,
                0.029,
                0.030,
                0.030,
            ],
        )
    )


def effect_of_broadband_in_creating_potential_initiatives(x=None):
    """
    Real Name: effect_of_broadband_in_creating_potential_initiatives
    Original Eqn: broadband_infrastructure_population_covered
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            broadband_infrastructure_population_covered(),
            [
                0.000,
                10.000,
                20.000,
                30.000,
                40.000,
                50.000,
                60.000,
                70.000,
                80.000,
                90.000,
                100.000,
            ],
            [
                0.007,
                0.018,
                0.047,
                0.119,
                0.269,
                0.500,
                0.731,
                0.881,
                0.953,
                0.982,
                0.993,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                0.000,
                10.000,
                20.000,
                30.000,
                40.000,
                50.000,
                60.000,
                70.000,
                80.000,
                90.000,
                100.000,
            ],
            [
                0.007,
                0.018,
                0.047,
                0.119,
                0.269,
                0.500,
                0.731,
                0.881,
                0.953,
                0.982,
                0.993,
            ],
        )
    )


def year_initiating_infrastructures_plan():
    """
    Real Name: year_initiating_infrastructures_plan
    Original Eqn: 2021
    Units: year
    Limits: (2021.0, 2040.0)
    Type: constant
    Subs: None


    """
    return 2021


def year_initiating_broadband_plan():
    """
    Real Name: year_initiating_broadband_plan
    Original Eqn: 2010
    Units: year
    Limits: (2021.0, 2040.0)
    Type: constant
    Subs: None


    """
    return 2010


def shared_knowledge_loss_time():
    """
    Real Name: shared_knowledge_loss_time
    Original Eqn: 3
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 3


def community_climate(x=None):
    """
    Real Name: community_climate
    Original Eqn: TIME
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None

    0 - 5 over time
    """
    return (
        lookup(
            time(),
            [
                2010.000,
                2011.500,
                2013.000,
                2014.500,
                2016.000,
                2017.500,
                2019.000,
                2020.500,
                2022.000,
                2023.500,
                2025.000,
                2026.500,
                2028.000,
                2029.500,
                2031.000,
                2032.500,
                2034.000,
                2035.500,
                2037.000,
                2038.500,
                2040.000,
            ],
            [
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                2010.000,
                2011.500,
                2013.000,
                2014.500,
                2016.000,
                2017.500,
                2019.000,
                2020.500,
                2022.000,
                2023.500,
                2025.000,
                2026.500,
                2028.000,
                2029.500,
                2031.000,
                2032.500,
                2034.000,
                2035.500,
                2037.000,
                2038.500,
                2040.000,
            ],
            [
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
                3.000,
            ],
        )
    )


def max_km_year_infrastructures():
    """
    Real Name: max_km_year_infrastructures
    Original Eqn: 500
    Units: km/year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 500


def broadband_gap():
    """
    Real Name: broadband_gap
    Original Eqn: population_covered_objective-broadband_infrastructure_population_covered
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        population_covered_objective() - broadband_infrastructure_population_covered()
    )


def average_jobs_per_service_initiative():
    """
    Real Name: average_jobs_per_service_initiative
    Original Eqn: 5
    Units: job/initiative
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 5


def average_jobs_per_primary_initiative():
    """
    Real Name: average_jobs_per_primary_initiative
    Original Eqn: 10
    Units: job/initiative
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 10


def average_jobs_per_industrial_initiative():
    """
    Real Name: average_jobs_per_industrial_initiative
    Original Eqn: 10
    Units: job/initiative
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 10


def broadband_effect_on_retention(x=None):
    """
    Real Name: broadband_effect_on_retention
    Original Eqn: broadband_infrastructure_population_covered
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            broadband_infrastructure_population_covered(),
            [
                63.000,
                65.000,
                70.400,
                74.100,
                77.800,
                81.500,
                85.200,
                88.900,
                92.600,
                96.300,
                100.000,
            ],
            [
                0.830,
                0.970,
                0.984,
                0.987,
                0.994,
                0.997,
                0.999,
                0.999,
                1.000,
                1.000,
                1.000,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                63.000,
                65.000,
                70.400,
                74.100,
                77.800,
                81.500,
                85.200,
                88.900,
                92.600,
                96.300,
                100.000,
            ],
            [
                0.830,
                0.970,
                0.984,
                0.987,
                0.994,
                0.997,
                0.999,
                0.999,
                1.000,
                1.000,
                1.000,
            ],
        )
    )


def social_capital_effect_on_retention(x=None):
    """
    Real Name: social_capital_effect_on_retention
    Original Eqn: social_capital
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            social_capital(),
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
                0.300,
                0.684,
                0.858,
                0.936,
                0.971,
                0.987,
                0.994,
                0.998,
                0.999,
                1.000,
                1.000,
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
                0.300,
                0.684,
                0.858,
                0.936,
                0.971,
                0.987,
                0.994,
                0.998,
                0.999,
                1.000,
                1.000,
            ],
        )
    )


def effect_of_cr_connections_on_retention(x=None):
    """
    Real Name: effect_of_c&r_connections_on_retention
    Original Eqn: city_and_regional_connections_access
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            city_and_regional_connections_access(),
            [4.000, 4.140, 4.230, 4.600, 4.800, 5.000],
            [0.700, 0.710, 0.910, 0.966, 0.982, 1.000],
        )
        if x is None
        else lookup(
            x,
            [4.000, 4.140, 4.230, 4.600, 4.800, 5.000],
            [0.700, 0.710, 0.910, 0.966, 0.982, 1.000],
        )
    )


def infrastructures_gap():
    """
    Real Name: infrastructures_gap
    Original Eqn: infrastructures_objective-initial_mobility_infrastructures
    Units: km
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return infrastructures_objective() - initial_mobility_infrastructures()


def initial_mobility_infrastructures():
    """
    Real Name: initial_mobility_infrastructures
    Original Eqn: 9000
    Units: km
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 9000


def initial_population_covered():
    """
    Real Name: initial_population_covered
    Original Eqn: 43
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 43


def infrastructure_campaign():
    """
    Real Name: infrastructure_campaign
    Original Eqn: infrastructures_gap/time_for_infrastructure_campaign_extension
    Units: km/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return infrastructures_gap() / time_for_infrastructure_campaign_extension()


def time_for_infrastructure_campaign_extension():
    """
    Real Name: time_for_infrastructure_campaign_extension
    Original Eqn: 10
    Units: year
    Limits: (2.0, 10.0)
    Type: constant
    Subs: None


    """
    return 10


def broadband_campaign():
    """
    Real Name: broadband_campaign
    Original Eqn: broadband_gap/time_to_complete_broadband_campaign
    Units: dmnl/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return broadband_gap() / time_to_complete_broadband_campaign()


def time_to_complete_broadband_campaign():
    """
    Real Name: time_to_complete_broadband_campaign
    Original Eqn: 4
    Units: year
    Limits: (2.0, 10.0)
    Type: constant
    Subs: None


    """
    return 4


def inst_support_evolution(x=None):
    """
    Real Name: inst_support_evolution
    Original Eqn: TIME
    Units: dmnl/year
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            time(),
            [2016.000, 2017.000, 2018.000, 2020.000],
            [14421569.000, 19733540.000, 5705255.000, 2647261.000],
        )
        if x is None
        else lookup(
            x,
            [2016.000, 2017.000, 2018.000, 2020.000],
            [14421569.000, 19733540.000, 5705255.000, 2647261.000],
        )
    )


def wa_moving():
    """
        Real Name: WA_moving
        Original Eqn: IF employment_gap_1>0 THEN ((employment_gap_1/WA_applying_employment_gap)*(housing_accessibility_factor_for_WA+natural_capital_factor_for_WA+cultural_appeal_factor_for_WA+public_services_factor_for_WA_attraction)) ELSE 0
        Units: person/year
        Limits: (None, None)
        Type: component
        Subs: None

        WA MOVING RATIO weights = 0,52 (of the employment gap)
    TOTAL = 1,02
    """
    return if_then_else(
        employment_gap_1() > 0,
        lambda: (
            (employment_gap_1() / wa_applying_employment_gap())
            * (
                housing_accessibility_factor_for_wa()
                + natural_capital_factor_for_wa()
                + cultural_appeal_factor_for_wa()
                + public_services_factor_for_wa_attraction()
            )
        ),
        lambda: 0,
    )


def elderly_move_rural():
    """
    Real Name: elderly_move_rural
    Original Eqn: maximum_elderly_population_moving* (natural_capital_factor_for_elderly+ cultural_appeal_factor_for_elderly+ housing_accessibility_factor_for_elderly+ medical_and_care_services_factor)
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return maximum_elderly_population_moving() * (
        natural_capital_factor_for_elderly()
        + cultural_appeal_factor_for_elderly()
        + housing_accessibility_factor_for_elderly()
        + medical_and_care_services_factor()
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
            [0.700, 0.956, 1.211, 1.467, 1.722, 1.978, 2.233, 2.489, 2.744, 3.000],
            [4.999, 4.993, 4.955, 4.718, 3.594, 1.406, 0.282, 0.045, 0.007, 0.001],
        )
        if x is None
        else lookup(
            x,
            [0.700, 0.956, 1.211, 1.467, 1.722, 1.978, 2.233, 2.489, 2.744, 3.000],
            [4.999, 4.993, 4.955, 4.718, 3.594, 1.406, 0.282, 0.045, 0.007, 0.001],
        )
    )


def maximum_elderly_population_moving():
    """
    Real Name: maximum_elderly_population_moving
    Original Eqn: 500
    Units: person/year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 500


def natural_capital_weight_for_young():
    """
    Real Name: natural_capital_weight_for_young
    Original Eqn: 0.15
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None

    NCWFY + HAWFY = 0,5 (of the employment gap)
    """
    return 0.15


def cultural_appeal_weight_for_wa():
    """
    Real Name: cultural_appeal_weight_for_WA
    Original Eqn: 0.15
    Units: dmnl
    Limits: (0.0, 1.0)
    Type: constant
    Subs: None


    """
    return 0.15


def natural_capital_weight_for_wa():
    """
    Real Name: natural_capital_weight_for_WA
    Original Eqn: 0.25
    Units: dmnl
    Limits: (0.0, 1.0)
    Type: constant
    Subs: None


    """
    return 0.25


def housing_accessibility_weight_for_wa():
    """
    Real Name: housing_accessibility_weight_for_WA
    Original Eqn: 0.32
    Units: dmnl
    Limits: (0.0, 1.0)
    Type: constant
    Subs: None


    """
    return 0.32


def medical_and_care_services_weight():
    """
    Real Name: medical_and_care_services_weight
    Original Eqn: 0.32
    Units: dmnl
    Limits: (0.0, 1.0)
    Type: constant
    Subs: None


    """
    return 0.32


def cultural_appeal_weight_for_elderly():
    """
    Real Name: cultural_appeal_weight_for_elderly
    Original Eqn: 0.2
    Units: dmnl
    Limits: (0.0, 1.0)
    Type: constant
    Subs: None


    """
    return 0.2


def natural_capital_weight_for_elderly():
    """
    Real Name: natural_capital_weight_for_elderly
    Original Eqn: 0.2
    Units: dmnl
    Limits: (0.0, 1.0)
    Type: constant
    Subs: None


    """
    return 0.2


def housing_accessibility_weight_for_elderly():
    """
    Real Name: housing_accessibility_weight_for_elderly
    Original Eqn: 0.28
    Units: dmnl
    Limits: (0.0, 1.0)
    Type: constant
    Subs: None


    """
    return 0.28


def housing_accessibility_factor_for_young():
    """
    Real Name: housing_accessibility_factor_for_young
    Original Eqn: housing_accessibility_weight_for_young*0.5*housing_accessibility/5
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return housing_accessibility_weight_for_young() * 0.5 * housing_accessibility() / 5


def natural_capital_factor_for_young():
    """
    Real Name: natural_capital_factor_for_young
    Original Eqn: natural_capital_weight_for_young*0.5*natural_capital_perception/5
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return natural_capital_weight_for_young() * 0.5 * natural_capital_perception() / 5


def housing_accessibility_factor_for_wa():
    """
    Real Name: housing_accessibility_factor_for_WA
    Original Eqn: housing_accessibility_weight_for_WA*housing_accessibility*0.52/5
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return housing_accessibility_weight_for_wa() * housing_accessibility() * 0.52 / 5


def housing_accessibility_factor_for_elderly():
    """
    Real Name: housing_accessibility_factor_for_elderly
    Original Eqn: housing_accessibility_weight_for_elderly*housing_accessibility/5
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return housing_accessibility_weight_for_elderly() * housing_accessibility() / 5


def medical_and_care_services_factor():
    """
    Real Name: medical_and_care_services_factor
    Original Eqn: health_centers_accessibility*medical_and_care_services_weight/5
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return health_centers_accessibility() * medical_and_care_services_weight() / 5


def natural_capital_factor_for_wa():
    """
    Real Name: natural_capital_factor_for_WA
    Original Eqn: natural_capital_weight_for_WA*0.52* natural_capital_perception/5
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return natural_capital_weight_for_wa() * 0.52 * natural_capital_perception() / 5


def cultural_appeal_factor_for_wa():
    """
    Real Name: cultural_appeal_factor_for_WA
    Original Eqn: cultural_appeal_weight_for_WA*0.52*cultural_appeal/5
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return cultural_appeal_weight_for_wa() * 0.52 * cultural_appeal() / 5


def cultural_appeal_factor_for_elderly():
    """
    Real Name: cultural_appeal_factor_for_elderly
    Original Eqn: cultural_appeal_weight_for_elderly*cultural_appeal/5
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return cultural_appeal_weight_for_elderly() * cultural_appeal() / 5


def natural_capital_factor_for_elderly():
    """
    Real Name: natural_capital_factor_for_elderly
    Original Eqn: natural_capital_perception*natural_capital_weight_for_elderly/5
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return natural_capital_perception() * natural_capital_weight_for_elderly() / 5


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


def public_services_factor_for_wa_attraction():
    """
    Real Name: public_services_factor_for_WA_attraction
    Original Eqn: community_and_public_services_accessibility*public_services_weight_in_WA_attraction*0.52
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        community_and_public_services_accessibility()
        * public_services_weight_in_wa_attraction()
        * 0.52
    )


def public_services_weight_in_wa_attraction():
    """
    Real Name: public_services_weight_in_WA_attraction
    Original Eqn: 0.28
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.28


def ps_moving():
    """
    Real Name: PS_moving
    Original Eqn: IF employment_gap_1>0 THEN (employment_gap_1/young_applying_employment_gap)* (housing_accessibility_factor_for_young+ natural_capital_factor_for_young+social_capital_factor_for_young) ELSE 0
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None

    NCWFY + HAWFY = 0,5 (of the employment gap)
    """
    return if_then_else(
        employment_gap_1() > 0,
        lambda: (employment_gap_1() / young_applying_employment_gap())
        * (
            housing_accessibility_factor_for_young()
            + natural_capital_factor_for_young()
            + social_capital_factor_for_young()
        ),
        lambda: 0,
    )


def young_applying_employment_gap():
    """
    Real Name: young_applying_employment_gap
    Original Eqn: 1.5
    Units: job*year/person
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 1.5


def wa_applying_employment_gap():
    """
    Real Name: WA_applying_employment_gap
    Original Eqn: 1
    Units: job*year/person
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 1


def post_school_leaving_ratio():
    """
    Real Name: post_school_leaving_ratio
    Original Eqn: 1- (higher_education_factor+ broadband_factor_for_young+ social_capital_factor_for_young+ housing_factor_for_young+ employment_factor_for_young)
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return 1 - (
        higher_education_factor()
        + broadband_factor_for_young()
        + social_capital_factor_for_young()
        + housing_factor_for_young()
        + employment_factor_for_young()
    )


def wa_leaving_ratio():
    """
    Real Name: WA_leaving_ratio
    Original Eqn: (1-retention_factor)* effect_of_employment_in_WA_leaving_ratio
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (1 - retention_factor()) * effect_of_employment_in_wa_leaving_ratio()


def elderly_leaving_ratio():
    """
    Real Name: elderly_leaving_ratio
    Original Eqn: maximum_ratio_elderly_population_leaving* (1- medical_and_care_factor- social_capital_factor_for_elderly)
    Units: dmnl/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return maximum_ratio_elderly_population_leaving() * (
        1 - medical_and_care_factor() - social_capital_factor_for_elderly()
    )


def maximum_ratio_elderly_population_leaving():
    """
    Real Name: maximum_ratio_elderly_population_leaving
    Original Eqn: 0.07
    Units: dmnl/year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.07


def higher_education_weight():
    """
    Real Name: higher_education_weight
    Original Eqn: 0.22
    Units: dmnl
    Limits: (0.0, 1.0)
    Type: constant
    Subs: None


    """
    return 0.22


def broadband_weight_for_young():
    """
    Real Name: broadband_weight_for_young
    Original Eqn: 0.22
    Units: dmnl
    Limits: (0.0, 1.0)
    Type: constant
    Subs: None


    """
    return 0.22


def housing_accessibility_weight_for_young():
    """
    Real Name: housing_accessibility_weight_for_young
    Original Eqn: 0.1
    Units: dmnl
    Limits: (0.0, 1.0)
    Type: constant
    Subs: None


    """
    return 0.1


def social_capital_weight_for_young():
    """
    Real Name: social_capital_weight_for_young
    Original Eqn: 0.22
    Units: dmnl
    Limits: (0.0, 1.0)
    Type: constant
    Subs: None


    """
    return 0.22


def broadband_weight_for_wa():
    """
    Real Name: broadband_weight_for_WA
    Original Eqn: 0.25
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.25


def cr_connections_weight():
    """
    Real Name: c&r_connections_weight
    Original Eqn: 0.25
    Units: dmnl
    Limits: (0.0, 1.0)
    Type: constant
    Subs: None


    """
    return 0.25


def social_capital_weight_for_wa():
    """
    Real Name: social_capital_weight_for_WA
    Original Eqn: 0.25
    Units: dmnl
    Limits: (0.0, 1.0)
    Type: constant
    Subs: None


    """
    return 0.25


def medical_and_care_weight():
    """
    Real Name: medical_and_care_weight
    Original Eqn: 0.65
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.65


def social_capital_weight_for_elderly():
    """
    Real Name: social_capital_weight_for_elderly
    Original Eqn: 0.35
    Units: dmnl
    Limits: (0.0, 1.0)
    Type: constant
    Subs: None


    """
    return 0.35


def employment_weight_for_young():
    """
    Real Name: employment_weight_for_young
    Original Eqn: 0.24
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.24


def effect_of_employment_in_ps_retention_ratio(x=None):
    """
    Real Name: effect_of_employment_in_PS_retention_ratio
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
                -1.000,
                -0.800,
                -0.600,
                -0.400,
                -0.200,
                0.000,
                0.200,
                0.400,
                0.600,
                0.800,
                1.000,
            ],
            [
                3.000,
                4.105,
                4.600,
                4.821,
                4.920,
                4.965,
                4.985,
                4.993,
                4.997,
                4.999,
                5.000,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                -1.000,
                -0.800,
                -0.600,
                -0.400,
                -0.200,
                0.000,
                0.200,
                0.400,
                0.600,
                0.800,
                1.000,
            ],
            [
                3.000,
                4.105,
                4.600,
                4.821,
                4.920,
                4.965,
                4.985,
                4.993,
                4.997,
                4.999,
                5.000,
            ],
        )
    )


def higher_education_factor():
    """
    Real Name: higher_education_factor
    Original Eqn: (VT_centers_accessibility+University_Accessibility)*higher_education_weight/10
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        (vt_centers_accessibility() + university_accessibility())
        * higher_education_weight()
        / 10
    )


def broadband_factor_for_young():
    """
    Real Name: broadband_factor_for_young
    Original Eqn: broadband_weight_for_young*broadband_effect_on_retention
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    is divided by 100 because ...pop covered... is expressed in % (50%)
    """
    return broadband_weight_for_young() * broadband_effect_on_retention()


def housing_factor_for_young():
    """
    Real Name: housing_factor_for_young
    Original Eqn: housing_accessibility_weight_for_young*housing_accessibility/5
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return housing_accessibility_weight_for_young() * housing_accessibility() / 5


def social_capital_factor_for_young():
    """
    Real Name: social_capital_factor_for_young
    Original Eqn: social_capital_weight_for_young*social_capital_effect_on_retention
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return social_capital_weight_for_young() * social_capital_effect_on_retention()


def employment_factor_for_young():
    """
    Real Name: employment_factor_for_young
    Original Eqn: (employment_weight_for_young/5)*effect_of_employment_in_PS_retention_ratio
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        employment_weight_for_young() / 5
    ) * effect_of_employment_in_ps_retention_ratio()


def broadband_factor_for_wa():
    """
    Real Name: broadband_factor_for_WA
    Original Eqn: broadband_weight_for_WA*broadband_effect_on_retention
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    is divided by 100 because ...pop covered... is expressed in % (50%)
    """
    return broadband_weight_for_wa() * broadband_effect_on_retention()


def social_capital_factor_for_wa():
    """
    Real Name: social_capital_factor_for_WA
    Original Eqn: (social_capital_weight_for_WA/5)*social_capital_effect_on_retention
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (social_capital_weight_for_wa() / 5) * social_capital_effect_on_retention()


def cr_factor():
    """
    Real Name: c&r_factor
    Original Eqn: city_and_regional_connections_access*"c&r_connections_weight"/5
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return city_and_regional_connections_access() * cr_connections_weight() / 5


def social_capital_factor_for_elderly():
    """
    Real Name: social_capital_factor_for_elderly
    Original Eqn: social_capital_weight_for_elderly*social_capital_effect_on_retention
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return social_capital_weight_for_elderly() * social_capital_effect_on_retention()


def medical_and_care_factor():
    """
    Real Name: medical_and_care_factor
    Original Eqn: medical_and_care_weight*health_centers_accessibility/5
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return medical_and_care_weight() * health_centers_accessibility() / 5


def retention_factor():
    """
    Real Name: retention_factor
    Original Eqn: social_capital_factor_for_WA+broadband_factor_for_WA+"c&r_factor"+public_services_retention
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        social_capital_factor_for_wa()
        + broadband_factor_for_wa()
        + cr_factor()
        + public_services_retention()
    )


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
                -1.000,
                -0.800,
                -0.600,
                -0.400,
                -0.200,
                0.000,
                0.200,
                0.400,
                0.600,
                0.800,
                1.000,
            ],
            [
                0.005,
                0.005,
                0.005,
                0.004,
                0.004,
                0.003,
                0.001,
                0.001,
                0.000,
                0.000,
                0.000,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                -1.000,
                -0.800,
                -0.600,
                -0.400,
                -0.200,
                0.000,
                0.200,
                0.400,
                0.600,
                0.800,
                1.000,
            ],
            [
                0.005,
                0.005,
                0.005,
                0.004,
                0.004,
                0.003,
                0.001,
                0.001,
                0.000,
                0.000,
                0.000,
            ],
        )
    )


def public_services_weight_for_wa_retention():
    """
    Real Name: public_services_weight_for_WA_retention
    Original Eqn: 0.25
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.25


def public_services_retention():
    """
    Real Name: public_services_retention
    Original Eqn: public_services_weight_for_WA_retention*community_and_public_services_accessibility
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        public_services_weight_for_wa_retention()
        * community_and_public_services_accessibility()
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
    Original Eqn: (decreasing_income_per_farm*agricultural_obsolescence_covered)+ ("diversification/_multifunctionality"*mean_local_income_per_farm*max_improvement_per_diversification)
    Units: €/farm/Years
    Limits: (None, None)
    Type: component
    Subs: None

    diversification can increase up to a 10% income (/50)
    """
    return (decreasing_income_per_farm() * agricultural_obsolescence_covered()) + (
        diversification_multifunctionality()
        * mean_local_income_per_farm()
        * max_improvement_per_diversification()
    )


def decreasing_income_per_farm():
    """
    Real Name: decreasing_income_per_farm
    Original Eqn: mean_local_income_per_farm/technical_obsolescence_time
    Units: €/farm/Years
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return mean_local_income_per_farm() / technical_obsolescence_time()


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
    Original Eqn: aging_1* (VT_centers_accessibility/5)* DELAY1(vocational_training_campaign, years_for_education_campaign)
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return aging_1() * (vt_centers_accessibility() / 5) * _delayn_entering_vt()


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
    Original Eqn: aging_1* (University_Accessibility/5)* DELAY1(students_university_campaign, years_for_education_campaign)
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return aging_1() * (university_accessibility() / 5) * _delayn_entering_university()


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


def creation_of_primary_jobs():
    """
    Real Name: creation_of_primary_jobs
    Original Eqn: endogenous_primary_job_creation_ratio
    Units: job/Years
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return endogenous_primary_job_creation_ratio()


def destruction_of_primary_jobs():
    """
    Real Name: destruction_of_primary_jobs
    Original Eqn: (endogenous_primary_job_creation_ratio*(1-primary_jobs_viability_ratio))+(Rest_of_primary_sector_jobs/average_life_of_a_primary_sector_business)
    Units: job/Years
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        endogenous_primary_job_creation_ratio() * (1 - primary_jobs_viability_ratio())
    ) + (rest_of_primary_sector_jobs() / average_life_of_a_primary_sector_business())


def creation_of_industrial_jobs():
    """
    Real Name: creation_of_industrial_jobs
    Original Eqn: endogenous_industrial_job_creation_ratio
    Units: job/Years
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return endogenous_industrial_job_creation_ratio()


def destruction_of_industrial_jobs():
    """
    Real Name: destruction_of_industrial_jobs
    Original Eqn: (Industrial_jobs/resulting_average_life_for_industrial_business)+ (endogenous_industrial_job_creation_ratio*(1-new_industrial_job_viability_ratio))
    Units: job/Years
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (industrial_jobs() / resulting_average_life_for_industrial_business()) + (
        endogenous_industrial_job_creation_ratio()
        * (1 - new_industrial_job_viability_ratio())
    )


def creation_of_services_jobs():
    """
    Real Name: creation_of_services_jobs
    Original Eqn: endogenous_service_jobs_creation_ratio
    Units: job/Years
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return endogenous_service_jobs_creation_ratio()


def destruction_of_services_jobs():
    """
    Real Name: destruction_of_services_jobs
    Original Eqn: (service_jobs/resulting_average_life_for_services)+ STEP((endogenous_service_jobs_creation_ratio*(1-new_services_viability_ratio)), 2015)
    Units: job/Years
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (service_jobs() / resulting_average_life_for_services()) + step(
        __data["time"],
        (
            endogenous_service_jobs_creation_ratio()
            * (1 - new_services_viability_ratio())
        ),
        2015,
    )


def change_in_population_services():
    """
    Real Name: change_in_population_services
    Original Eqn: Difference_of_population*ratio_population_services
    Units: job/Years
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return difference_of_population() * ratio_population_services()


_delayn_natural_capital_net_variation = DelayN(
    lambda: natural_land_variation(),
    lambda: years_for_completing_natural_land_objective(),
    lambda: natural_land_variation(),
    lambda: 1,
    time_step,
    "_delayn_natural_capital_net_variation",
)


def natural_capital_net_variation():
    """
    Real Name: natural_capital_net_variation
    Original Eqn: DELAY1(natural_land_variation, years_for_completing_natural_land_objective)+ (Natural_Capital*effect_of_tourism_on_natural_capital)+ effect_of_agriculture_on_Natural_Capital
    Units: ha/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        _delayn_natural_capital_net_variation()
        + (natural_capital() * effect_of_tourism_on_natural_capital())
        + effect_of_agriculture_on_natural_capital()
    )


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
    Original Eqn: working_age_net_migration*0.5*fertility_rate*2/3*1/10
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return working_age_net_migration() * 0.5 * fertility_rate() * 2 / 3 * 1 / 10


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
    Original Eqn: elderly_move_rural- (ELDERLY_POPULATION*elderly_leaving_ratio_1)
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return elderly_move_rural() - (elderly_population() * elderly_leaving_ratio_1())


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
    Original Eqn: working_age_net_migration*0.5*fertility_rate/3*1/5
    Units: person/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return working_age_net_migration() * 0.5 * fertility_rate() / 3 * 1 / 5


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


def building_mobility_infrastructures():
    """
    Real Name: building_mobility_infrastructures
    Original Eqn: MIN (max_km_year_infrastructures, mobility_infrastructures_depletion+ STEP(infrastructure_campaign, year_initiating_infrastructures_plan)- STEP(infrastructure_campaign, year_initiating_infrastructures_plan+time_for_infrastructure_campaign_extension))
    Units: km/Years
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return min(
        max_km_year_infrastructures(),
        mobility_infrastructures_depletion()
        + step(
            __data["time"],
            infrastructure_campaign(),
            year_initiating_infrastructures_plan(),
        )
        - step(
            __data["time"],
            infrastructure_campaign(),
            year_initiating_infrastructures_plan()
            + time_for_infrastructure_campaign_extension(),
        ),
    )


def mobility_infrastructures_depletion():
    """
    Real Name: mobility_infrastructures_depletion
    Original Eqn: mobility_infrastructures/infrastructures_depletion_time
    Units: km/Years
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return mobility_infrastructures() / infrastructures_depletion_time()


def building_infrastructure():
    """
    Real Name: building_infrastructure
    Original Eqn: broadband_infrastructure_depletion+ STEP (broadband_campaign, year_initiating_broadband_plan)
    Units: dmnl/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return broadband_infrastructure_depletion() + step(
        __data["time"], broadband_campaign(), year_initiating_broadband_plan()
    )


def broadband_infrastructure_depletion():
    """
    Real Name: broadband_infrastructure_depletion
    Original Eqn: broadband_infrastructure_population_covered/broadband_infrastructures_depletion_time
    Units: dmnl/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        broadband_infrastructure_population_covered()
        / broadband_infrastructures_depletion_time()
    )


def creating_potential_initiatives():
    """
    Real Name: creating_potential_initiatives
    Original Eqn: effect_of_social_innovation_in_creating_initiatives_ratio*effect_of_broadband_in_creating_potential_initiatives*WORKING_AGE_POPULATION
    Units: initiative/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        effect_of_social_innovation_in_creating_initiatives_ratio()
        * effect_of_broadband_in_creating_potential_initiatives()
        * working_age_population()
    )


def planning_initiatives():
    """
    Real Name: planning_initiatives
    Original Eqn: potential_initiatives*institutional_support
    Units: initiative/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return potential_initiatives() * institutional_support()


def dismissing_potential_initiatives():
    """
    Real Name: dismissing_potential_initiatives
    Original Eqn: potential_initiatives/potential_initiatives_active_time
    Units: initiative/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return potential_initiatives() / potential_initiatives_active_time()


def becoming_stablished_jobs():
    """
    Real Name: becoming_stablished_jobs
    Original Eqn: implemented_initiatives/time_to_implement_initiatives
    Units: initiative/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return implemented_initiatives() / time_to_implement_initiatives()


def building_shared_knowledge():
    """
    Real Name: building_shared_knowledge
    Original Eqn: community_activity_and_networks/time_to_build_effective_shared_knowledge
    Units: dmnl/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        community_activity_and_networks() / time_to_build_effective_shared_knowledge()
    )


def shared_knowledge_loss():
    """
    Real Name: shared_knowledge_loss
    Original Eqn: shared_knowledge/shared_knowledge_loss_time
    Units: dmnl/year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return shared_knowledge() / shared_knowledge_loss_time()


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


def mean_local_income_per_farm():
    """
    Real Name: mean_local_income_per_farm
    Original Eqn: improving_income_per_farm - decreasing_income_per_farm
    Units: €/farm
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_mean_local_income_per_farm()


_integ_mean_local_income_per_farm = Integ(
    lambda: improving_income_per_farm() - decreasing_income_per_farm(),
    lambda: initial_mean_income_per_farm(),
    "_integ_mean_local_income_per_farm",
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
    lambda: 5462 * 3 * 0.46,
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
    lambda: 5462 * 5 * 0.36,
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
    lambda: 5462 * 50 * 0.41,
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
    lambda: 2512 * 42,
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
    lambda: 1966 * 40,
    "_integ_graduated_professionals",
)


def rest_of_primary_sector_jobs():
    """
    Real Name: Rest_of_primary_sector_jobs
    Original Eqn: creation_of_primary_jobs - destruction_of_primary_jobs
    Units: job
    Limits: (None, None)
    Type: component
    Subs: None

    aprox 2%
    """
    return _integ_rest_of_primary_sector_jobs()


_integ_rest_of_primary_sector_jobs = Integ(
    lambda: creation_of_primary_jobs() - destruction_of_primary_jobs(),
    lambda: 20000,
    "_integ_rest_of_primary_sector_jobs",
)


def industrial_jobs():
    """
    Real Name: Industrial_jobs
    Original Eqn: creation_of_industrial_jobs - destruction_of_industrial_jobs
    Units: job
    Limits: (None, None)
    Type: component
    Subs: None

    25% total - 4% (agriindustry) = 21%
    """
    return _integ_industrial_jobs()


_integ_industrial_jobs = Integ(
    lambda: creation_of_industrial_jobs() - destruction_of_industrial_jobs(),
    lambda: 52700,
    "_integ_industrial_jobs",
)


def service_jobs():
    """
    Real Name: service_jobs
    Original Eqn: creation_of_services_jobs - destruction_of_services_jobs
    Units: job
    Limits: (None, None)
    Type: component
    Subs: None

    total 68% - 2% (agriservices) - 10% (population) = 56%
    """
    return _integ_service_jobs()


_integ_service_jobs = Integ(
    lambda: creation_of_services_jobs() - destruction_of_services_jobs(),
    lambda: (103400 - 50500) * 0.75,
    "_integ_service_jobs",
)


def population_services():
    """
    Real Name: population_services
    Original Eqn: change_in_population_services
    Units: job
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_population_services()


_integ_population_services = Integ(
    lambda: change_in_population_services(),
    lambda: (103400 - 50500) * 0.25,
    "_integ_population_services",
)


def natural_capital():
    """
    Real Name: Natural_Capital
    Original Eqn: natural_capital_net_variation
    Units: ha
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_natural_capital()


_integ_natural_capital = Integ(
    lambda: natural_capital_net_variation(),
    lambda: initial_natural_land() - 1160,
    "_integ_natural_capital",
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
    lambda: 54620,
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
    lambda: 300270,
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
    lambda: 89275,
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
    lambda: 56209,
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
    lambda: 26539,
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
    lambda: 15000,
    "_integ_newcomers",
)


def mobility_infrastructures():
    """
    Real Name: mobility_infrastructures
    Original Eqn: building_mobility_infrastructures - mobility_infrastructures_depletion
    Units: km
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_mobility_infrastructures()


_integ_mobility_infrastructures = Integ(
    lambda: building_mobility_infrastructures() - mobility_infrastructures_depletion(),
    lambda: initial_mobility_infrastructures(),
    "_integ_mobility_infrastructures",
)


def broadband_infrastructure_population_covered():
    """
    Real Name: broadband_infrastructure_population_covered
    Original Eqn: building_infrastructure - broadband_infrastructure_depletion
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None

    Expressed in % (50 for 50%)
    """
    return _integ_broadband_infrastructure_population_covered()


_integ_broadband_infrastructure_population_covered = Integ(
    lambda: building_infrastructure() - broadband_infrastructure_depletion(),
    lambda: initial_population_covered(),
    "_integ_broadband_infrastructure_population_covered",
)


def potential_initiatives():
    """
    Real Name: potential_initiatives
    Original Eqn: creating_potential_initiatives - planning_initiatives - dismissing_potential_initiatives
    Units: initiative
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_potential_initiatives()


_integ_potential_initiatives = Integ(
    lambda: creating_potential_initiatives()
    - planning_initiatives()
    - dismissing_potential_initiatives(),
    lambda: 3000,
    "_integ_potential_initiatives",
)


def implemented_initiatives():
    """
    Real Name: implemented_initiatives
    Original Eqn: planning_initiatives - becoming_stablished_jobs
    Units: initiative
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_implemented_initiatives()


_integ_implemented_initiatives = Integ(
    lambda: planning_initiatives() - becoming_stablished_jobs(),
    lambda: 780,
    "_integ_implemented_initiatives",
)


def shared_knowledge():
    """
    Real Name: shared_knowledge
    Original Eqn: building_shared_knowledge - shared_knowledge_loss
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_shared_knowledge()


_integ_shared_knowledge = Integ(
    lambda: building_shared_knowledge() - shared_knowledge_loss(),
    lambda: 5,
    "_integ_shared_knowledge",
)
