import flet as ft
from chessFletApp.chessGameFletApp.view1 import View1
from chessFletApp.chessGameFletApp.view2 import View2
from chessFletApp.chessGameFletApp.view3 import View3
from chessFletApp.chessGameFletApp.view4 import View4


def view_handler(
        page,
        loop,
        start_chess_game,
        write_event_and_players_data_chess_game,
        execute_procedure_of_move_white,
        execute_procedure_of_move_black,
        end_chess_game
):
    view_1 = "/view1"
    view_2 = "/view2"
    view_3 = "/view3"
    view_4 = "/view4"

    view_to_return = page.route

    if view_to_return == view_1:
        return ft.View(
            route=view_to_return,
            controls=[
                View1(
                    page=page,
                    loop=loop
                )
            ]
        )
    elif view_to_return == view_2:
        return ft.View(
            route=view_to_return,
            controls=[
                View2(
                    page=page,
                    loop=loop,
                    start_chess_game=start_chess_game,
                    write_event_and_players_data_chess_game=write_event_and_players_data_chess_game
                )
            ]
        )
    elif view_to_return == view_3:
        return ft.View(
            route=view_to_return,
            controls=[
                View3(
                    page=page,
                    loop=loop,
                    execute_procedure_of_move_white=execute_procedure_of_move_white,
                    execute_procedure_of_move_black=execute_procedure_of_move_black,
                )
            ]
        )
    elif view_to_return == view_4:
        return ft.View(
            route=view_to_return,
            controls=[
                View4(page, loop, end_chess_game)
            ]
        )


    # return {
    #     view_1: ft.View(
    #         route=view_1,
    #         controls=[
    #             View1(
    #                 page=page,
    #                 loop=loop
    #             )
    #         ]
    #     ),
    #     view_2: ft.View(
    #         route=view_2,
    #         controls=[
    #             View2(
    #                 page=page,
    #                 loop=loop,
    #                 start_chess_game=start_chess_game,
    #                 write_event_and_players_data_chess_game=write_event_and_players_data_chess_game
    #             )
    #         ]
    #     ),
    #     view_3: ft.View(
    #         route=view_3,
    #         controls=[
    #             View3(
    #                 page=page,
    #                 loop=loop,
    #                 execute_procedure_of_move_white=execute_procedure_of_move_white,
    #                 execute_procedure_of_move_black=execute_procedure_of_move_black,
    #             )
    #         ]
    #     ),
    #     view_4: ft.View(
    #         route=view_4,
    #         controls=[
    #             View4(page, loop, end_chess_game)
    #         ]
    #     )
    # }