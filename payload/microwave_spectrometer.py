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

microwave_spectrometer = namedtuple('microwave_spectrometer', 'mission_name mass p_av p_peak')

MWR = microwave_spectrometer(mission_name="juno",
                             mass=6.6,
                             p_av=58.5,
                             p_peak=82.73
                             )
