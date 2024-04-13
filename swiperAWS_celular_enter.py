from selenium.webdriver.support import expected_conditions as EC
import random
#Vzmj230312@@00 secure1.store.apple.co CORRRCTO
# BoujmaElalami8456#$,0! icloud

#idmsa.apple.com gmail Vzmj230312
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as bs
#import pyautogui
#pyautogui.FAILSAFE = False
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, \
    ElementClickInterceptedException
import time



# chrome_options.add_argument("--headless")

# prmero uso selenium
#https://us1.bumble.com/app
import re
import time

import requests
import http.cookiejar
# Configurar opciones de Chrome


latitude = 40.7128  # Por ejemplo, latitud de Nueva York
longitude = -74.0060  # Por ejemplo, longitud de Nueva York
accuracy = 100  # Precisión en metros

sender_email = "jmzv13@gmail.com"
receiver_email = "writetoadil@gmail.com, jmzv13@gmail.com"
password = "jcdd gmrd ntgu cmsh"


def send_email(number):
    date = datetime.now().strftime("%B-%d-%Y %H:%M")
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Bumble Report"

    body = (f" Hello Adil: \n\n"
            f" Here is the report for today's swiping:\n\n "
            f" Bumble delivered this message:'You're All Caught Up.'\n\n "
            f"Location: Morocco\n"
            f"Swiping finished today, {date}\n"
            f"We swiped {number} times\n"
            f"{number} swipes right\n"
            f" 0 swipes left")

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

    print("Email1 enviado.")

def send_email2(number):
    date = datetime.now().strftime("%B-%d-%Y %H:%M")
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Bumble Report"

    body = (f" Hello Adil: \n\n"
            f" Here is the report for today's swiping: \n\n"
            
            f"Location: Morocco\n"
            f"Swiping finished today, {date}\n"
            f"We swiped {number} times\n"
            f"{number} swipes right\n"
            f" 0 swipes left")

    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

    print("Email2 enviado.")

def coneccion_driver_extension_location():
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--lang=es-ES")
    chrome_options.add_argument("--no-sandbox")



    download_dir = 'C:\\Users\\jmzv1\\Dropbox\\toshiba 2021 F\\webscraping_contraloria\\escritos2\\'

    profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],  # Disable Chrome's PDF Viewer
               "download.default_directory": download_dir, "plugins.always_open_pdf_externally": True,
               "download.extensions_to_open": "applications/pdf"}
    chrome_options.add_experimental_option("prefs", profile)


    driver_path = 'C:\\Users\\encue\\Dropbox\\toshiba 2021 F\\PycharmProjects\\dashboard\\chromedriver.exe'
    driver = webdriver.Chrome(options=chrome_options)

    driver.set_window_size(1800, 768)  # Establece el tamaño de la ventana

    size = driver.get_window_size()
    width = size['width']
    height = size['height']

    print(f"Ancho: {width}, Alto: {height}")

    from selenium.webdriver.common.by import By

    driver.get("https://us1.bumble.com/en-us/")
    #driver.add_cookie({"name": "first_web_visit_id", "value": "69f9cb3515a865ad000c81f19920eaff3006f19f"})
    #driver.refresh()

    time.sleep(random.uniform(2, 4))

    # Cargar la cookie desde un archivo
    with open('cookies_celular_adil_22_03.json', 'r') as cookie_file:
        cookies = json.load(cookie_file)
        for cookie in cookies:
            if 'expiry' in cookie:
                del cookie['expiry']  # Selenium no acepta la clave 'expiry'
            driver.add_cookie(cookie)
    print("puso las cookies")

    #WebDriverWait(driver, 10).until(lambda d: d.current_url == expected_url)
    driver.get("https://us1.bumble.com/app")
    #codigo_fuente = driver.page_source
    #print(codigo_fuente)


    time.sleep(random.uniform(10, 16))



    actions = ActionChains(driver)

    # Mueve el cursor a la posición (680, 706) y realiza un clic
    #actions.move_by_offset(1280, 244).click().perform()

    #time.sleep(random.uniform(100, 120))







    numero1 = int(random.uniform(75, 85))
    for x in  range(numero1):
        numero = int(random.uniform(1, 3))
        for x in range(numero):
            actions = ActionChains(driver)
            actions.send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(random.uniform(1, 3))

        try:
            # Espera hasta que el elemento sea visible y luego haz clic en él
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, ".encounters-action.encounters-action--like[data-qa-role='encounters-action-like']"))
            ).click()
            print("Elemento clickeado.")
        except Exception as e:
            print("Error al clickear el elemento:", e)
            time.sleep(3)

        try:
            elemento_span = driver.find_element(By.XPATH, "//span[text()='Continue Bumbling']")

            # Haz clic en el elemento
            elemento_span.click()
            time.sleep(random.uniform(1, 5))

        except Exception as e:
            print("Ocurrió un error: Continue bumbling", e)

        time.sleep(random.uniform(3, 5))
        time.sleep(random.uniform(30, 35))
        try:
            # Reemplaza 'tu_selector' por el método de selección apropiado y su valor
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[text()='You’re all caught up!']"))
            )
            if element:
                send_email(numero1)
                break
        except Exception as e:
            print("no encuentra el cauthup, contiinua swiping")
            continue

    send_email2(numero1)
coneccion_driver_extension_location()

'''    cookies = driver.get_cookies()

    # Save the cookies to a JSON file
    with open("cookies_celular_adil.json", "w") as cookie_file:
        json.dump(cookies, cookie_file)

    time.sleep(random.uniform(2, 5))

    print("cookies guardadas")'''