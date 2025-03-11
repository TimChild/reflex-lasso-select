from pathlib import Path
import pytest
from playwright.sync_api import Page, expect
from reflex.testing import AppHarness


@pytest.fixture(scope="session")
def lasso_select_app():
    app_root = Path(__file__).parent.parent
    with AppHarness.create(root=app_root) as harness:
        yield harness


def test_lasso_select_render(lasso_select_app: AppHarness, page: Page):
    assert lasso_select_app.frontend_url is not None

    page.goto(lasso_select_app.frontend_url)
    # Check if the heading is correct
    heading = page.locator("#lasso-select-heading")
    expect(heading).to_have_text("Lasso select demo")

    # Check if the lasso select component is visible
    lasso_component = page.locator("#lasso-select")
    expect(lasso_component).to_be_visible()

    selected_points = page.locator("#selected-points")
    page.pause()

    # Check initial value of selected points
    expect(selected_points).to_have_text("[]")

    # Get the bounding box of the lasso component
    bounding_box = lasso_component.bounding_box()
    assert bounding_box is not None

    # Calculate relative positions
    rel_x_start = 10
    rel_y_start = 20

    rel_x_2 = 50
    rel_y_2 = 20

    rel_x_3 = 50
    rel_y_3 = 60

    rel_x_4 = 10
    rel_y_4 = 60

    # Calculate specific positions to click
    click_x_start = bounding_box["x"] + rel_x_start
    click_y_start = bounding_box["y"] + rel_y_start

    click_x_2 = bounding_box["x"] + rel_x_2
    click_y_2 = bounding_box["y"] + rel_y_2

    click_x_3 = bounding_box["x"] + rel_x_3
    click_y_3 = bounding_box["y"] + rel_y_3

    click_x_4 = bounding_box["x"] + rel_x_4
    click_y_4 = bounding_box["y"] + rel_y_4

    # Use the mouse to click at the specific positions to form a polygon
    page.mouse.click(click_x_start, click_y_start)
    page.mouse.click(click_x_2, click_y_2)
    page.mouse.click(click_x_3, click_y_3)
    page.mouse.click(click_x_4, click_y_4)
    page.mouse.click(click_x_start, click_y_start)  # Close the polygon

    # Check if the selected points are updated
    selected_points = page.locator("#selected-points")
    expect(selected_points).not_to_have_text("[]")
    # Check if the selected points are updated with the expected coordinates
    # Calculate relative positions
    rel_x_start = 10
    rel_y_start = 20

    rel_x_2 = 50
    rel_y_2 = 20

    rel_x_3 = 50
    rel_y_3 = 60

    rel_x_4 = 10
    rel_y_4 = 60

    expected_text = (
        f"[{{'x': {rel_x_start}, 'y': {rel_y_start}}}, "
        f"{{'x': {rel_x_2}, 'y': {rel_y_2}}}, "
        f"{{'x': {rel_x_3}, 'y': {rel_y_3}}}, "
        f"{{'x': {rel_x_4}, 'y': {rel_y_4}}}, "
        f"{{'x': {rel_x_start}, 'y': {rel_y_start}}}]"
    )
    expect(selected_points).to_have_text(expected_text)
