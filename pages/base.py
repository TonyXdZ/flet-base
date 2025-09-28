# base_page.py
import flet as ft
from flet_model import Model

class BasePage(Model):
    """
    BasePage provides a consistent layout and style for all app pages.
    Other pages (Home, Login, Signup, etc.) can inherit from this.
    """

    # Common layout configuration (can be overridden in child pages)
    vertical_alignment = ft.MainAxisAlignment.CENTER
    horizontal_alignment = ft.CrossAxisAlignment.CENTER
    bgcolor = "#121212"
    padding = 20
    spacing = 10

    def __init__(self, page: ft.Page):
        super().__init__(page)
        self.page = page
        # apply background color to the page
        try:
            self.page.bgcolor = self.bgcolor
        except Exception:
            # some flet_model setups might handle page differently; ignore if not available
            pass

    def build_container(self, content, visible=True, margin=10, padding=20, border_radius=12, bgcolor="#1e1e1e", alignment=ft.alignment.center):
        """
        Helper method to build styled containers for sections/cards.
        """
        return ft.Container(
            content=content,
            margin=margin,
            padding=padding,
            border_radius=border_radius,
            bgcolor=bgcolor,
            alignment=alignment,
            visible=visible,
        )

    def build_text(self, text: str, size: int = 22, weight="bold", color="white", visible=True, text_align=ft.TextAlign.CENTER, **kwargs):
        """
        Helper for consistent Text creation. Accepts 'visible' and any extra ft.Text kwargs.
        """
        return ft.Text(text, size=size, weight=weight, color=color, text_align=text_align, visible=visible, **kwargs)

    def navigate_to(self, route: str):
        """Navigate to another page route."""
        self.page.go(route)
