import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

allure.severity(allure.severity_level.NORMAL)


class TestHRM:
    allure.severity(allure.severity_level.CRITICAL)

    def test_logo(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.orangehrm.com/")
        status = self.driver.find_element(By.XPATH,
                                          "//img[@src='/public/_resources/themes/orangehrm/dist/images/OrangeHRM_Logo.svg']").is_displayed()
        if status:
            allure.attach(self.driver.get_screenshot_as_png(), name="logo_test", attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert True

        else:
            self.driver.close()
            assert False

    allure.severity(allure.severity_level.MINOR)

    def test_listemployees(self):
        pytest.skip("Implement later")

    allure.severity(allure.severity_level.NORMAL)

    def test_Login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        allure.attach(self.driver.get_screenshot_as_png(), name="test login screen",
                      attachment_type=AttachmentType.PNG)
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        act_title = self.driver.title
        print(act_title)
        if act_title == "OrangeHRM":
            self.driver.close()
            assert True
        else:

            self.driver.close()
            assert False
