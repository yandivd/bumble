from selenium.webdriver.support import expected_conditions as EC
import random
#Vzmj230312@@00 secure1.store.apple.co CORRRCTO
# BoujmaElalami8456#$,0! icloud

#idmsa.apple.com gmail Vzmj230312



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


# Configurar opciones de Chrome


latitude = 40.7128  # Por ejemplo, latitud de Nueva York
longitude = -74.0060  # Por ejemplo, longitud de Nueva York
accuracy = 100  # Precisión en metros


def coneccion_driver_extension_location():
    latitude = 40.7128  # Por ejemplo, latitud de Nueva York
    longitude = -74.0060  # Por ejemplo, longitud de Nueva York
    accuracy = 100  # Precisión en metros
    ruta_extension = 'GKOJFKHLEKIGHIKAFCPJKIKLFBNLMEIO_1_219_646_0.crx'
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-dev-shm-usage')
    download_dir = 'C:\\Users\\jmzv1\\Dropbox\\toshiba 2021 F\\webscraping_contraloria\\escritos2\\'

    profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],  # Disable Chrome's PDF Viewer
               "download.default_directory": download_dir, "plugins.always_open_pdf_externally": True,
               "download.extensions_to_open": "applications/pdf",         "download.prompt_for_download": False,
             "download.directory_upgrade": True,     "safebrowsing.enabled": True,
               "profile.default_content_settings.popups": 0,
               "download.default_directory": "path_to_download_folder",  # UPDATE THIS
               "download.prompt_for_download": False,
               "download.directory_upgrade": True,
               "safebrowsing_for_trusted_sources_enabled": False,
               "safebrowsing.enabled": False,
               "profile.default_content_setting_values.geolocation": 1
               }

    chrome_options.add_experimental_option("prefs", profile)
    chrome_options.add_extension(ruta_extension)
    chrome_options.add_argument("--lang=es-ES")
    driver_path = 'C:\\Users\\jmzv1\\Dropbox\\toshiba 2021 F\\PycharmProjects\\bumble\\bumble_app\\chromedriver.exe'

    servicio = Service('C:\\Users\\jmzv1\\Dropbox\\toshiba 2021 F\\PycharmProjects\\bumble\\bumble_app\\chromedriver.exe')

    driver = webdriver.Chrome(service=servicio, options=chrome_options)

    driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
        "latitude": latitude,
        "longitude": longitude,
        "accuracy": accuracy
    })


    from selenium.webdriver.common.by import By

    driver.get("https://hola.org/")
    time.sleep(random.uniform(12, 18))

    #time.sleep(random.uniform(120, 180))

    try:
        # Espera hasta que el elemento sea visible y luego haz clic en él
        elemento = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="content_of_consent"]/div[3]/button[3]'))
        )
        elemento.click()
        print("Elemento cookies clickeado.")
    except Exception as e:
        print("Error al clickear el elemento cookies:", e)

    time.sleep(random.uniform(12, 18))


    try:
        # Localizar el elemento input por sus atributos y enviar la URL
        input_element = driver.find_element(By.CSS_SELECTOR, "input.hola_input.hola_input--xl.hola_input--has_icon.hola_input_icon--md")

        input_element.send_keys('www.bumble.com')
        print("URL ingresada en el campo.")
    except Exception as e:
        print("Error al ingresar la URL en el campo:", e)

    time.sleep(random.uniform(5, 9))

    try:
        # Espera hasta que el elemento sea visible y luego haz clic en él
        elemento = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="page_content_wrapper"]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/div/div'))
        )
        elemento.click()
        print("Elemento url clickeado.")
    except Exception as e:
        print("Error al clickear el elemento url:", e)

    time.sleep(random.uniform(50, 64))


    try:
        # Espera a que el iframe esté presente y luego cambia al contexto del iframe
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "#sp_message_iframe_971214"))
        )

        # Ahora que estamos en el contexto del iframe, busca y haz clic en el botón
        WebDriverWait(driver, 10).until(
            #EC.visibility_of_element_located((By.XPATH, "//button[@title='Accept All']"))
            EC.visibility_of_element_located((By.XPATH, "//button[@title='Aceptar cookies']"))
        ).click()
        print("Botón  Accept All clickeado.")
    except Exception as e:
        print("Error al clickear el botón Accept All:", e)
    finally:
        # Vuelve al contenido principal de la página
        driver.switch_to.default_content()
    time.sleep(random.uniform(5, 8))



    try:
        # Espera hasta que el elemento con la clase 'apple-button__text' que contiene el texto sea clickeable
        boton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@class, 'button') and contains(@class, 'button--block') and contains(@class, 'button--secondary') and contains(@class, 'js-event-link')][.//span[contains(text(), 'Entrar')]]"))
        )
        boton.click()
        # Realiza aquí más acciones si es necesario

        print("Botón  enter clickeado.")
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

    except Exception as e:
        print("Error al interactuar con el botón signin:", e)

    time.sleep(random.uniform(4, 8))

    try:
        # Localiza el campo de entrada por su ID y envía el texto
        campo_password = driver.find_element(By.ID, "password_text_field")
        campo_password.send_keys("Vzmj230312@@00")

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
        else:
            print("El código debe tener 6 dígitos.")

    except Exception as e:
        print("o aparecion elemento para  el codigo:", e)

    time.sleep(random.uniform(10, 14))

    try:
        # Espera hasta que el elemento con el texto 'Confiar' sea clickeable
        boton_confiar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Confiar')]"))
        )
        boton_confiar.click()
        # Realiza aquí más acciones si es necesario

    except Exception as e:
        print("Error al interactuar con el botón:", e)

    time.sleep(random.uniform(6, 8))

    try:
        # Espera hasta que el botón con las clases especificadas sea clickeable
        boton_continuar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.button.button-primary.last.nav-action.pull-right.weight-medium"))
        )
        boton_continuar.click()
        # Realiza aquí más acciones si es necesario

    except Exception as e:
        print("Error al interactuar con el botón continuar:", e)












    try:
        # Espera hasta que el elemento sea visible y luego haz clic en él
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@src='./bext/vpn/ui/flags/us.svg']"))
        )
        element.click()
        print("Elemento USA clickeado.")
    except Exception as e:
        print("Error al clickear el elemento USA:", e)

    time.sleep(random.uniform(7, 12))



    try:
        # Espera hasta que el elemento sea visible y luego haz clic en él
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@src='./bext/vpn/ui/flags/us.svg']"))
        )
        element.click()
        print("Elemento clickeado.")
    except Exception as e:
        print("Error al clickear el elemento:", e)

    time.sleep(random.uniform(7, 12))

    try:
        # Localizar el elemento por su atributo placeholder y enviar el texto
        input_element = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        input_element.send_keys('Morocco')
        input_element.send_keys(Keys.RETURN)  # Si necesitas presionar Enter después de escribir
        print("Texto ingresado en el campo.")
    except Exception as e:
        print("Error al ingresar texto en el campo:", e)



    time.sleep(20)

    #driver.get("https://fr1.bumble.com/get-started")


    time.sleep(random.uniform(7, 12))
    try:
        # Espera a que el iframe esté presente y luego cambia al contexto del iframe
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "#sp_message_iframe_971214"))
        )

        # Ahora que estamos en el contexto del iframe, busca y haz clic en el botón
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@title='Accept All']"))
        ).click()
        print("Botón clickeado.")
    except Exception as e:
        print("Error al clickear el botón:", e)
    finally:
        # Vuelve al contenido principal de la página
        driver.switch_to.default_content()
    time.sleep(random.uniform(5, 8))

    time.sleep(40)

    try:
        # Espera hasta que el elemento sea visible y luego haz clic en él
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='action text-break-words' and text()='Use cell phone number']"))
        ).click()
        print("Elemento clickeado.")
    except Exception as e:
        print("Error al clickear el elemento:", e)

    numero = int(random.uniform(1, 4))
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

    time.sleep(3000)


coneccion_driver_extension_location()