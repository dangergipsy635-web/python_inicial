from selenium import webdriver
from selenium.webdriver.common.by import by
from selenium.webdriver.common.keys import keys
import time 

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

web_element = driver.find_element(By.NAME, ´q´)
web_element.send_key("Selenium Webdriver" + keys.ENTER)

time.sleep(30)