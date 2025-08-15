import flet as ft
from view.flet_view import FletView

def main(page: ft.Page):
    FletView(page)

ft.app(target=main)