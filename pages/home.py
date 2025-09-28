import flet as ft
from flet_model import route
from pages.base import BasePage

@route("home")
class HomeModel(BasePage):

    def __init__(self, page: ft.Page):
        super().__init__(page)

        # Build views using helper methods
        self.home_view = self.build_container(
            ft.Column(
                controls=[
                    self.build_text("🏠 Welcome Home!"),
                    ft.Text("This is your home dashboard. Enjoy the dark mode theme.",
                            size=14, color="white70", text_align=ft.TextAlign.CENTER),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            visible=True,
        )

        self.profile_view = self.build_container(
            ft.Column(
                controls=[
                    self.build_text("👤 Profile Page"),
                    ft.Text("Here you can update your account details.",
                            size=14, color="white70", text_align=ft.TextAlign.CENTER),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            visible=False,
        )

        self.notifications_view = self.build_container(
            ft.Column(
                controls=[
                    self.build_text("🔔 Notifications"),
                    ft.Text("Stay updated with the latest alerts and updates here.",
                            size=14, color="white70", text_align=ft.TextAlign.CENTER),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            visible=False,
        )

        # Navigation bar
        self.navigation_bar = ft.NavigationBar(
            bgcolor="#1e1e1e",
            indicator_color="#1DB954",
            selected_index=1,
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Profile"),
                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
                ft.NavigationBarDestination(icon=ft.Icons.NOTIFICATIONS, label="Notifications"),
            ],
            on_change=self.handle_navigation,
        )

        # Controls
        self.controls = [
            ft.Column(
                controls=[
                    self.home_view,
                    self.profile_view,
                    self.notifications_view,
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            self.navigation_bar,
        ]

    def handle_navigation(self, e):
        """Switch views when navigation bar changes."""
        if e.data == "0":  # Profile
            self.notifications_view.visible = False
            self.profile_view.visible = True
            self.home_view.visible = False

        elif e.data == "1":  # Home
            self.notifications_view.visible = False
            self.profile_view.visible = False
            self.home_view.visible = True

        elif e.data == "2":  # Notifications
            self.notifications_view.visible = True
            self.profile_view.visible = False
            self.home_view.visible = False

        self.update()
