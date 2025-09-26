import flet as ft
import time

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.bgcolor = ft.Colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(
        gradient= ft.LinearGradient(
            colors=[ft.Colors.RED, ft.Colors.BLUE],
            stops=[0,1],
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right
            
        )
    )
    page.window.width = 400
    page.window.height = 500
    page.window.resizable = False
    page.update()

    text = ft.Text(value="Merhaba dünya", color="white")
    page.add(text)

    page.add(
        ft.Row(controls=[
            ft.Text(value="A"),
            ft.Text(value="B"),
            ft.Text(value="C")
        ])
    )

    page.add(
        ft.Row(controls=[
            ft.TextField(label="Your Text:",width=200),
            ft.ElevatedButton(text="Find Language!")
        ])
    )

ft.app(main)

