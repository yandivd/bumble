from selenium.webdriver.support import expected_conditions as EC
import random
#Vzmj230312@@00 secure1.store.apple.co CORRRCTO
# BoujmaElalami8456#$,0! icloud

#idmsa.apple.com gmail Vzmj230312

import json

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

import re
import time

import requests
import http.cookiejar
# Configurar opciones de Chrome


latitude = 40.7128  # Por ejemplo, latitud de Nueva York
longitude = -74.0060  # Por ejemplo, longitud de Nueva York
accuracy = 100  # Precisión en metros



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

    driver.get("https://fr1.bumble.com/en-us/")
    #driver.add_cookie({"name": "first_web_visit_id", "value": "69f9cb3515a865ad000c81f19920eaff3006f19f"})
    #driver.refresh()

    expected_url = "https://fr1.bumble.com/en-us/"
    actual_url = driver.current_url
    print(actual_url)
    if actual_url == expected_url:
        print("Estás en la URL correcta.")
    else:
        print("No estás en la URL correcta.")

    # Cargar la cookie desde un archivo
   # with open('cookies.json', 'r') as cookie_file:
  #      cookies = json.load(cookie_file)
    #    for cookie in cookies:
      #      if 'expiry' in cookie:
     #           del cookie['expiry']  # Selenium no acepta la clave 'expiry'
     #       driver.add_cookie(cookie)

    #WebDriverWait(driver, 10).until(lambda d: d.current_url == expected_url)
   # driver.get("https://fr1.bumble.com/app")
    codigo_fuente = driver.page_source
    #print(codigo_fuente)


    time.sleep(random.uniform(4, 8))



    actions = ActionChains(driver)

    # Mueve el cursor a la posición (680, 706) y realiza un clic
    actions.move_by_offset(1280, 244).click().perform()

    time.sleep(random.uniform(6, 8))

    try:
        # Espera a que el iframe esté presente y luego cambia al contexto del iframe
        WebDriverWait(driver, 10).until(
            #EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "#sp_message_iframe_971214"))
            EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "#sp_message_iframe_971200"))
        )

        # Ahora que estamos en el contexto del iframe, busca y haz clic en el botón
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@title='Accept All']"))
            #EC.visibility_of_element_located((By.XPATH, "//button[@title='Aceptar cookies']"))
        ).click()
        print("Botón  Accept All clickeado.")
    except Exception as e:
        print("Error al clickear el botón Accept All:", e)
    finally:
        # Vuelve al contenido principal de la página
        driver.switch_to.default_content()
    time.sleep(random.uniform(5, 8))

    time.sleep(random.uniform(5, 8))


    try:
        # Espera hasta que el elemento sea visible y luego haz clic en él
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[@class='action text-break-words' and text()='Use cell phone number']"))
        ).click()
        print("Elemento clickeado.")
    except Exception as e:
        print("Error al clickear el elemento:", e)




    try:
        # Espera hasta que el elemento con la clase 'apple-button__text' que contiene el texto sea clickeable
        enlace_sign_in = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@data-seo-label='sign-in']"))
        )

        # Hacer clic en el enlace "Sign In"
        enlace_sign_in.click()
        # Realiza aquí más acciones si es necesario

        print("Botón  sign In clickeado.")
    except Exception as e:
        print("Error al interactuar con el botón enter:", e)

    time.sleep(random.uniform(5, 8))



    try:
        # Esperar a que el elemento sea clickeable y luego hacer clic
        boton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "apple-button__text"))
        )
        boton.click()
        print("Botón  apple clickeado.")
        # Continuar con más acciones después del clic si es necesario

    except Exception as e:
        print("Error al interactuar con el botón apple:", e)

    time.sleep(random.uniform(10, 15))

    wait = WebDriverWait(driver, 10)
    wait.until(EC.number_of_windows_to_be(2))  # Espera a que haya dos ventanas abiertas

    # Cambiar al contexto de la nueva ventana (popup) o nuevo contexto
    ventanas = driver.window_handles
    driver.switch_to.window(ventanas[1])  # Cambiar al segundo contexto, ajusta el índice según sea necesario

    time.sleep(random.uniform(4, 6))
    elemento_input = driver.find_element(By.ID, 'account_name_text_field')

    # Limpiar cualquier texto existente en el input
    elemento_input.clear()

    # Ingresar el texto "jmz@gmail.com" en el input
    elemento_input.send_keys('jose_zapata@ksg07.harvard.edu')

    time.sleep(random.uniform(4, 6))

    try:
        # Espera hasta que el botón con el ID 'sign-in' sea clickeable
        boton_continuar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "sign-in"))
        )
        boton_continuar.click()
        # Realiza aquí más acciones si es necesario
        print("Botón ID apple clicked.")

    except Exception as e:
        print("Error al interactuar con el botón signin:", e)

    time.sleep(random.uniform(4, 8))

    try:
        # Localiza el campo de entrada por su ID y envía el texto
        campo_password = driver.find_element(By.ID, "password_text_field")
        campo_password.send_keys("Vzmj230312@@00")
        print("Password entered")

        # Realiza aquí más acciones si es necesario

    except Exception as e:
        print("Error al interactuar con el campo de entrada: password", e)

    time.sleep(random.uniform(4, 8))



    try:
        # Espera hasta que el botón con el ID 'sign-in' sea clickeable
        boton_iniciar_sesion = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "sign-in"))
        )
        boton_iniciar_sesion.click()
        # Realiza aquí más acciones si es necesario
        print("Botón sign in apple clicked.")

    except Exception as e:
        print("Error al interactuar con el botón:", e)

    time.sleep(random.uniform(4, 8))



    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "char0"))
        )

        # Pedir al usuario que ingrese el código de verificación
        codigo_verificacion = input("Por favor, introduce el código de verificación: ")

        # Asegúrate de que el código tiene 6 dígitos
        if len(codigo_verificacion) == 6:
            for i, digito in enumerate(codigo_verificacion):
                campo = driver.find_element(By.ID, f"char{i}")
                campo.send_keys(digito)
            print("Verification code accepted.")
        else:
            print("El código debe tener 6 dígitos.")

    except Exception as e:
        print("no aparecion elemento para  el codigo:", e)

    time.sleep(random.uniform(10, 14))

    try:
        # Espera hasta que el elemento con el texto 'Confiar' sea clickeable
        boton_confiar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Confiar')]"))
        )
        boton_confiar.click()
        print("Botón trust clicked.")
        # Realiza aquí más acciones si es necesario

    except Exception as e:
        print("Error al interactuar con el botón: trust", e)

    time.sleep(random.uniform(6, 8))

    try:
        # Espera hasta que el botón con las clases especificadas sea clickeable
        boton_continuar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.button.button-primary.last.nav-action.pull-right.weight-medium"))
        )
        boton_continuar.click()
        # Realiza aquí más acciones si es necesario
        print("Botón continue clicked.")

    except Exception as e:
        print("Error al interactuar con el botón continuar:", e)

    time.sleep(random.uniform(10, 14))
    driver.switch_to.window(ventanas[0])
    print("Swiping started!!")

    cookies = driver.get_cookies()

    # Save the cookies to a JSON file
    with open("cookies2.json", "w") as cookie_file:
        json.dump(cookies, cookie_file)

    numero1 = int(random.uniform(80, 100))
    for x in  range(numero1):
        numero = int(random.uniform(2, 6))
        for x in range(numero):
            actions = ActionChains(driver)
            actions.send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(random.uniform(1, 5))

        try:
            # Espera hasta que el elemento sea visible y luego haz clic en él
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, ".encounters-action.encounters-action--like[data-qa-role='encounters-action-like']"))
            ).click()
            print("Elemento clickeado.")
        except Exception as e:
            print("Error al clickear el elemento:", e)
            time.sleep(300)

        time.sleep(random.uniform(5, 120))


coneccion_driver_extension_location()