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

    page.pause()

    # Check initial value of selected points
    expect(selected_points).to_have_text("[]")

    # Simulate a lasso selection
    page.mouse.move(100, 100)
    page.mouse.down()
    page.mouse.move(200, 200)
    page.mouse.up()

    # Check if the selected points are updated
    selected_points = page.locator('#selected-points')
    expect(selected_points).not_to_have_text("[]")
