
"""
pytextdist

Author: Yifan Wu
Contact: yw693@cornell.edu
"""


__name__ = "pytextdist"
__version__ = "0.1.6"

import importlib

from . import preprocessing 
importlib.reload(preprocessing)
from . import input_validator
importlib.reload(input_validator)
from . import edit_distance 
importlib.reload(edit_distance)
from . import vector_similarity
importlib.reload(vector_similarity)
