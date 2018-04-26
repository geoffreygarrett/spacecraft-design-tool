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


solar_cell = namedtuple('solar_cell', 's_power efficiency')

TRIPLE_JUNCTION_GAAS_RIGID = solar_cell(s_power=70,      # [W/kg]
                                        efficiency=26.8  # [%]
                                        )

