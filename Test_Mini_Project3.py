import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

allure.severity(allure.severity_level.CRITICAL)


class Mini_Project_3:
    def __init__(self):
        self.driver = None

    @allure.severity(allure.severity_level.NORMAL)
    def test_launch_website(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.idrive360.com/enterprise/login")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "username").send_keys('augtest_040823@idrive.com')
        self.driver.find_element(By.ID, "password").send_keys('123456')
        self.driver.find_element(By.ID, 'frm-btn').click()
        self.driver.implicitly_wait(7)

    @allure.severity(allure.severity_level.NORMAL)
    def test_verifyURL(self):
        assert self.driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"
        allure.attach(self.driver.get_screenshot_as_png(), name='CurrentURL',
                      attachment_type=AttachmentType.PNG)

    @allure.severity(allure.severity_level.NORMAL)
    def test_validity(self):
        freetrail = self.driver.find_element(By.XPATH, "//div[@id='upgrade']//span[1]")
        print(freetrail.text)
        if freetrail.text == "Your free trial expires in":
            print("enjoy free trail")
        elif freetrail.text == "Your free trial has expired":
            print("Upgrade Now!")
