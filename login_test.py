import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from conftest import browser

@pytest.mark.usefixtures("browser")
class LoginTest:
    def login_test(self, browser):
        login_url = "https://www.mojposao.ba/"

        browser.get(login_url)

        username_input = browser.find_element(By.NAME, "username")
        password_input = browser.find_element(By.NAME, "password")

        username_input.send_keys("merzicbelma@gmail.com")
        password_input.send_keys("test123")

        password_input.send_keys(Keys.RETURN)

        time.sleep(3)

        assert "dashboard" in browser.surrent_url.lower()

        browser.quit()


