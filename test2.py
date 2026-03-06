from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import keys
import time

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")

web_element = driver.find_element(By.NAME, ´search´)
web_element.send_keys("Python" + keys.ENTER)

time.sleep(30)
