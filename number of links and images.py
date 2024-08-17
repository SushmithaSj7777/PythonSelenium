from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.implicitly_wait(7)
print(driver.title)

linklist = driver.find_elements(By.TAG_NAME, 'a')
print(len(linklist))

for links in linklist:
    linkstext=links.text
    print(linkstext)

images = driver.find_elements(By.TAG_NAME,'img')
print(len(images))

