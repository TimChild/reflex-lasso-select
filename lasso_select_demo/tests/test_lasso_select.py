from pathlib import Path
import pytest
import time
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

    # Check initial value of selected points
    selected_points = page.locator("#selected-points")
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
    time.sleep(0.1)
    page.mouse.click(click_x_2, click_y_2)
    time.sleep(0.1)
    page.mouse.click(click_x_3, click_y_3)
    time.sleep(0.1)
    page.mouse.click(click_x_4, click_y_4)
    page.pause()
    # Optionally close the polygon by clicking the start point again
    # page.mouse.click(click_x_start, click_y_start)

    # Check if the selected points are updated with the expected coordinates
    expected_text = (
        f"[{{'x': {rel_x_start}, 'y': {rel_y_start}}}, "
        f"{{'x': {rel_x_2}, 'y': {rel_y_2}}}, "
        f"{{'x': {rel_x_3}, 'y': {rel_y_3}}}, "
        f"{{'x': {rel_x_4}, 'y': {rel_y_4}}}]"
    )
    # Running headless changes the x values to be 1 lower than expected
    expected_text_headless = (
        f"[{{'x': {rel_x_start - 1}, 'y': {rel_y_start}}}, "
        f"{{'x': {rel_x_2 - 1}, 'y': {rel_y_2}}}, "
        f"{{'x': {rel_x_3 - 1}, 'y': {rel_y_3}}}, "
        f"{{'x': {rel_x_4 - 1}, 'y': {rel_y_4}}}]"
    )

    actual_text = selected_points.inner_text()
    # Check if matches headless, otherwise give helpful error message by assert
    if actual_text != expected_text_headless:
        assert actual_text == expected_text
