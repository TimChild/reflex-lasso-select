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

    # Calculate specific positions to click
    click_x_start = bounding_box['x'] + 10  # 10 pixels from the left
    click_y_start = bounding_box['y'] + 20  # 20 pixels from the top

    click_x_end = bounding_box['x'] + 50  # 50 pixels from the left
    click_y_end = bounding_box['y'] + 60  # 60 pixels from the top

    # Use the mouse to click at the specific positions
    page.mouse.click(click_x_start, click_y_start)
    page.mouse.down()
    page.mouse.click(click_x_end, click_y_end)
    page.mouse.up()

    # Check if the selected points are updated
    selected_points = page.locator("#selected-points")
    expect(selected_points).not_to_have_text("[]")
    # Check if the selected points are updated with the expected coordinates
    expected_text = f"[{{'x': {click_x_start}, 'y': {click_y_start}}}, {{'x': {click_x_end}, 'y': {click_y_end}}}]"
    expect(selected_points).to_have_text(expected_text)
