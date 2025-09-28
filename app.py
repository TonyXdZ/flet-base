import flet as ft
from flet_model import Model, Router
from pages.home import HomeModel
from pages.login import LoginModel
from pages.signup import SignUpModel 

def main(page: ft.Page):
    page.title = "YOUR APP NAME"
    page.window.height = 712
    page.window.width = 375
    page.go("/login")


ft.app(target=main)