from figurelib.figure import FigureContainer

from . import Introduction1
from . import appendix_Antenna_design
from . import Technical03
from . import system
#from . import appendix_Simple_model
from . import Appendix_Simple_Model_102032
from . import Application04
from . import appendix_para

main_container = FigureContainer(
    [
        Introduction1.collection,
        Technical03.collection,
        appendix_Antenna_design.collection,
        system.collection,
        #appendix_Simple_model.collection,
        Appendix_Simple_Model_102032.collection,
        Application04.collection,
        appendix_para.collection
    ]
)
