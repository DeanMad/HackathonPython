from selenium.webdriver.common.by import By

from Extentions.UI_actions_web import WebActions


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def get_user_name(self):
        return self.driver.find_element(By.XPATH, "//input[@id='username']")

    def get_password1(self):
        return self.driver.find_element(By.XPATH, "//input[@id='password']")

    def get_signin_btn(self):
        return self.driver.find_element(By.XPATH, "//button[@data-test='signin-submit']")

