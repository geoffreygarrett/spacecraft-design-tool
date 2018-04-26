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

gravity_science_instrument = namedtuple('gravity_science_instrument', 'mission_name mass p_av p_peak')

JUNO_GSI = gravity_science_instrument(mission_name="juno",
                                      mass=6.6,
                                      p_av=0,
                                      p_peak=0
                                      )
