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

rtg = namedtuple('rtg', 'power_mass mass fuel_mass heat power')

ASRG = rtg(power_mass=4.1,
           mass=34,
           fuel_mass=1,
           heat=500,
           power=140)

GPHS_RTG_1 = rtg(power_mass=5.2,
                 mass=55.9,
                 fuel_mass=7.8,
                 heat=4400,
                 power=300)

GPHS_RTG_2 = rtg(power_mass=5.4,
                 mass=57.8,
                 fuel_mass=7.8,
                 heat=4400,
                 power=300)

if __name__=="__main__":
    print(GPHS_RTG_1.power)
