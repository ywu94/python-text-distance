import os
import logging
import logging.config
import yaml

__name__ = "pytextdist"
__version__ = "0.0.1"

from .levenshtein import levenshtein_distance, levenshtein_similarity

"""
Set up logging
| Default logging configuration can be edited in logging.yaml.
| You can also bring customized logging modules.
"""

env_key = "LOG_CFG"
value = os.getenv(env_key, None)

init_file_dir = os.path.dirname(os.path.abspath(__file__))
logger_config_yaml_path = value if value else os.path.join(init_file_dir, "logging.yaml")
logger_default_level = logging.INFO

if os.path.exists(logger_config_yaml_path):
	with open(logger_config_yaml_path, "rt") as f:
		config = yaml.safe_load(f.read())
	logging.config.dictConfig(config)
else:
	logging.basicConfig(level=logger_default_level)
