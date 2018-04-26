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

ir_mapping = namedtuple('ir_mapping', 'mission_name ifov mass p_av p_peak')

HRSC = ir_mapping(mission_name="esa_mars",
                  ifov=0.1279,
                  mass=20.4,
                  p_av=43.4,
                  p_peak=61.38)

SSI = ir_mapping(mission_name='galileo',
                 ifov=0.1822,
                 mass=28,
                 p_av=16.26,
                 p_peak=23.00)

JunoCam = ir_mapping(mission_name="juno",
                     ifov=0.1822,
                     mass=28,
                     p_av=16.26,
                     p_peak=23.00)

Janus = ir_mapping(mission_name="juicy",
                   ifov=0.015,
                   mass=None,
                   p_av=None,
                   p_peak=None)
