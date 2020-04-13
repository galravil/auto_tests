import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install()
    )
    # Resize the window to the screen width/height
    # driver.set_window_size(1366, 768)
    yield driver
    driver.quit()