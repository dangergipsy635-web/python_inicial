from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, os

driver = webdriver.Chrome()
driver.get("https://identidad.mtess.gov.py/alumno/register.php")

campo_cedula = driver.find_element(By.NAME, 'value_cedula_1')
time.sleep(2)
campo_cedula.send_keys("4641375" + Keys.ENTER)
time.sleep(2)

mensaje_campo = driver.find_element(By.ID, "DenyDuplicatedcedula_1")
contenido = mensaje_campo.get_attribute("innerHTML")

if(contenido != ""):
    nombre = driver.find_element(By.ID, "readonly_value_nombre_1")
    nombre = campo.get_attribute("value")
    apellido = driver.find_element(By.ID, "readonly_value_apellido_1")
    apellido = campo.get_attribute("value")
    f = open("data.txt", "a")
    f.write(f"{nombre} {apellido}")
    f.write("\n")
    f.close()
driver.quit()
