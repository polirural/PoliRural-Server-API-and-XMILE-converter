"""
Python model 'test_p.py'
Translated using PySD
"""


from pysd.py_backend.functions import ramp, lookup, step
from pysd.py_backend.statefuls import Initial, Smooth, Integ, DelayN

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
    "farm_to_fork_effect_on_services": "farm_to_fork_effect_on_services",
    "CAP_Eco-Schemes": "cap_ecoschemes",
    "farming_attraction_factor": "farming_attraction_factor",
    "farm_to_fork_effect_on_industry": "farm_to_fork_effect_on_industry",
    "related_agricultural_jobs_on_industry": "related_agricultural_jobs_on_industry",
    "social_capital": "social_capital",
    "social_innovation_/_potential_initiatives": "social_innovation__potential_initiatives",
    "average_farm_area": "average_farm_area",
    "agricultural_land": "agricultural_land",
    "agriculture_profitability": "agriculture_profitability",
    "CAP_direct_payment": "cap_direct_payment",
    "agriculture_jobs": "agriculture_jobs",
    "tourist_visitors": "tourist_visitors",
    "total_rural_population": "total_rural_population",
    "effect_of_tourism_on_diversification": "effect_of_tourism_on_diversification",
    "AKIS_effect": "akis_effect",
    "CAP_reform_direct_payments_decrease_2021": "cap_reform_direct_payments_decrease_2021",
    "CAP_mean_proportion_of_direct_payment_to_FNVA": "cap_mean_proportion_of_direct_payment_to_fnva",
    "Eco-schemes_effect_on_direct_payment": "ecoschemes_effect_on_direct_payment",
    "initial_mean_income_per_farm": "initial_mean_income_per_farm",
    "technical_obsolescence_time": "technical_obsolescence_time",
    "agricultural_obsolescence_covered": "agricultural_obsolescence_covered",
    "mean_jobs_per_farm": "mean_jobs_per_farm",
    "max_mean_related_agri_jobs_on_services": "max_mean_related_agri_jobs_on_services",
    "max_mean_related_agri_jobs_on_industry": "max_mean_related_agri_jobs_on_industry",
    "max_improvement_per_diversification": "max_improvement_per_diversification",
    "attraction_ratio_for_tourists": "attraction_ratio_for_tourists",
    "initial_number_of_farms": "initial_number_of_farms",
    "final_technical_obsolescence_time": "final_technical_obsolescence_time",
    "time_for_slope": "time_for_slope",
    "normal_technical_obsolescence_time": "normal_technical_obsolescence_time",
    "AKIS_evolution": "akis_evolution",
    "related_agricultural_jobs_effect_on_services": "related_agricultural_jobs_effect_on_services",
    "farms": "farms",
    "mean_local_income_per_farm": "mean_local_income_per_farm",
    "increasing_farms": "increasing_farms",
    "decreasing_farms": "decreasing_farms",
    "improving_income_per_farm": "improving_income_per_farm",
    "decreasing_income_per_farm": "decreasing_income_per_farm",
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
    "farm_to_fork_effect_on_services": {"time": 1},
    "cap_ecoschemes": {"time": 1},
    "farming_attraction_factor": {"land_access": 1, "agriculture_profitability": 1},
    "farm_to_fork_effect_on_industry": {"time": 1},
    "related_agricultural_jobs_on_industry": {
        "farms": 1,
        "max_mean_related_agri_jobs_on_industry": 1,
        "farm_to_fork_effect_on_industry": 1,
        "time": 1,
        "akis_effect": 1,
    },
    "social_capital": {"time": 1},
    "social_innovation__potential_initiatives": {},
    "average_farm_area": {},
    "agricultural_land": {"farms": 1, "average_farm_area": 1},
    "agriculture_profitability": {
        "mean_local_income_per_farm": 1,
        "cap_direct_payment": 1,
    },
    "cap_direct_payment": {
        "cap_mean_proportion_of_direct_payment_to_fnva": 1,
        "cap_reform_direct_payments_decrease_2021": 1,
        "time": 2,
        "ecoschemes_effect_on_direct_payment": 1,
    },
    "agriculture_jobs": {"farms": 1, "jobs_per_farm": 1},
    "tourist_visitors": {},
    "total_rural_population": {},
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
    "mean_jobs_per_farm": {},
    "max_mean_related_agri_jobs_on_services": {},
    "max_mean_related_agri_jobs_on_industry": {},
    "max_improvement_per_diversification": {},
    "attraction_ratio_for_tourists": {},
    "initial_number_of_farms": {},
    "final_technical_obsolescence_time": {},
    "time_for_slope": {},
    "normal_technical_obsolescence_time": {},
    "akis_evolution": {"time": 1},
    "related_agricultural_jobs_effect_on_services": {
        "farms": 1,
        "max_mean_related_agri_jobs_on_services": 1,
        "cap_ecoschemes": 1,
        "farm_to_fork_effect_on_services": 1,
        "time": 1,
        "akis_effect": 1,
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
            [0.000, 11250.000, 22500.000, 33750.000, 45000.000],
            [0.993, 0.924, 0.500, 0.076, 0.007],
        )
        if x is None
        else lookup(
            x,
            [0.000, 11250.000, 22500.000, 33750.000, 45000.000],
            [0.993, 0.924, 0.500, 0.076, 0.007],
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
                0.001,
                0.003,
                0.013,
                0.053,
                0.192,
                0.500,
                0.808,
                0.947,
                0.987,
                0.997,
                0.999,
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
                0.001,
                0.003,
                0.013,
                0.053,
                0.192,
                0.500,
                0.808,
                0.947,
                0.987,
                0.997,
                0.999,
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
    Original Eqn: 50000
    Units: ha
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 50000


def potential_land_transformation():
    """
    Real Name: potential_land_transformation
    Original Eqn: max_agricultural_land-agricultural_land
    Units: ha
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return max_agricultural_land() - agricultural_land()


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


def farm_to_fork_effect_on_services(x=None):
    """
    Real Name: farm_to_fork_effect_on_services
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


def farm_to_fork_effect_on_industry(x=None):
    """
    Real Name: farm_to_fork_effect_on_industry
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


def related_agricultural_jobs_on_industry():
    """
    Real Name: related_agricultural_jobs_on_industry
    Original Eqn: (farms/max_mean_related_agri_jobs_on_industry)*MAX(1, STEP (farm_to_fork_effect_on_industry/4, 2021))*AKIS_effect
    Units: job
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        (farms() / max_mean_related_agri_jobs_on_industry())
        * max(1, step(__data["time"], farm_to_fork_effect_on_industry() / 4, 2021))
        * akis_effect()
    )


def social_capital(x=None):
    """
    Real Name: social_capital
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


def social_innovation__potential_initiatives():
    """
    Real Name: social_innovation_/_potential_initiatives
    Original Eqn: {Enter equation for use when not hooked up to other models}00
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 00


def average_farm_area():
    """
    Real Name: average_farm_area
    Original Eqn: 23
    Units: ha/farm
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 23


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
    Original Eqn: mean_local_income_per_farm*(1+CAP_direct_payment)
    Units: â‚¬/farm
    Limits: (None, None)
    Type: component
    Subs: None

    0 - 105 aprox

    """
    return mean_local_income_per_farm() * (1 + cap_direct_payment())


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


def tourist_visitors():
    """
    Real Name: tourist_visitors
    Original Eqn: {Enter equation for use when not hooked up to other models}0
    Units: person/year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0


def total_rural_population():
    """
    Real Name: total_rural_population
    Original Eqn: {Enter equation for use when not hooked up to other models}0
    Units: person
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0


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
    Original Eqn: 0.3
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None

    FNVA farm net value added
    """
    return 0.3


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
    Original Eqn: 35000
    Units: â‚¬/farm
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 35000


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


def mean_jobs_per_farm():
    """
    Real Name: mean_jobs_per_farm
    Original Eqn: 1.5
    Units: job/farm
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 1.5


def max_mean_related_agri_jobs_on_services():
    """
    Real Name: max_mean_related_agri_jobs_on_services
    Original Eqn: 10
    Units: farm/job
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 10


def max_mean_related_agri_jobs_on_industry():
    """
    Real Name: max_mean_related_agri_jobs_on_industry
    Original Eqn: 5
    Units: farm/job
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 5


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


def attraction_ratio_for_tourists():
    """
    Real Name: attraction_ratio_for_tourists
    Original Eqn: 0.5
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.5


def initial_number_of_farms():
    """
    Real Name: initial_number_of_farms
    Original Eqn: 506
    Units: farm
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 506


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


def normal_technical_obsolescence_time():
    """
    Real Name: normal_technical_obsolescence_time
    Original Eqn: 7
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 7


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


def related_agricultural_jobs_effect_on_services():
    """
    Real Name: related_agricultural_jobs_effect_on_services
    Original Eqn: (farms/max_mean_related_agri_jobs_on_services)*MAX(1, STEP(("CAP_Eco-Schemes"+farm_to_fork_effect_on_services)/8, 2021))*AKIS_effect
    Units: job
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        (farms() / max_mean_related_agri_jobs_on_services())
        * max(
            1,
            step(
                __data["time"],
                (cap_ecoschemes() + farm_to_fork_effect_on_services()) / 8,
                2021,
            ),
        )
        * akis_effect()
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
    Units: â‚¬/farm/Years
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
    Units: â‚¬/farm/Years
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return mean_local_income_per_farm() / technical_obsolescence_time()


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
    Units: â‚¬/farm
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
