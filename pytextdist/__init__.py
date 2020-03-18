import os
import logging
import logging.config
import json

__name__ = "pytextdist"
__version__ = "0.1.5"

import importlib

from . import preprocessing 
importlib.reload(preprocessing)
from . import input_validator
importlib.reload(input_validator)
from . import edit_distance 
importlib.reload(edit_distance)
from . import vector_similarity
importlib.reload(vector_similarity)

"""
Set up logging
| Default logging configuration can be edited in logging.json.
| You can also bring customized logging modules.
"""

env_key = "LOG_CFG"
value = os.getenv(env_key, None)

init_file_dir = os.path.dirname(os.path.abspath(__file__))
logger_config_json_path = value if value else os.path.join(init_file_dir, "logging.json")
logger_default_level = logging.INFO

if os.path.exists(logger_config_json_path):
	with open(logger_config_json_path, "rb") as f:
		try:
			config = json.load(f)
		except:
			config = json.loads(f.read().decode('utf-8'))
	logging.config.dictConfig(config)
else:
	logging.basicConfig(level=logger_default_level)
