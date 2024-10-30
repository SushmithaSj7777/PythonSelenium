from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.hyrtutorials.com/p/add-padding-to-containers.html#google_vignette")
print(driver.title)
driver.implicitly_wait(7)

first_name = driver.find_element(By.XPATH, "//label[contains(text(),'First Name')]/following::input[1]")
first_name.send_keys("Sushmitha")


