# pages/signup.py
import flet as ft
from flet_model import route
from email_validator import validate_email, EmailNotValidError
from zxcvbn import zxcvbn
from pages.base import BasePage


@route("signup")
class SignUpModel(BasePage):
    def __init__(self, page: ft.Page):
        super().__init__(page)

        # Validation state
        self.valid_email = False
        self.valid_username = False
        self.valid_password = False
        self.valid_password_confirm = False

        # Fields
        self.email_field = ft.TextField(
            label="Email",
            width=350,
            border_color="#2a2a2a",
            bgcolor="#1e1e1e",
            color="white",
            cursor_color="white",
            border_radius=10,
            text_size=16,
            content_padding=ft.padding.only(left=12, top=20, bottom=12),
            on_change=self.validate_email,
        )
        # small helper label under field
        self.email_label = self.build_text("", size=12, weight="normal", visible=False)

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
            on_change=self.validate_username,
        )
        self.username_label = self.build_text("", size=12, weight="normal", visible=False)

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
            on_change=self.validate_password,
        )
        self.strength_indicators = ft.Row(
            spacing=4,
            alignment=ft.MainAxisAlignment.START,
            controls=[],
        )

        self.confirm_password_field = ft.TextField(
            label="Confirm Password",
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
            on_change=self.password_match,
        )

        self.submit_btn = ft.ElevatedButton(
            text="Sign Up",
            disabled=True,
            width=350,
            style=ft.ButtonStyle(
                bgcolor="#1DB954",
                color="white",
                shape=ft.RoundedRectangleBorder(radius=10),
                padding=15,
            ),
            on_click=self.request_signup,
        )

        # Controls layout
        self.controls = [
            ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Text("📝", size=64),
                        alignment=ft.alignment.center,
                        padding=10,
                    ),
                    self.build_text("Sign Up", size=22),
                    self.email_field,
                    self.email_label,
                    self.username_field,
                    self.username_label,
                    ft.Column(
                        controls=[
                            self.password_field,
                            self.strength_indicators,
                        ],
                        width=350,
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                    self.confirm_password_field,
                    self.submit_btn,
                    ft.OutlinedButton(
                        text="Back to Login",
                        on_click=self.go_to_login,
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
                spacing=15,
            )
        ]

    # === Validation methods ===
    def validate_email(self, e):
        try:
            validate_email(e.data)
            self.email_field.border_color = ft.Colors.GREEN
            self.email_label.visible = True
            self.email_label.value = "Email is valid"
            self.email_label.color = ft.Colors.GREEN
            self.valid_email = True
        except EmailNotValidError as err:
            self.email_field.border_color = ft.Colors.RED
            self.email_label.visible = True
            self.email_label.value = str(err)
            self.email_label.color = ft.Colors.RED
        self.update()
        self.check_all_valid()

    def validate_username(self, e):
        if e.data != "":
            self.username_label.visible = True
            self.username_label.value = "Username available"
            self.username_label.color = ft.Colors.GREEN
            self.valid_username = True
        else:
            self.username_label.visible = False
        self.update()
        self.check_all_valid()

    def validate_password(self, e):
        password = e.data
        if password != "":
            result = zxcvbn(password)
            score = result["score"]
            strength_colors = ["grey", "red", "orange", "yellow", "green"]
            self.strength_indicators.controls = [
                ft.Container(
                    width=18,
                    height=8,
                    bgcolor=strength_colors[i] if i <= score else "#333",
                    border_radius=4,
                )
                for i in range(5)
            ]
            self.valid_password = True
        self.update()
        self.check_all_valid()

    def password_match(self, e):
        if self.password_field.value != e.data:
            self.password_field.border_color = ft.Colors.RED
            self.confirm_password_field.border_color = ft.Colors.RED
        else:
            self.password_field.border_color = ft.Colors.GREEN
            self.confirm_password_field.border_color = ft.Colors.GREEN
            self.valid_password_confirm = True
        self.update()
        self.check_all_valid()

    def check_all_valid(self):
        if all(
            [
                self.valid_email,
                self.valid_username,
                self.valid_password,
                self.valid_password_confirm,
            ]
        ):
            self.submit_btn.disabled = False
            self.update()

    # === Actions ===
    def go_to_login(self, e):
        self.navigate_to("/login")  # BasePage helper

    def request_signup(self, e):
        print("signing up ...")
        self.navigate_to("/home")  # BasePage helper
