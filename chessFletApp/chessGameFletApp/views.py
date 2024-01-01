import flet as ft
from chessFletApp.chessGameFletApp.view1 import View1
from chessFletApp.chessGameFletApp.view2 import View2
from chessFletApp.chessGameFletApp.view3 import View3
from chessFletApp.chessGameFletApp.view4 import View4


def view_handler(page):
    return {
        "/view1": ft.View(
            route="/view1",
            controls=[
                View1(page)
            ]
        ),
        "/view2": ft.View(
            route="/view2",
            controls=[
                View2(page)
            ]
        ),
        "/view3": ft.View(
            route="/view3",
            controls=[
                View3(page)
            ]
        ),
        "/view4": ft.View(
            route="/view4",
            controls=[
                View4(page)
            ]
        )
    }