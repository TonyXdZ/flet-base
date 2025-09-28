import flet as ft
from flet_model import route
from pages.base import BasePage
from utils import build_request, async_build_request


@route("login")
class LoginModel(BasePage):

    def __init__(self, page: ft.Page):
        super().__init__(page)

        # Placeholder logo (replace with ft.Image if available)
        self.logo = ft.Container(
            content=ft.Text("🔒", size=72),
            alignment=ft.alignment.center,
            padding=10,
            animate_opacity=500,
        )

        self.username_field = ft.TextField(
            label="Username",
            width=350,
            border_color="#2a2a2a",
            bgcolor="#1e1e1e",
            color="white",
            cursor_color="white",
            border_radius=10,
            text_size=16,
            content_padding=ft.padding.only(left=12, top=20, bottom=12),
        )

        self.password_field = ft.TextField(
            label="Password",
            password=True,
            can_reveal_password=True,
            width=350,
            border_color="#2a2a2a",
            bgcolor="#1e1e1e",
            color="white",
            cursor_color="white",
            border_radius=10,
            text_size=16,
            content_padding=ft.padding.only(left=12, top=20, bottom=12),
        )

        # Main controls layout
        self.controls = [
            ft.Column(
                controls=[
                    self.logo,
                    self.build_text("Welcome Back", size=22),
                    self.username_field,
                    self.password_field,
                    ft.ElevatedButton(
                        text="Login",
                        on_click=self.request_login,
                        width=350,
                        style=ft.ButtonStyle(
                            bgcolor="#1DB954",
                            color="white",
                            shape=ft.RoundedRectangleBorder(radius=10),
                            padding=15,
                        ),
                    ),
                    ft.OutlinedButton(
                        text="Sign Up",
                        on_click=self.sign_up,
                        width=350,
                        style=ft.ButtonStyle(
                            color="white",
                            side=ft.BorderSide(1, "white"),
                            shape=ft.RoundedRectangleBorder(radius=10),
                            padding=15,
                        ),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )
        ]

    def did_mount(self):
        # Animate logo on mount
        self.logo.opacity = 0
        self.update()
        self.logo.opacity = 1
        self.logo.update()

    def request_login(self, e):
        if self.username_field.value == "" or self.password_field.value == "":
            self.page.dialog = ft.AlertDialog(
                title=ft.Text("Username and Password required!", size=16, color="white"),
                bgcolor="#2c2c2c",
                open=True,
            )
            self.page.update()
        else:
            # Example login handling
            self.navigate_to("/home")  # use BasePage helper

    def sign_up(self, e):
        self.navigate_to("/signup")  # use BasePage helper