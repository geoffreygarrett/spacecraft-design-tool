from tools import _total_power, _square_meter_eol_power, _degradation, _square_meter_bol_power, \
    _square_meter_power_solar_cell
from power_storage.batteries import *
from power_generation.solar_cells import *
import numpy as np

MISSION_DURATION_YEARS = 20  # [years]
PERIOD_OBSERVATION = 1       # [years]
PERIOD_TRAVEL = 19           # [years]
FRACTION_TRAVEL = 0.1        # [-]
FRACTION_OBSERVATION = 1.0   # [-]
YEARS_TO_HOURS = 365*24      # [year to hour conversion factor]

#  Statistical relation for total power required.
example_payload_power  = 50                                               # [W]
example_peak_payload_power = example_payload_power * np.sqrt(2)           # Approximation of Peak (Peak = Avg * sqrt(2))
example_peak_total_power    = _total_power(example_peak_payload_power)    # [1]

#  [REF 1]
#  Calculation of surface area required for solar-array.
solar_irradiance_pluto = 0.872                                                                # [W/m^2]
example_solar_cell     = TRIPLE_JUNCTION_GAAS_RIGID                                           #
example_sq_meter_bol_power = _square_meter_bol_power(
        _square_meter_power_solar_cell(solar_irradiance_pluto,
                                       example_solar_cell.efficiency))
sq_meter_eol_power = _square_meter_eol_power(example_sq_meter_bol_power,
                                             _degradation(PERIOD_TRAVEL+PERIOD_OBSERVATION))

example_solar_array_area = example_peak_total_power/sq_meter_eol_power
print("REF 1: {:.1f} [m^2]".format(example_solar_array_area))


# [REF 2]
# Calculation of battery weight required to power entire mission.
example_battery = Li_SoCl2
total_energy_required = (FRACTION_OBSERVATION * PERIOD_OBSERVATION * YEARS_TO_HOURS
                         + FRACTION_TRAVEL * PERIOD_TRAVEL * YEARS_TO_HOURS) * example_peak_payload_power * 3600
example_battery_weight = total_energy_required / Li_SoCl2.energy_density
print("REF 2: {:.1f} [kg]".format(example_battery_weight))




# BIBLIOGRAPHY
# [1] Charles D. Brown.Elements of spacecraft design. (2002). 1st ed. AIAA.

