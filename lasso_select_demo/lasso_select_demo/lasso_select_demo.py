"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from typing import List, Dict
from rxconfig import config

import reflex as rx

from reflex_lasso_select import lasso_select

filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    selected_points: List[Dict[str, float]] = []

    def set_points(self, pts: List[Dict[str, float]]):
        self.selected_points = pts


def index() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Test your custom component by editing ",
                rx.code(filename),
                font_size="2em",
            ),
            lasso_select(
                src="test_image.png",
                value=State.selected_points,
                on_change=State.set_points,
            ),
            rx.text("Selected Points:"),
            rx.text(State.selected_points),
            align="center",
            spacing="7",
        ),
        height="100vh",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
