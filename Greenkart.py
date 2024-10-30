import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
print(driver.title)
driver.maximize_window()
driver.implicitly_wait(7)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search for Vegetables and Fruits']").send_keys('berry')
time.sleep(3)
berrys = driver.find_elements(By.XPATH, "//div[@class='products']/div")
for strawberry in berrys:
    strawberry = str(strawberry.text)
    print(strawberry)
    if 'Strawberry' in strawberry.text:
        driver.find_element(By.XPATH, "div/button").click()
        time.sleep(7)
        continue
