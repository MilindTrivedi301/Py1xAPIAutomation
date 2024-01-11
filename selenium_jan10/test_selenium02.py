import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver

def test_open_url_verify_title(driver):
    driver.get("http://app.vwo.com")
    print(driver.title)
    # verification
    # Actual Result == Expected Result
    assert "Login - VWO" == driver.title
