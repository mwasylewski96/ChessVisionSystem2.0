import flet as ft
def main(page):
    slider = ft.Slider(min=0, max=2, divisions=2)
    slider.value = 1
    page.add(
        ft.Text("Slider with a custom range and label:"),
        slider
    )

ft.app(target=main)