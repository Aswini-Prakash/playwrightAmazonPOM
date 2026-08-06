print("conftest loaded")

import pytest

@pytest.fixture
def navigate_to_amazon(page):
    page.goto("https://www.amazon.in/")
    