from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(10)
print(driver.title)
driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("Frid")

searchlist = driver.find_elements(By.XPATH, "//div[@class='s-suggestion s-suggestion-ellipsis-direction']")
print(len(searchlist))
for item in searchlist:
    result = item.text
    print(result)
    if item.text == "fridge cover":
        item.click()
        break