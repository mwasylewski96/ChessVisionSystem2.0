"""
Functions to obtain config values from config.yaml file.
"""

############################
###  EXTERNAL LIBRARIES  ###
############################
import os


############################
###  INTERNAL LIBRARIES  ###
############################
from chessTool import read_yaml, write_yaml

main_dir_path = os.path.dirname(os.path.realpath(__file__))
PATH_TO_CONFIG = main_dir_path + '/chessConfig.yaml'
config = read_yaml(PATH_TO_CONFIG)


def get_chess_config():
    return config["chess_config"]