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

camera = namedtuple('camera', 'ifov mass p_av p_peak')

SRC = camera(ifov=0.1279,
             mass=20.4,
             p_av=5.30,
             p_peak=7.50)

SSI = camera(ifov=0.1822,
             mass=28,
             p_av=16.26,
             p_peak=23.00)

JunoCam = camera(ifov=0.1822,
                 mass=28,
                 p_av=16.26,
                 p_peak=23.00)

Janus = camera(ifov=0.015,
               mass=None,
               p_av=None,
               p_peak=None)
