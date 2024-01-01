import flet as ft
from views import view_handler


def main(page: ft.Page):

    def route_change(route):
        print(page.route)

        page.views.clear()
        page.views.append(
            view_handler(page)[page.route]
        )
    page.on_route_change = route_change
    page.go("/view1")


if __name__ == "__main__":
    ft.app(target=main)