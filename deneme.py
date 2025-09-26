import flet as ft
import time

def main(page: ft.Page):
    page.title = "Flet counter example"

    text = ft.Text(value="Merhaba dünya", color="white")
    page.add(text)

    for i in range(30):
        text.value = i
        time.sleep(1)
        page.update()


ft.app(main)

