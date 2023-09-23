from figurelib.figure import FigureContainer

from . import collection1
from . import collection2
from . import prob_synchro
from . import dopplerCurve
from . import apdx_usrp_b210
from . import SNR_simulations
from . import system_design
from . import modulation
from . import multip_path_figures
from . import Angle_gain_plot
from . import test_results
from . import channel_test


main_container = FigureContainer(
    [
        collection1.collection,
    ]
)
