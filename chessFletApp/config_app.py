import flet as ft
from chessTools.chessConfig import main_chess_vision_system_20_path


# FOR ALL VIEWS
def get_view_config():
    return {
        "MAIN": {
            "WIDTH": 411,
            "HEIGHT": 700,
            "BG_COLOR": "transparent",
            "IMG_SRC": main_chess_vision_system_20_path + "/chessFletApp/chessGameFletApp/assets/background.png"
        },
        "TEXT_CHESS_CLOCK": {
            "VALUE": "CHESS CLOCK",
            "SIZE": 50,
            "COLOR": ft.colors.WHITE,
            "WEIGHT": ft.FontWeight.W_500,
            "HEIGHT": 100,
            "TOP": 40
        },
        "BUTTON_BACK": {
            "VALUE": "BACK",
            "SIZE": 30,
            "BG_COLOR": ft.colors.DEEP_PURPLE_200,
            "COLOR": ft.colors.WHITE,
            "TOP": 630,
            "HEIGHT": 50,
            "LEFT2": 30
        },
    }


# FOR VIEW 1
def get_view_1_config():
    return {
        "BUTTONS_APPLY_NEXT": {
            "TOP": 630,
            "HEIGHT": 50,
            "BUTTON_APPLY": {
                "VALUE": "APPLY",
                "SIZE": 30,
                "RADIUS": 10,
                "BG_COLOR": ft.colors.DEEP_PURPLE_200,
                "COLOR": ft.colors.WHITE
            },
            "BUTTON_NEXT": {
                "VALUE": "NEXT",
                "SIZE": 30,
                "RADIUS": 10,
                "BG_COLOR": ft.colors.DEEP_PURPLE_200,
                "COLOR": ft.colors.WHITE
            }
        },
        "ENTRIES_WHITE_EVENT_BLACK": {
            "COLOR": ft.colors.WHITE,
            "WIDTH": 120,
            "BG_COLOR": ft.colors.DEEP_PURPLE_200,
            "TOP": 550,
            "HEIGHT": 50
        },
        "TEXTS_WHITE_EVENT_BLACK": {
            "VALUE_WHITE": "WHITE",
            "VALUE_EVENT": "EVENT",
            "VALUE_BLACK": "BLACK",
            "SIZE": 30,
            "COLOR": ft.colors.WHITE,
            "WEIGHT": ft.FontWeight.W_500,
            "BG_COLOR": ft.colors.DEEP_PURPLE_200,
            "TOP": 500,
            "HEIGHT": 50
        }
    }


def get_view_2_config():
    return {
        "BUTTON_START_GAME": {
            "VALUE": "START GAME",
            "SIZE": 30,
            "RADIUS": 10,
            "BG_COLOR": ft.colors.DEEP_PURPLE_200,
            "COLOR": ft.colors.WHITE,
            "TOP": 330,
            "HEIGHT": 180,
            "ROTATE": 3.14
        },
        "TEXT_PREPARE_CHESSBOARD": {
            "VALUE": "PREPARE CHESSBOARD!",
            "SIZE": 25,
            "COLOR": ft.colors.WHITE,
            "WEIGHT": ft.FontWeight.W_500,
            "HEIGHT": 100,
            "TOP": 280
        }
    }


# FOR VIEW 3
def get_view_3_config():
    return {
        "BUTTON_BLACK": {
            "TIME": "05:00",
            "SIZE": 130,
            "RADIUS": 10,
            "BG_COLOR": ft.colors.DEEP_PURPLE_200,
            "COLOR": ft.colors.WHITE,
            "TOP": 100,
            "HEIGHT": 180,
            "ROTATE": 3.14
        },
        "BUTTON_WHITE": {
            "TIME": "05:00",
            "SIZE": 130,
            "RADIUS": 10,
            "BG_COLOR": ft.colors.DEEP_PURPLE_200,
            "COLOR": ft.colors.WHITE,
            "BOTTOM": 100,
            "HEIGHT": 180,
        },
        "BUTTON_PAUSE": {
            "ICON": ft.icons.PAUSE_CIRCLE_FILLED_ROUNDED,
            "COLOR": ft.colors.DEEP_PURPLE_200,
            "SIZE": 85,
            "RADIUS": 10,
            "BG_COLOR": ft.colors.DEEP_PURPLE_200,
            "TOP": 300,
            "HEIGHT": 100,
        }
    }


# FOR VIEW 4
def get_view_4_config():
    return {
        "BUTTON_END_GAME": {
            "VALUE": "END GAME",
            "SIZE": 30,
            "COLOR": ft.colors.WHITE,
            "BG_COLOR": ft.colors.DEEP_PURPLE_200,
            "TOP": 300,
            "HEIGHT": 50,
        },
        "BUTTONS_BACK_START_NEW_GAME": {
            "TOP": 630,
            "HEIGHT": 50,
            "BUTTON_START_NEW_GAME": {
                "VALUE": "START NEW GAME",
                "SIZE": 25,
                "BG_COLOR": ft.colors.DEEP_PURPLE_200,
                "COLOR": ft.colors.WHITE
            },
            "BUTTON_BACK": {
                "SIZE": 25,
                "BG_COLOR": ft.colors.DEEP_PURPLE_200,
                "COLOR": ft.colors.WHITE
            }
        },
    }