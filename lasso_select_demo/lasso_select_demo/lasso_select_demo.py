"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from typing import List, Dict

import reflex as rx

from reflex_lasso_select.lasso_select import LassoSelect


class State(rx.State):
    """The app state."""

    selected_points: List[Dict[str, float]] = []

    def set_points(self, pts: List[Dict[str, float]]):
        self.selected_points = pts

    @rx.var
    def selected_points_string(self) -> str:
        return str(self.selected_points)


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Lasso select demo", size="9", id="lasso-select-heading"),
            rx.box(
                LassoSelect(
                    src="https://picsum.photos/400/500",
                    value=State.selected_points,
                    on_change=State.set_points,
                    disabled=False,
                    on_complete=lambda: None,
                ),
                id="lasso-select",
            ),
            rx.text("Selected Points:"),
            rx.text(State.selected_points_string, id="selected-points"),
            align="center",
            spacing="7",
        ),
        height="100vh",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
