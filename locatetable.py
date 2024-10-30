from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
prices = []
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
fruits = driver.find_elements(By.XPATH, "//div[@class='sc-jsEeTM itluUR rdt_TableRow']/div[2]/div")
for fruitloc in fruits:
    fruit = fruitloc.text
    price = driver.find_element(By.XPATH, "//div[text()='" + fruit + "']/following::div[4]").text
    print(fruitloc.text, price)
    prices.append(price)

prices.sort()
for price in prices:
    print(price)

