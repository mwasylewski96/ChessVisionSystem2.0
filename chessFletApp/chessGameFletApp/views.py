import flet as ft
from chessFletApp.chessGameFletApp.view1 import View1
from chessFletApp.chessGameFletApp.view2 import View2
from chessFletApp.chessGameFletApp.view3 import View3
from chessFletApp.chessGameFletApp.view4 import View4


def view_handler(
        page,
        loop,
        start_game_process,
        pause_process,
        end_game_process,
        read_temp_data_white_event_black
):
    return {
        "/view1": ft.View(
            route="/view1",
            controls=[
                View1(page, loop, read_temp_data_white_event_black)
            ]
        ),
        "/view2": ft.View(
            route="/view2",
            controls=[
                View2(page, loop, start_game_process)
            ]
        ),
        "/view3": ft.View(
            route="/view3",
            controls=[
                View3(page, loop, pause_process)
            ]
        ),
        "/view4": ft.View(
            route="/view4",
            controls=[
                View4(page, loop, end_game_process)
            ]
        )
    }