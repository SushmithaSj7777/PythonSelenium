import webdriver_manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

browser = input("Enter the browser you want to use \n")

if browser=='chrome':
    driver=webdriver.Chrome(ChromeDriverManager().install())
elif:
    driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())

