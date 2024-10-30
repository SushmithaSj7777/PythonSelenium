import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(7)
driver.maximize_window()
print("Title of the webpage %s" % driver.title)
Radiobtn = driver.find_element(By.XPATH, "//input[@value='radio2']")
Radiobtn.click()
assert Radiobtn.is_selected()
autosuggest = driver.find_element(By.XPATH, "//input[@placeholder='Type to Select Countries']")
autosuggest.send_keys("Ind")
autosuggest2 = driver.find_elements(By.XPATH, "//ul[@id='ui-id-1'][1]/li")
print(len(autosuggest2))
for country in autosuggest2:
    if country.text == 'India':
        country.click()
        break
print(autosuggest.text)

dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#dropdown-class-example"))
dropdown.select_by_visible_text("Option3")
checkbox = driver.find_element(By.CSS_SELECTOR, "#checkBoxOption3")
checkbox.click()
driver.find_element(By.XPATH, "//input[@placeholder='Enter Your Name']").send_keys("Sush")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
driver.find_element(By.CSS_SELECTOR, "#openwindow").click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)

