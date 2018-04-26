import numpy as np
from collections import namedtuple

# Authorship -----------------------------------------------------------------------------#
__author__      = ["Geoffrey Hyde Garrett", "Vladimir"]
__copyright__   = None
__credits__     = None
__license__     = "MIT"
__version__     = "1.0.0"
__maintainer__  = ["Geoffrey Hyde Garrett", "Vladimir"]
__email__       = ["g.h.garrett13@gmail.com", "vladifm97@gmail.com"]
__status__      = "Development"


def _total_power(p_pl_peak):
    return 332.93 * np.log(p_pl_peak) - 1047


def _circular_orbit_time(radius_planet, altitude, gravitational_constant_gm):
    return 2 * np.pi * np.sqrt((radius_planet + altitude) ** 3 / gravitational_constant_gm)


def _circular_eclipse_time(_circular_orbit_time, altitude, radius_planet):
    return (_circular_orbit_time / np.pi) * np.arcsin(1 / (1 + (altitude / radius_planet)))


def _circular_non_eclipse_time(_circular_orbit_time, _circular_eclipse_time):
    return _circular_orbit_time - _circular_eclipse_time


def _power_solar_array(p_e, p_d, t_e, t_d, peak_power_tracking):
    if peak_power_tracking is True:
        x_e = 0.6
        x_d = 0.8
    else:
        x_e = 0.65
        x_d = 0.85
    print(x_e, x_d)
    return ((t_e * p_e / x_e) + (t_d * p_d / x_d)) / t_d


def _square_meter_power_solar_cell(solar_irradiance, efficiency):
    return solar_irradiance * efficiency / 100


def _square_meter_bol_power(sq_meter_power):
    # Average theta of 10 degrees assumed.
    _theta = 10
    # I_d assumed as 0.77
    _i_d = 0.77
    return sq_meter_power * _i_d * np.cos(_theta * np.pi / 180)


def _degradation(life):
    # Degradation factor assumed as 1.5
    degradation_factor = 1.5
    return (1 - degradation_factor / 100) ** life


def _square_meter_eol_power(_square_meter_bol_power, _degradation):
    return _square_meter_bol_power * _degradation


def _area_solar_array(sq_meter_power_eol, power_required_solar_array):
    return power_required_solar_array / sq_meter_power_eol


def _energy_storage_required(p_e, t_e):  # Whr
    # Assumption: dod = 0.3
    # Assumption: mu_b = 0.85
    dod = 0.3
    mu_b = 0.85
    return (p_e*t_e)/(dod*mu_b*3600)


def eps_parameters(power_peak, radius_planet, gravitional_constant, altitude, peak_power_tracking, array_efficiency,
                   solar_irradiance, life):

    # Orbit parameters
    fraction_power_used_night = 0.5
    fraction_power_payload_night = 1.0

    total_power = _total_power(power_peak)
    power_day = total_power
    power_night = total_power - fraction_power_used_night * total_power - fraction_power_payload_night * power_peak
    circular_orbit_time = _circular_orbit_time(radius_planet, altitude, gravitional_constant)

    circular_eclipse_time = _circular_eclipse_time(circular_orbit_time, altitude, radius_planet)

    circular_non_eclipse_time = _circular_non_eclipse_time(circular_orbit_time, circular_eclipse_time)

    # Required power for solar array at EOL
    power_solar_array = _power_solar_array(power_night, power_day, circular_eclipse_time, circular_non_eclipse_time,
                                           peak_power_tracking)

    sq_meter_bol_power = _square_meter_bol_power(_square_meter_power_solar_cell(solar_irradiance, array_efficiency))

    sq_meter_eol_power = _square_meter_eol_power(sq_meter_bol_power, _degradation(life))

    print(sq_meter_eol_power, power_solar_array)
    array_area = _area_solar_array(sq_meter_eol_power, power_solar_array)

    # EPS: Power Storage
    energy_storage_required = _energy_storage_required(power_night, circular_eclipse_time)

    _eps_parameters = namedtuple('eps_parameters', 'power_non_eclipse power_eclipse circular_orbit_time' +
                                 ' circular_eclipse_time circular_non_eclipse_time' +
                                 ' power_solar_array_eol power_solar_array_bol power_solar_array array_area' +
                                 ' energy_storage_required')

    return _eps_parameters(power_non_eclipse=power_day,
                           power_eclipse=power_night,
                           circular_orbit_time=circular_orbit_time,
                           circular_eclipse_time=circular_eclipse_time,
                           circular_non_eclipse_time=circular_non_eclipse_time,
                           power_solar_array_eol=array_area * sq_meter_eol_power,
                           power_solar_array_bol=array_area * sq_meter_bol_power,
                           power_solar_array=power_solar_array,
                           array_area=array_area,
                           energy_storage_required=energy_storage_required)
