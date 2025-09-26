# I will use a api to check language of a given text. Maybe a basic GUI with tkinter
import detectlanguage
import flet as ft
import time

my_key = "6c8b289b01a6edfe12d37e00771ff089"

detectlanguage.configuration.api_key = my_key

def find_language(text):
    return detectlanguage.detect_code(text)

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

    page.add(
        ft.Text(value="Merhaba dünya",size = 32, color="white", weight=ft.FontWeight.BOLD ,text_align= "Center")
    )
    


    page.add(
        ft.Row(controls=[
            ft.TextField(label="Your Text:",width=200, height=300),
            ft.ElevatedButton(text="Find Language!")
        ])
    )

ft.app(main)

