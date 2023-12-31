import flet as ft

width = 411
height = 700
bg_col = "transparent"

top_chess_clock = 40
top_white_event_black = 500
top_entries = 550
top_buttons = 630

body = ft.Container(
    ft.Stack(
        [
            ft.Image(
                src="assets/background.png",
                width=width,
                height=height
            ),
            ft.Container(
                ft.Column([
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.Text(
                                "CHESS CLOCK",
                                size=50,
                                color=ft.colors.WHITE,
                                italic=True,
                                weight=ft.FontWeight.W_500
                            )
                        ]
                    )
                ]),
                alignment=ft.alignment.center,
                width=width,
                height=100,
                bgcolor=bg_col,
                top=top_chess_clock
            ),
            ft.Container(
                ft.Column([
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.Text("WHITE", size=30, color=ft.colors.WHITE, italic=True, weight=ft.FontWeight.W_500),
                            ft.Text("EVENT", size=30, color=ft.colors.WHITE, italic=True, weight=ft.FontWeight.W_500),
                            ft.Text("BLACK", size=30, color=ft.colors.WHITE, italic=True, weight=ft.FontWeight.W_500),
                        ]
                    ),
                ]),
                top=top_white_event_black,
                width=width,
                height=50,
                bgcolor=bg_col
            ),
            ft.Container(
                ft.Column([
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.TextField(color=ft.colors.WHITE, width=120, bgcolor=ft.colors.DEEP_PURPLE_200),
                            ft.TextField(color=ft.colors.WHITE, width=120, bgcolor=ft.colors.DEEP_PURPLE_200),
                            ft.TextField(color=ft.colors.WHITE, width=120, bgcolor=ft.colors.DEEP_PURPLE_200),
                        ]
                    )
                ]),
                top=top_entries,
                width=width,
                height=50,
                bgcolor=bg_col
            ),
            ft.Container(
                ft.Column([
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.ElevatedButton(
                                content=ft.Text(value="APPLY", size=30),
                                style=ft.ButtonStyle(
                                bgcolor=ft.colors.DEEP_PURPLE_200,
                                color=ft.colors.WHITE
                            )),
                            ft.ElevatedButton(
                                content=ft.Text(value="NEXT", size=30),
                                style=ft.ButtonStyle(
                                    bgcolor=ft.colors.DEEP_PURPLE_200,
                                    color=ft.colors.WHITE
                                )),
                        ]
                    )
                ]),
                top=top_buttons,
                width=width,
                height=50,
                bgcolor=bg_col
            )
        ]
    )
)


def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.title = "Calc App"
    # result = ft.Text(value="CHESS CLOCK APP")
    page.add(
        body
    )


ft.app(target=main)