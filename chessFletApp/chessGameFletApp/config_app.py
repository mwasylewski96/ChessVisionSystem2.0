import flet as ft


# FOR ALL VIEWS
def get_view_config():
    return {
        "MAIN": {
            "DEVELOP_MODE": False,
            "WIDTH": 411,
            "HEIGHT": 700,
            "BG_COLOR": "transparent",
            "IMG_SRC": "assets/background.png",
            "PAGE_TITLE": "Chess Flet App"
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
        }
    }


# FOR VIEW 1
def get_view_1_config():
    return {
        "BUTTON_NEXT": {
            "VALUE": "NEXT",
            "SIZE": 30,
            "RADIUS": 10,
            "BG_COLOR": ft.colors.DEEP_PURPLE_200,
            "COLOR": ft.colors.WHITE,
            "RIGHT": 30,
            "TOP": 630,
            "HEIGHT": 50,
        },
        "ENTRIES_WHITE_BLACK": {
            "COLOR": ft.colors.WHITE,
            "WIDTH": 140,
            "BG_COLOR": ft.colors.DEEP_PURPLE_200,
            "HINT_WHITE": "Insert player 1",
            "HINT_BLACK": "Insert player 2",
            "TOP": 300,
            "HEIGHT": 50
        },
        "ENTRY_EVENT": {
            "COLOR": ft.colors.WHITE,
            "WIDTH": 150,
            "HINT": "Insert event",
            "BG_COLOR": ft.colors.DEEP_PURPLE_200,
            "TOP": 420,
            "HEIGHT": 50
        },
        "TEXTS_WHITE_BLACK": {
            "VALUE_WHITE": "WHITE",
            "VALUE_BLACK": "BLACK",
            "SIZE": 30,
            "COLOR": ft.colors.WHITE,
            "WEIGHT": ft.FontWeight.W_500,
            "BG_COLOR": ft.colors.DEEP_PURPLE_200,
            "TOP": 250,
            "HEIGHT": 50
        },
        "TEXT_EVENT": {
            "VALUE": "EVENT",
            "SIZE": 30,
            "COLOR": ft.colors.WHITE,
            "WEIGHT": ft.FontWeight.W_500,
            "BG_COLOR": ft.colors.DEEP_PURPLE_200,
            "TOP": 370,
            "HEIGHT": 50
        },
        "PATH": "event_and_players_data_chess_game.json"
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
            "TIME": {
                "MIN": 5,
                "SEC": 0
            },
            "WIDTH": 380,
            "SIZE": 130,
            "RADIUS": 10,
            "BG_COLOR": {
                "DISABLED": ft.colors.DEEP_PURPLE_100,
                "DEFAULT": ft.colors.DEEP_PURPLE_200
            },
            "COLOR": {
                "DISABLED": ft.colors.WHITE,
                "DEFAULT": ft.colors.WHITE
            },
            "TOP": 80,
            "HEIGHT": 180,
            "ROTATE": 3.14
        },
        "BUTTON_WHITE": {
            "TIME": {
                "MIN": 5,
                "SEC": 0
            },
            "WIDTH": 380,
            "SIZE": 130,
            "RADIUS": 10,
            "BG_COLOR": {
                "DISABLED": ft.colors.DEEP_PURPLE_100,
                "DEFAULT": ft.colors.DEEP_PURPLE_200
            },
            "COLOR": {
                "DISABLED": ft.colors.WHITE,
                "DEFAULT": ft.colors.WHITE
            },
            "BOTTOM": 80,
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
        },
        "PATH": {
            "TIMERS": "state_of_timers.json",
            "BUTTONS": "state_of_buttons.json"
        }
    }


# FOR VIEW 4
def get_view_4_config():
    return {
        "BUTTON_QUIT": {
            "VALUE": "QUIT",
            "SIZE": 30,
            "COLOR": ft.colors.WHITE,
            "BG_COLOR": ft.colors.DEEP_PURPLE_200,
            "TOP": 530,
            "HEIGHT": 50,
        },
        "BUTTON_RESUME": {
            "VALUE": "RESUME",
            "SIZE": 30,
            "BG_COLOR": ft.colors.DEEP_PURPLE_200,
            "COLOR": ft.colors.WHITE,
            "TOP": 450,
            "HEIGHT": 50,
        }
    }


# FOR VIEW 5
def get_view_5_config():
    return {
        "BUTTONS_WHITE_DRAW_BLACK": {
            "SRC_WHITE": "assets/white_win.png",
            "SRC_DRAW": "assets/draw.png",
            "SRC_BLACK": "assets/black_win.png",
            "TOP": 370,
            "BG_COLOR": "transparent",
            "WIDTH": 120,
            "HEIGHT": 120
        },
        "TEXT_CHOOSE_WINNER": {
            "VALUE": "CHOOSE WINNER",
            "SIZE": 30,
            "COLOR": ft.colors.WHITE,
            "WEIGHT": ft.FontWeight.W_500,
            "HEIGHT": 50,
            "TOP": 300
        }
    }


# FOR VIEW 6
def get_view_6_config():
    return {
        "TEXT_CONGRATULATIONS": {
            "VALUE": "CONGRATULATIONS!",
            "SIZE": 30,
            "COLOR": ft.colors.WHITE,
            "WEIGHT": ft.FontWeight.W_500,
            "HEIGHT": 50,
            "TOP": 300
        },
        "BUTTON_MENU": {
            "VALUE": "MENU",
            "SIZE": 30,
            "COLOR": ft.colors.WHITE,
            "BG_COLOR": ft.colors.DEEP_PURPLE_200,
            "TOP": 430,
            "HEIGHT": 50,
        }
    }