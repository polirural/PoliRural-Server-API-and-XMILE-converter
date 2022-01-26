"""
Python model 'vidzeme-combined.py'
Translated using PySD
"""


from pysd.py_backend.functions import lookup, if_then_else
from pysd.py_backend.statefuls import Integ

__pysd_version__ = "2.0.0-dev"

__data = {"scope": None, "time": lambda: 0}

_subscript_dict = {}

_namespace = {
    "TIME": "time",
    "Time": "time",
    "time": "time",
    "initial_farms'_average_size": "initial_farms_average_size",
    "current_agricultural_land": "current_agricultural_land",
    "maximum_agricultural_land": "maximum_agricultural_land",
    "average_environmental_permissions_denials": "average_environmental_permissions_denials",
    "arable_land_farms_profitability": "arable_land_farms_profitability",
    "new_uses_ratio": "new_uses_ratio",
    "agricultural_land_availability": "agricultural_land_availability",
    "intensive_farms_profitability": "intensive_farms_profitability",
    "arable_land": "arable_land",
    "energy_prize_index": "energy_prize_index",
    "energy_prize_effect_on_profitability": "energy_prize_effect_on_profitability",
    "CAP_direct_payments_evolution": "cap_direct_payments_evolution",
    "Eco-schemes_evolution": "ecoschemes_evolution",
    "CAP_effect_on_arable_land_farms_profitability": "cap_effect_on_arable_land_farms_profitability",
    "CAP_effect_on_intensive_farm_profitability": "cap_effect_on_intensive_farm_profitability",
    "size_effect_on_profitability": "size_effect_on_profitability",
    "retirement_ratio": "retirement_ratio",
    "access_to_newcomers": "access_to_newcomers",
    "time_before_abandonment": "time_before_abandonment",
    "intensive_farm_land": "intensive_farm_land",
    "max_transformation_per_year": "max_transformation_per_year",
    "farms_average_size": "farms_average_size",
    "arable_land_farms": "arable_land_farms",
    "arable_land_standby_farms": "arable_land_standby_farms",
    "converted_farms": "converted_farms",
    "intensive_farms": "intensive_farms",
    "intensive_standby_farms": "intensive_standby_farms",
    "arable_land_farms_average_size": "arable_land_farms_average_size",
    "intensive_farm_average_size": "intensive_farm_average_size",
    "increasing_arable_land_farms": "increasing_arable_land_farms",
    "retirement_+_abandonment": "retirement__abandonment",
    "arable_land_abandonment": "arable_land_abandonment",
    "arable_land_new_owners": "arable_land_new_owners",
    "new_uses": "new_uses",
    "to_other_farm_owners": "to_other_farm_owners",
    "increasing_intensive_farms": "increasing_intensive_farms",
    "intensive_farms_abandonment": "intensive_farms_abandonment",
    "new_uses_2": "new_uses_2",
    "intensive_farms_retirement_+_abandonment": "intensive_farms_retirement__abandonment",
    "to_other_intensive_farms_owners": "to_other_intensive_farms_owners",
    "intensive_farm_new_owners": "intensive_farm_new_owners",
    "increasing_average_size": "increasing_average_size",
    "increasing_intensive_farm_size": "increasing_intensive_farm_size",
}

_dependencies = {
    "initial_farms_average_size": {},
    "current_agricultural_land": {"arable_land": 1, "intensive_farm_land": 1},
    "maximum_agricultural_land": {},
    "average_environmental_permissions_denials": {},
    "arable_land_farms_profitability": {
        "size_effect_on_profitability": 1,
        "cap_effect_on_arable_land_farms_profitability": 1,
    },
    "new_uses_ratio": {},
    "agricultural_land_availability": {
        "maximum_agricultural_land": 1,
        "current_agricultural_land": 1,
    },
    "intensive_farms_profitability": {
        "energy_prize_effect_on_profitability": 1,
        "cap_effect_on_intensive_farm_profitability": 1,
    },
    "arable_land": {"arable_land_farms": 1, "arable_land_farms_average_size": 1},
    "energy_prize_index": {"time": 1},
    "energy_prize_effect_on_profitability": {"energy_prize_index": 1},
    "cap_direct_payments_evolution": {"time": 1},
    "ecoschemes_evolution": {"time": 1},
    "cap_effect_on_arable_land_farms_profitability": {
        "cap_direct_payments_evolution": 1,
        "ecoschemes_evolution": 1,
    },
    "cap_effect_on_intensive_farm_profitability": {
        "ecoschemes_evolution": 1,
        "cap_direct_payments_evolution": 1,
    },
    "size_effect_on_profitability": {"arable_land_farms_average_size": 1},
    "retirement_ratio": {"time": 1},
    "access_to_newcomers": {},
    "time_before_abandonment": {},
    "intensive_farm_land": {"intensive_farms": 1, "intensive_farm_average_size": 1},
    "max_transformation_per_year": {},
    "farms_average_size": {
        "arable_land_farms_average_size": 1,
        "intensive_farm_average_size": 1,
    },
    "increasing_arable_land_farms": {
        "arable_land_farms_profitability": 2,
        "agricultural_land_availability": 2,
        "intensive_farms_profitability": 1,
        "max_transformation_per_year": 1,
        "arable_land_farms_average_size": 1,
    },
    "retirement__abandonment": {
        "arable_land_farms_profitability": 2,
        "retirement_ratio": 2,
        "arable_land_farms": 3,
        "max_transformation_per_year": 1,
    },
    "arable_land_abandonment": {
        "arable_land_standby_farms": 1,
        "time_before_abandonment": 1,
    },
    "arable_land_new_owners": {
        "arable_land_farms_profitability": 1,
        "retirement__abandonment": 1,
        "access_to_newcomers": 1,
        "average_environmental_permissions_denials": 1,
    },
    "new_uses": {
        "arable_land_farms_profitability": 1,
        "arable_land_standby_farms": 1,
        "new_uses_ratio": 1,
    },
    "to_other_farm_owners": {
        "arable_land_farms_profitability": 1,
        "arable_land_standby_farms": 1,
        "max_transformation_per_year": 1,
    },
    "increasing_intensive_farms": {
        "agricultural_land_availability": 2,
        "intensive_farms_profitability": 2,
        "arable_land_farms_profitability": 1,
        "max_transformation_per_year": 1,
        "intensive_farm_average_size": 1,
    },
    "intensive_farms_abandonment": {
        "intensive_standby_farms": 1,
        "time_before_abandonment": 1,
    },
    "new_uses_2": {
        "intensive_farms_profitability": 1,
        "intensive_standby_farms": 1,
        "new_uses_ratio": 1,
    },
    "intensive_farms_retirement__abandonment": {
        "intensive_farms_profitability": 2,
        "intensive_farms": 3,
        "retirement_ratio": 2,
        "max_transformation_per_year": 1,
    },
    "to_other_intensive_farms_owners": {
        "intensive_farms_profitability": 2,
        "intensive_standby_farms": 1,
        "max_transformation_per_year": 1,
    },
    "intensive_farm_new_owners": {
        "intensive_farms_profitability": 1,
        "intensive_farms_retirement__abandonment": 1,
        "average_environmental_permissions_denials": 1,
        "access_to_newcomers": 1,
    },
    "increasing_average_size": {
        "to_other_farm_owners": 1,
        "arable_land_farms_average_size": 1,
        "arable_land_farms": 1,
    },
    "increasing_intensive_farm_size": {
        "to_other_intensive_farms_owners": 1,
        "intensive_farm_average_size": 1,
        "intensive_farms": 1,
    },
    "arable_land_farms": {"_integ_arable_land_farms": 1},
    "_integ_arable_land_farms": {
        "initial": {},
        "step": {
            "increasing_arable_land_farms": 1,
            "arable_land_new_owners": 1,
            "retirement__abandonment": 1,
        },
    },
    "arable_land_standby_farms": {"_integ_arable_land_standby_farms": 1},
    "_integ_arable_land_standby_farms": {
        "initial": {},
        "step": {
            "retirement__abandonment": 1,
            "arable_land_abandonment": 1,
            "arable_land_new_owners": 1,
            "new_uses": 1,
            "to_other_farm_owners": 1,
        },
    },
    "converted_farms": {"_integ_converted_farms": 1},
    "_integ_converted_farms": {"initial": {}, "step": {"new_uses": 1, "new_uses_2": 1}},
    "intensive_farms": {"_integ_intensive_farms": 1},
    "_integ_intensive_farms": {
        "initial": {},
        "step": {
            "increasing_intensive_farms": 1,
            "intensive_farm_new_owners": 1,
            "intensive_farms_retirement__abandonment": 1,
        },
    },
    "intensive_standby_farms": {"_integ_intensive_standby_farms": 1},
    "_integ_intensive_standby_farms": {
        "initial": {},
        "step": {
            "intensive_farms_retirement__abandonment": 1,
            "intensive_farms_abandonment": 1,
            "new_uses_2": 1,
            "to_other_intensive_farms_owners": 1,
            "intensive_farm_new_owners": 1,
        },
    },
    "arable_land_farms_average_size": {"_integ_arable_land_farms_average_size": 1},
    "_integ_arable_land_farms_average_size": {
        "initial": {"initial_farms_average_size": 1},
        "step": {"increasing_average_size": 1},
    },
    "intensive_farm_average_size": {"_integ_intensive_farm_average_size": 1},
    "_integ_intensive_farm_average_size": {
        "initial": {"initial_farms_average_size": 1},
        "step": {"increasing_intensive_farm_size": 1},
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
    Units: Year
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
    Units: Year
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
    Units: Year
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
    Units: Year
    Limits: None
    Type: constant
    Subs: None

    The time step for the simulation.
    """
    return __data["time"].saveper()


##########################################################################
#                             MODEL VARIABLES                            #
##########################################################################


def initial_farms_average_size():
    """
    Real Name: initial_farms'_average_size
    Original Eqn: 21.77
    Units: ha/farm
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 21.77


def current_agricultural_land():
    """
    Real Name: current_agricultural_land
    Original Eqn: arable_land+intensive_farm_land
    Units: ha
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return arable_land() + intensive_farm_land()


def maximum_agricultural_land():
    """
    Real Name: maximum_agricultural_land
    Original Eqn: 622738
    Units: ha
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 622738


def average_environmental_permissions_denials():
    """
    Real Name: average_environmental_permissions_denials
    Original Eqn: 0.063
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.063


def arable_land_farms_profitability():
    """
    Real Name: arable_land_farms_profitability
    Original Eqn: (size_effect_on_profitability+CAP_effect_on_arable_land_farms_profitability)/2
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        size_effect_on_profitability() + cap_effect_on_arable_land_farms_profitability()
    ) / 2


def new_uses_ratio():
    """
    Real Name: new_uses_ratio
    Original Eqn: 0.15
    Units: dmnl/year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.15


def agricultural_land_availability():
    """
    Real Name: agricultural_land_availability
    Original Eqn: MAX(0, maximum_agricultural_land-current_agricultural_land)
    Units: ha
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return max(0, maximum_agricultural_land() - current_agricultural_land())


def intensive_farms_profitability():
    """
    Real Name: intensive_farms_profitability
    Original Eqn: energy_prize_effect_on_profitability+CAP_effect_on_intensive_farm_profitability/2
    Units: dmnl
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        energy_prize_effect_on_profitability()
        + cap_effect_on_intensive_farm_profitability() / 2
    )


def arable_land():
    """
    Real Name: arable_land
    Original Eqn: arable_land_farms*arable_land_farms_average_size
    Units: ha
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return arable_land_farms() * arable_land_farms_average_size()


def energy_prize_index(x=None):
    """
    Real Name: energy_prize_index
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
                1.000,
                1.160,
                1.210,
                1.235,
                1.126,
                1.180,
                1.311,
                1.508,
                1.604,
                1.700,
                1.795,
                1.891,
                1.967,
                2.051,
                2.135,
                2.219,
                2.309,
                2.399,
                2.489,
                2.579,
                2.678,
                2.755,
                2.831,
                2.899,
                2.967,
                3.036,
                3.104,
                3.159,
                3.213,
                3.311,
                3.585,
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
                1.000,
                1.160,
                1.210,
                1.235,
                1.126,
                1.180,
                1.311,
                1.508,
                1.604,
                1.700,
                1.795,
                1.891,
                1.967,
                2.051,
                2.135,
                2.219,
                2.309,
                2.399,
                2.489,
                2.579,
                2.678,
                2.755,
                2.831,
                2.899,
                2.967,
                3.036,
                3.104,
                3.159,
                3.213,
                3.311,
                3.585,
            ],
        )
    )


def energy_prize_effect_on_profitability(x=None):
    """
    Real Name: energy_prize_effect_on_profitability
    Original Eqn: energy_prize_index
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            energy_prize_index(),
            [
                0.800,
                0.938,
                1.075,
                1.213,
                1.350,
                1.488,
                1.625,
                1.763,
                1.900,
                2.038,
                2.175,
                2.312,
                2.450,
                2.588,
                2.725,
                2.862,
                3.000,
            ],
            [
                1.200,
                1.004,
                0.840,
                0.702,
                0.588,
                0.491,
                0.411,
                0.344,
                0.288,
                0.241,
                0.201,
                0.168,
                0.141,
                0.118,
                0.099,
                0.082,
                0.069,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                0.800,
                0.938,
                1.075,
                1.213,
                1.350,
                1.488,
                1.625,
                1.763,
                1.900,
                2.038,
                2.175,
                2.312,
                2.450,
                2.588,
                2.725,
                2.862,
                3.000,
            ],
            [
                1.200,
                1.004,
                0.840,
                0.702,
                0.588,
                0.491,
                0.411,
                0.344,
                0.288,
                0.241,
                0.201,
                0.168,
                0.141,
                0.118,
                0.099,
                0.082,
                0.069,
            ],
        )
    )


def cap_direct_payments_evolution(x=None):
    """
    Real Name: CAP_direct_payments_evolution
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
                0.200,
                0.200,
                0.200,
                0.200,
                0.200,
                0.200,
                0.200,
                0.200,
                0.200,
                0.200,
                0.200,
                0.200,
                0.200,
                0.175,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
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
                0.200,
                0.200,
                0.200,
                0.200,
                0.200,
                0.200,
                0.200,
                0.200,
                0.200,
                0.200,
                0.200,
                0.200,
                0.200,
                0.175,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
            ],
        )
    )


def ecoschemes_evolution(x=None):
    """
    Real Name: Eco-schemes_evolution
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
                0.003,
                0.006,
                0.011,
                0.019,
                0.033,
                0.057,
                0.093,
                0.146,
                0.213,
                0.287,
                0.354,
                0.407,
                0.443,
                0.467,
                0.481,
                0.489,
                0.494,
                0.497,
            ],
        )
        if x is None
        else lookup(
            x,
            [
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
                0.003,
                0.006,
                0.011,
                0.019,
                0.033,
                0.057,
                0.093,
                0.146,
                0.213,
                0.287,
                0.354,
                0.407,
                0.443,
                0.467,
                0.481,
                0.489,
                0.494,
                0.497,
            ],
        )
    )


def cap_effect_on_arable_land_farms_profitability(x=None):
    """
    Real Name: CAP_effect_on_arable_land_farms_profitability
    Original Eqn: CAP_direct_payments_evolution+"Eco-schemes_evolution"
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            cap_direct_payments_evolution() + ecoschemes_evolution(),
            [
                0.000,
                0.020,
                0.040,
                0.060,
                0.080,
                0.100,
                0.120,
                0.140,
                0.160,
                0.180,
                0.200,
            ],
            [
                0.000,
                0.285,
                0.493,
                0.643,
                0.753,
                0.832,
                0.890,
                0.932,
                0.962,
                0.984,
                1.000,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                0.000,
                0.020,
                0.040,
                0.060,
                0.080,
                0.100,
                0.120,
                0.140,
                0.160,
                0.180,
                0.200,
            ],
            [
                0.000,
                0.285,
                0.493,
                0.643,
                0.753,
                0.832,
                0.890,
                0.932,
                0.962,
                0.984,
                1.000,
            ],
        )
    )


def cap_effect_on_intensive_farm_profitability(x=None):
    """
    Real Name: CAP_effect_on_intensive_farm_profitability
    Original Eqn: "Eco-schemes_evolution"+CAP_direct_payments_evolution
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            ecoschemes_evolution() + cap_direct_payments_evolution(),
            [
                0.000,
                0.020,
                0.040,
                0.060,
                0.080,
                0.100,
                0.120,
                0.140,
                0.160,
                0.180,
                0.200,
            ],
            [
                0.536,
                0.691,
                0.803,
                0.913,
                0.973,
                1.000,
                1.000,
                1.000,
                1.000,
                1.000,
                1.000,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                0.000,
                0.020,
                0.040,
                0.060,
                0.080,
                0.100,
                0.120,
                0.140,
                0.160,
                0.180,
                0.200,
            ],
            [
                0.536,
                0.691,
                0.803,
                0.913,
                0.973,
                1.000,
                1.000,
                1.000,
                1.000,
                1.000,
                1.000,
            ],
        )
    )


def size_effect_on_profitability(x=None):
    """
    Real Name: size_effect_on_profitability
    Original Eqn: arable_land_farms_average_size
    Units: dmnl
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return (
        lookup(
            arable_land_farms_average_size(),
            [
                0.000,
                10.526,
                21.053,
                31.579,
                42.105,
                52.632,
                63.158,
                73.684,
                84.211,
                94.737,
                105.263,
                115.789,
                126.316,
                136.842,
                147.368,
                157.895,
                168.421,
                178.947,
                189.474,
                200.000,
            ],
            [
                0.000,
                0.713,
                1.002,
                1.120,
                1.167,
                1.187,
                1.195,
                1.198,
                1.199,
                1.200,
                1.200,
                1.200,
                1.200,
                1.200,
                1.200,
                1.200,
                1.200,
                1.200,
                1.200,
                1.200,
            ],
        )
        if x is None
        else lookup(
            x,
            [
                0.000,
                10.526,
                21.053,
                31.579,
                42.105,
                52.632,
                63.158,
                73.684,
                84.211,
                94.737,
                105.263,
                115.789,
                126.316,
                136.842,
                147.368,
                157.895,
                168.421,
                178.947,
                189.474,
                200.000,
            ],
            [
                0.000,
                0.713,
                1.002,
                1.120,
                1.167,
                1.187,
                1.195,
                1.198,
                1.199,
                1.200,
                1.200,
                1.200,
                1.200,
                1.200,
                1.200,
                1.200,
                1.200,
                1.200,
                1.200,
                1.200,
            ],
        )
    )


def retirement_ratio(x=None):
    """
    Real Name: retirement_ratio
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
                0.150,
                0.140,
                0.135,
                0.135,
                0.135,
                0.135,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
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
                0.150,
                0.140,
                0.135,
                0.135,
                0.135,
                0.135,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
                0.150,
            ],
        )
    )


def access_to_newcomers():
    """
    Real Name: access_to_newcomers
    Original Eqn: 0.8
    Units: dmnl
    Limits: (None, None)
    Type: constant
    Subs: None

    this is 0,5 as an example. It could be another value or even be changing in time
    """
    return 0.8


def time_before_abandonment():
    """
    Real Name: time_before_abandonment
    Original Eqn: 4
    Units: year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 4


def intensive_farm_land():
    """
    Real Name: intensive_farm_land
    Original Eqn: intensive_farms*intensive_farm_average_size
    Units: ha
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return intensive_farms() * intensive_farm_average_size()


def max_transformation_per_year():
    """
    Real Name: max_transformation_per_year
    Original Eqn: 0.2
    Units: dmnl/year
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 0.2


def farms_average_size():
    """
    Real Name: farms_average_size
    Original Eqn: (arable_land_farms_average_size*0.73)+(intensive_farm_average_size*0.27)
    Units: ha/farm
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (arable_land_farms_average_size() * 0.73) + (
        intensive_farm_average_size() * 0.27
    )


def increasing_arable_land_farms():
    """
    Real Name: increasing_arable_land_farms
    Original Eqn: IF (arable_land_farms_profitability >=0.9) AND(agricultural_land_availability>0) AND (arable_land_farms_profitability>intensive_farms_profitability) THEN INT(agricultural_land_availability*max_transformation_per_year/arable_land_farms_average_size) ELSE 0
    Units: farm/Year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return if_then_else(
        (arable_land_farms_profitability() >= 0.9)
        and (agricultural_land_availability() > 0)
        and (arable_land_farms_profitability() > intensive_farms_profitability()),
        lambda: int(
            agricultural_land_availability()
            * max_transformation_per_year()
            / arable_land_farms_average_size()
        ),
        lambda: 0,
    )


def retirement__abandonment():
    """
    Real Name: retirement_+_abandonment
    Original Eqn: IF arable_land_farms_profitability>=0.6 THEN retirement_ratio*arable_land_farms ELSE (retirement_ratio*arable_land_farms)+ ((1-arable_land_farms_profitability)*arable_land_farms*max_transformation_per_year)
    Units: farm/Year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return if_then_else(
        arable_land_farms_profitability() >= 0.6,
        lambda: retirement_ratio() * arable_land_farms(),
        lambda: (retirement_ratio() * arable_land_farms())
        + (
            (1 - arable_land_farms_profitability())
            * arable_land_farms()
            * max_transformation_per_year()
        ),
    )


def arable_land_abandonment():
    """
    Real Name: arable_land_abandonment
    Original Eqn: arable_land_standby_farms/time_before_abandonment
    Units: farm/Year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return arable_land_standby_farms() / time_before_abandonment()


def arable_land_new_owners():
    """
    Real Name: arable_land_new_owners
    Original Eqn: IF arable_land_farms_profitability>0.7 THEN "retirement_+_abandonment"* (access_to_newcomers-average_environmental_permissions_denials) ELSE 0
    Units: farm/Year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return if_then_else(
        arable_land_farms_profitability() > 0.7,
        lambda: retirement__abandonment()
        * (access_to_newcomers() - average_environmental_permissions_denials()),
        lambda: 0,
    )


def new_uses():
    """
    Real Name: new_uses
    Original Eqn: IF arable_land_farms_profitability<0.5 THEN arable_land_standby_farms*new_uses_ratio ELSE 0
    Units: farm/Year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return if_then_else(
        arable_land_farms_profitability() < 0.5,
        lambda: arable_land_standby_farms() * new_uses_ratio(),
        lambda: 0,
    )


def to_other_farm_owners():
    """
    Real Name: to_other_farm_owners
    Original Eqn: IF arable_land_farms_profitability>0.5 THEN arable_land_standby_farms*max_transformation_per_year ELSE 0
    Units: farm/Year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return if_then_else(
        arable_land_farms_profitability() > 0.5,
        lambda: arable_land_standby_farms() * max_transformation_per_year(),
        lambda: 0,
    )


def increasing_intensive_farms():
    """
    Real Name: increasing_intensive_farms
    Original Eqn: IF agricultural_land_availability>0 AND (intensive_farms_profitability >=1) AND (intensive_farms_profitability>arable_land_farms_profitability) THEN INT(agricultural_land_availability*max_transformation_per_year/intensive_farm_average_size) ELSE 0
    Units: farm/Year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return if_then_else(
        agricultural_land_availability() > 0
        and (intensive_farms_profitability() >= 1)
        and (intensive_farms_profitability() > arable_land_farms_profitability()),
        lambda: int(
            agricultural_land_availability()
            * max_transformation_per_year()
            / intensive_farm_average_size()
        ),
        lambda: 0,
    )


def intensive_farms_abandonment():
    """
    Real Name: intensive_farms_abandonment
    Original Eqn: intensive_standby_farms/time_before_abandonment
    Units: farm/Year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return intensive_standby_farms() / time_before_abandonment()


def new_uses_2():
    """
    Real Name: new_uses_2
    Original Eqn: IF intensive_farms_profitability<0.7 THEN intensive_standby_farms*new_uses_ratio ELSE 0
    Units: farm/Year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return if_then_else(
        intensive_farms_profitability() < 0.7,
        lambda: intensive_standby_farms() * new_uses_ratio(),
        lambda: 0,
    )


def intensive_farms_retirement__abandonment():
    """
    Real Name: intensive_farms_retirement_+_abandonment
    Original Eqn: IF intensive_farms_profitability>=1 THEN intensive_farms*retirement_ratio ELSE (intensive_farms*retirement_ratio)+ ((1-intensive_farms_profitability)*intensive_farms*max_transformation_per_year)
    Units: farm/Year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return if_then_else(
        intensive_farms_profitability() >= 1,
        lambda: intensive_farms() * retirement_ratio(),
        lambda: (intensive_farms() * retirement_ratio())
        + (
            (1 - intensive_farms_profitability())
            * intensive_farms()
            * max_transformation_per_year()
        ),
    )


def to_other_intensive_farms_owners():
    """
    Real Name: to_other_intensive_farms_owners
    Original Eqn: IF intensive_farms_profitability>0.7 AND intensive_farms_profitability<0.9 THEN intensive_standby_farms*max_transformation_per_year ELSE 0
    Units: farm/Year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return if_then_else(
        intensive_farms_profitability() > 0.7 and intensive_farms_profitability() < 0.9,
        lambda: intensive_standby_farms() * max_transformation_per_year(),
        lambda: 0,
    )


def intensive_farm_new_owners():
    """
    Real Name: intensive_farm_new_owners
    Original Eqn: IF intensive_farms_profitability>0.9 THEN "intensive_farms_retirement_+_abandonment"* (1-average_environmental_permissions_denials)* access_to_newcomers ELSE 0
    Units: farm/Year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return if_then_else(
        intensive_farms_profitability() > 0.9,
        lambda: intensive_farms_retirement__abandonment()
        * (1 - average_environmental_permissions_denials())
        * access_to_newcomers(),
        lambda: 0,
    )


def increasing_average_size():
    """
    Real Name: increasing_average_size
    Original Eqn: to_other_farm_owners*arable_land_farms_average_size/arable_land_farms
    Units: ha/farm/Year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        to_other_farm_owners() * arable_land_farms_average_size() / arable_land_farms()
    )


def increasing_intensive_farm_size():
    """
    Real Name: increasing_intensive_farm_size
    Original Eqn: to_other_intensive_farms_owners*intensive_farm_average_size/intensive_farms
    Units: ha/farm/Year
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return (
        to_other_intensive_farms_owners()
        * intensive_farm_average_size()
        / intensive_farms()
    )


def arable_land_farms():
    """
    Real Name: arable_land_farms
    Original Eqn: increasing_arable_land_farms + arable_land_new_owners - "retirement_+_abandonment"
    Units: farm
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_arable_land_farms()


_integ_arable_land_farms = Integ(
    lambda: increasing_arable_land_farms()
    + arable_land_new_owners()
    - retirement__abandonment(),
    lambda: 10416,
    "_integ_arable_land_farms",
)


def arable_land_standby_farms():
    """
    Real Name: arable_land_standby_farms
    Original Eqn: "retirement_+_abandonment" - arable_land_abandonment - arable_land_new_owners - new_uses - to_other_farm_owners
    Units: farm
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_arable_land_standby_farms()


_integ_arable_land_standby_farms = Integ(
    lambda: retirement__abandonment()
    - arable_land_abandonment()
    - arable_land_new_owners()
    - new_uses()
    - to_other_farm_owners(),
    lambda: 10416 * 0.15,
    "_integ_arable_land_standby_farms",
)


def converted_farms():
    """
    Real Name: converted_farms
    Original Eqn: new_uses + new_uses_2
    Units: farm
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_converted_farms()


_integ_converted_farms = Integ(
    lambda: new_uses() + new_uses_2(),
    lambda: 10416 * 0.15 * 0.15,
    "_integ_converted_farms",
)


def intensive_farms():
    """
    Real Name: intensive_farms
    Original Eqn: increasing_intensive_farms + intensive_farm_new_owners - "intensive_farms_retirement_+_abandonment"
    Units: farm
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_intensive_farms()


_integ_intensive_farms = Integ(
    lambda: increasing_intensive_farms()
    + intensive_farm_new_owners()
    - intensive_farms_retirement__abandonment(),
    lambda: 17915,
    "_integ_intensive_farms",
)


def intensive_standby_farms():
    """
    Real Name: intensive_standby_farms
    Original Eqn: "intensive_farms_retirement_+_abandonment" - intensive_farms_abandonment - new_uses_2 - to_other_intensive_farms_owners - intensive_farm_new_owners
    Units: farm
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_intensive_standby_farms()


_integ_intensive_standby_farms = Integ(
    lambda: intensive_farms_retirement__abandonment()
    - intensive_farms_abandonment()
    - new_uses_2()
    - to_other_intensive_farms_owners()
    - intensive_farm_new_owners(),
    lambda: 17915 * 0.15,
    "_integ_intensive_standby_farms",
)


def arable_land_farms_average_size():
    """
    Real Name: arable_land_farms_average_size
    Original Eqn: increasing_average_size
    Units: ha/farm
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_arable_land_farms_average_size()


_integ_arable_land_farms_average_size = Integ(
    lambda: increasing_average_size(),
    lambda: initial_farms_average_size(),
    "_integ_arable_land_farms_average_size",
)


def intensive_farm_average_size():
    """
    Real Name: intensive_farm_average_size
    Original Eqn: increasing_intensive_farm_size
    Units: ha/farm
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_intensive_farm_average_size()


_integ_intensive_farm_average_size = Integ(
    lambda: increasing_intensive_farm_size(),
    lambda: initial_farms_average_size(),
    "_integ_intensive_farm_average_size",
)
