from payload.camera import *
from payload.infra_red import *
from payload.ultra_violet import *
from payload.gravity_science import *
from power_generation.solar_cells import *
from power_storage.batteries import *
from tools import eps_parameters, _total_power


# Authorship -----------------------------------------------------------------------------#
__author__      = ["Geoffrey Hyde Garrett", "Vladimir"]
__copyright__   = None
__credits__     = None
__license__     = "MIT"
__version__     = "1.0.0"
__maintainer__  = ["Geoffrey Hyde Garrett", "Vladimir"]
__email__       = ["g.h.garrett13@gmail.com", "vladifm97@gmail.com"]
__status__      = "Development"

# -------------------------------------------------------------------------------------------------------------------- #
# Define design parameters
gm = 126.687*10**6        # [km^3/s^2]
h = 5000.                 # [km]
sr = 2                    # [km]
d = 5                     # [AU]
t_op = 3                  # [years]
t_voyage = 3              # [years]
r_planet = 69911.         # [km]
lambda_j = 30.            # [deg]
solar_irr = 50.25         # [W/m^2]


# Define chosen instruments for scientific payload.
chosen_camera = SRC
chosen_infra_red = HRSC
chosen_ultra_violet = JUNO_UVS
chosen_gravity_science = JUNO_GSI

# chosen_micro_waves
chosen_instruments = [chosen_camera, chosen_infra_red, chosen_ultra_violet, chosen_gravity_science]

# Payload parameters calculation.
p_av = sum([x.p_av for x in chosen_instruments])
p_peak = sum([x.p_peak for x in chosen_instruments])
m_pl = sum([x.mass for x in chosen_instruments])

# EPS Power generation parameters.
chosen_solar_cells = TRIPLE_JUNCTION_GAAS_RIGID
if t_op+t_voyage <= 5:
    peak_power_tracking = True
else:
    peak_power_tracking = False
_eps_parameters = eps_parameters(p_peak, r_planet, gm, h, peak_power_tracking, chosen_solar_cells.efficiency, solar_irr,
                                 life=t_op+t_voyage)
p_av_total = _total_power(p_av)
p_peak_total = _total_power(p_peak)
p_bol = _eps_parameters.power_solar_array_bol
p_eol = _eps_parameters.power_solar_array_eol
a_sa = _eps_parameters.array_area
m_sa = _eps_parameters.power_solar_array*(1/(chosen_solar_cells.s_power/d**2))

# EPS Power storage parameters.
chosen_battery = Li_SoCl2
e_stored = _eps_parameters.energy_storage_required

print("-"*39+"|")
print("DESIGN PARAMETERS".ljust(39)+"|")
print("-"*39+"|")
print("Altitude: ".ljust(23)+"{:.0f}. [km]".ljust(18).format(h)+"|")
print("Spacial resolution: ".ljust(23)+"{:.3f} [km]".ljust(17).format(sr)+"|")
print("Solar irradiance: ".ljust(23)+"{:.2f} [W/m^2]".ljust(17).format(solar_irr)+"|")
print("-"*39+"|")
print("PAYLOAD PARAMETERS".ljust(39)+"|")
print("-"*39+"|")
print("Payload mass: ".ljust(23)+"{:.2f} [kg]".ljust(17).format(m_pl)+"|")
print("Payload average power: ".ljust(23)+"{:.1f} [W]".ljust(18).format(p_av)+"|")
print("Payload peak power: ".ljust(23)+"{:.1f} [W]".ljust(18).format(p_peak)+"|")
print("PSA: ".ljust(23)+"{:.0f} [W]".ljust(18).format(_eps_parameters.power_solar_array)+"|")
print("-"*39+"|")
print("EPS: POWER GENERATION PARAMETERS".ljust(39)+"|")
print("-"*39+"|")
print("Array area: ".ljust(23)+"{:.2f} [m^2]".ljust(17).format(a_sa)+"|")
print("Array power (BOL): ".ljust(23)+"{:.1f} [W]".ljust(17).format(p_bol)+"|")
print("Array power (EOL): ".ljust(23)+"{:.1f} [W]".ljust(17).format(p_eol)+"|")
print("Array mass: ".ljust(23)+"{:.1f} [kg]".ljust(17).format(m_sa)+"|")
print("Average total power: ".ljust(23)+"{:.1f} [W]".ljust(17).format(p_av_total)+"|")
print("Peak total power: ".ljust(23)+"{:.1f} [W]".ljust(17).format(p_peak_total)+"|")
print("-"*39+"|")
print("EPS: POWER STORAGE PARAMETERS".ljust(39)+"|")
print("-"*39+"|")
print("Energy capacity: ".ljust(23)+"{:.1f} [Whr]".ljust(17).format(e_stored)+"|")
print("Battery weight: ".ljust(23)+"{:.2f} [kg]".ljust(17).format(e_stored/chosen_battery.energy_density)+"|")

# -------------------------------------------------------------------------------------------------------------------- #
# Intermediary parameters
circular_orbit_time = _eps_parameters.circular_orbit_time
circular_eclipse_time = _eps_parameters.circular_eclipse_time
circular_non_eclipse_time = _eps_parameters.circular_non_eclipse_time
power_eclipse = _eps_parameters.power_eclipse
power_non_eclipse = _eps_parameters.power_non_eclipse

print("-"*39+"|")
print("ORBIT PARAMETERS".ljust(39)+"|")
print("-"*39+"|")
print("T_day: ".ljust(23)+"{:.1f} [min]".ljust(17).format(circular_non_eclipse_time/60)+"|")
print("T_eclipse: ".ljust(23)+"{:.2f} [min]".ljust(17).format(circular_eclipse_time/60)+"|")
print("P_day: ".ljust(23)+"{:.1f} [W]".ljust(17).format(power_non_eclipse)+"|")
print("P_eclipse: ".ljust(23)+"{:.1f} [W]".ljust(17).format(power_eclipse)+"|")

