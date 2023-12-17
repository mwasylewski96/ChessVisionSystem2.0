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
from chessTools.chessTool import read_yaml, write_yaml

PATH_TO_CONFIG_YAML = os.path.dirname(os.path.realpath(__file__)) + '/chessConfig.yaml'
config = read_yaml(PATH_TO_CONFIG_YAML)

main_chess_vision_system_20_path = os.path.dirname(os.path.realpath(__file__))[:-11:1]
# [:-11:1] means removing '\chessTools' from path


def get_chess_config():
    return config["chess_config"]


def get_chess_current_game_table_config():
    path_to_config_chess_current_game_table_config = main_chess_vision_system_20_path\
                                              + get_chess_config()['paths']['chessCurrentGameTable']
    return path_to_config_chess_current_game_table_config


def get_chess_init_game_table_config():
    path_to_config_chess_init_game_table_config = main_chess_vision_system_20_path\
                                              + get_chess_config()['paths']['chessInitGameTable']
    return path_to_config_chess_init_game_table_config


def get_chess_cameras_config():
    return get_chess_config()['cameras']['windows']


def get_chess_calibration_config():
    return get_chess_config()['board']['calibration']
