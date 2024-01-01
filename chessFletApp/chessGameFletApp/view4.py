import flet as ft

width = 411
height = 700
bg_col = "transparent"

top_chess_clock = 40
top_button_end_game = 300
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
                            ft.ElevatedButton(
                                content=ft.Text(value="END GAME", size=30),
                                style=ft.ButtonStyle(
                                    bgcolor=ft.colors.DEEP_PURPLE_200,
                                    color=ft.colors.WHITE
                                )),
                        ]
                    )
                ]),
                top=top_button_end_game,
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
                                content=ft.Text(value="BACK", size=30),
                                style=ft.ButtonStyle(
                                bgcolor=ft.colors.DEEP_PURPLE_200,
                                color=ft.colors.WHITE
                            )),
                            ft.ElevatedButton(
                                content=ft.Text(value="START NEW GAME", size=25),
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