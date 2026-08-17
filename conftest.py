print("conftest loaded")

import allure
import pytest

@pytest.fixture
def navigate_to_amazon(page):
    page.goto("https://www.amazon.in/")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if report.failed:
        page = item.funcargs.get("page")
        if page:
            allure.attach(page.screenshot(),
                          name="failedpage",
                          attachment_type=allure.attachment_type.PNG)