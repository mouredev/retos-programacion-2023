'''/*
 * El día 128 del año celebramos en la comunidad el "Hola Mundo day"
 * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
 *
 * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
 * del día 8. Mostrando hora e información de cada uno.
 * Ejemplo: "16:00 | Bienvenida"
 *
 * Se permite utilizar librerías que nos faciliten esta tarea.
 *
 */'''
 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # sirve para actualizar el driver
from selenium.webdriver.common.by import By
import os
import pandas as pd
import time

url ="https://holamundo.day/"

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
except:
#forma tradicional
    try:
        driver_service = Service(executable_path=driver_path)
        driver = webdriver.Chrome(service=driver_service)
    except:
        print("el controlador del Chrome está edsactualizado, descargue")
        print(" la versión Latest stable release:, de https://chromedriver.chromium.org/home")
        time.sleep(30)
        quit()
driver.get(url)
time.sleep(10)
driver.maximize_window()
articulo = driver.find_element(By.XPATH, '//*[@id="section-37c93060-be70-11ed-a6a0-03f7635e8df3"]/div[2]/div/article')
lineas = articulo.text.split("\n")
dia = 0
for linea in lineas:
    if dia == 8:
        print(linea)
        if "Despedida" in linea:
            dia = 9
    if "Agenda 8 de mayo" in linea:
        dia = 8
driver.quit()
    