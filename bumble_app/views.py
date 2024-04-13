from django.http import HttpResponse
# Create your views here.
# views.py
from django.shortcuts import redirect, render
from .forms import RegistrationForm
from django.http import JsonResponse
import threading
from selenium.webdriver.support import expected_conditions as EC
import shutil
import os
from django.conf import settings
import random
from PIL import Image
from io import BytesIO
# import request

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
import requests
import time
import pytesseract
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

def handle_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Aquí iría la lógica para iniciar el proceso con Selenium en un hilo separado
            # Por ejemplo, podrías llamar a una función que haga el trabajo con Selenium
            # y pasarle los datos del formulario como argumentos
            threading.Thread(target=registro_cookies, args=(request, form.cleaned_data,)).start()
            # return JsonResponse({'message': 'Espere hasta que se le solicite el código de verificación'})
            return redirect('form2')
    else:
        form = RegistrationForm()
    
    return render(request, 'bumble_app/registration.html', {'form': form})





def registro_cookies(request, phone_number):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--lang=es-ES")
        chrome_options.add_argument("--no-sandbox")
        print('1')
        download_dir = '/home/yandivd/'
        print('2')
        profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
                   # Disable Chrome's PDF Viewer
                   "download.default_directory": download_dir, "plugins.always_open_pdf_externally": True,
                   "download.extensions_to_open": "applications/pdf"}
        chrome_options.add_experimental_option("prefs", profile)
        print('3')
        driver_path = '/usr/local/share/chromedriver'
        driver = webdriver.Chrome(options=chrome_options)

        driver.set_window_size(1800, 768)  # Establece el tamaño de la ventana
        print('4')
        size = driver.get_window_size()
        width = size['width']
        height = size['height']
        phone_number=phone_number['phone_number']
        print(f"Ancho: {width}, Alto: {height}")
        print('phone_number',phone_number)

        from selenium.webdriver.common.by import By
        print('5')
        driver.get("https://us1.bumble.com/en-us/")
        # driver.add_cookie({"name": "first_web_visit_id", "value": "69f9cb3515a865ad000c81f19920eaff3006f19f"})
        # driver.refresh()

        time.sleep(random.uniform(2, 4))
        print('6')
        # Cargar la cookie desde un archivo
        with open('cookies_celular_adil.json', 'r') as cookie_file:
            cookies = json.load(cookie_file)
            for cookie in cookies:
                if 'expiry' in cookie:
                    del cookie['expiry']  # Selenium no acepta la clave 'expiry'
                driver.add_cookie(cookie)

        # WebDriverWait(driver, 10).until(lambda d: d.current_url == expected_url)
        driver.get("https://us1.bumble.com/app")
        # codigo_fuente = driver.page_source
        # print(codigo_fuente)

        time.sleep(random.uniform(10, 16))
        print('7')
        texto_buscado = "cell phone number"

        # Usa XPath para buscar cualquier elemento que contenga el texto
        elementos = driver.find_elements(By.XPATH,f"//*[contains(text(), '{texto_buscado}')]")

        # Verifica si se encontró algún elemento con el texto
        if elementos:
            print("El texto fue encontrado en la página.")
            # Aquí puedes proceder con las acciones adicionales que necesites realizar
            input_element = driver.find_element(By.ID,"phone")
            input_element.send_keys(phone_number)

            time.sleep(random.uniform(2, 4))
            continue_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Continue')]"))
            )
            continue_button.click()
            time.sleep(random.uniform(3, 5))
            ###leer sourcecode
            print("cell passed")
            time.sleep(random.uniform(6, 10))
            print('8')


            html_content = driver.page_source

            # Usar BeautifulSoup para extraer la URL de la imagen
            soup = bs(html_content, 'html.parser')
            print(soup)

            #captcha_element = driver.find_element(By.XPATH, '//*[contains(text(), "captcha_url")]')

            # Obtiene el texto del elemento
            #captcha_url_text = captcha_element.text

            # Extrae la URL del captcha del texto (puedes utilizar expresiones regulares u otras técnicas según el formato)
            #captcha_url = captcha_url_text.split('"')[3]

            #print("URL del captcha:", captcha_url)



            time.sleep(random.uniform(10, 15))
            # pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
            try:
                texto_buscado = "captcha__image"
                captcha__image = driver.find_elements(By.XPATH, f"//*[contains(text(), '{texto_buscado}')]")
                
                if captcha__image:
                    print("Encontrado texto captcha__image")
                    img_src = soup.find('img', {'class': 'captcha__image'})['src']
                    print('img_src=', img_src)
                    input_element = driver.find_element(By.ID, 'miInput')
                    return render(request, 'registration.html', {'img_src': img_src})
                else:
                    print("No encontró imagen de captcha")

                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//img[contains(@src, "https://us1.bumble.com/hidden?euri=")]')))
                
                img_element = driver.find_element(By.XPATH, '//img[contains(@src, "https://us1.bumble.com/hidden?euri=")]')
                img_src = img_element.get_attribute("src")
                print("URL de la imagen:", img_src)
                # Extraer solo la parte de la ruta de la imagen de la URL
                img_path = img_src.split('https:/us1.bumble.com/')[-1]

                # Construir la URL completa de la imagen
                full_img_url = f"https://us1.bumble.com/{img_path}"

                # Descargar la imagen del captcha
                response = requests.get(full_img_url)
                # Verificar si la respuesta es exitosa
                # Verificar si la respuesta es exitosa
                if response.status_code == 200:
                    # Guardar la imagen del CAPTCHA
                    with open('captcha_image.png', 'wb') as img_file:
                        img_file.write(response.content)
                    print("Imagen del captcha guardada como captcha_image.png")

                    # Construye la ruta completa de la imagen
                    image_path = os.path.join(settings.MEDIA_ROOT, 'captcha_image.png')

                    # Mover la imagen a la carpeta 'media'
                    shutil.move('captcha_image.png', image_path)
                
                else:
                    print('Error al descargar la imagen del captcha')
                # img = Image.open(BytesIO(response.content))

                # Procesar la imagen con pytesseract
                # captcha_text = pytesseract.image_to_string(img)

                # Introduce el texto del captcha en el input
                # input_element = driver.find_element(By.NAME, 'captcha')
                # input_element.send_keys(captcha_text)
                
                # print("Texto del captcha:", captcha_text)
            except Exception as e:
                print(f"Error: {e}")
                print("No encontró imagen de captcha en ninguno de los métodos")

            # try:
            #     texto_buscado = "Next, please enter the 6-digit code we just sent you"
                
            #     # Espera explícita para el texto buscado
            #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{texto_buscado}')]")))
                
            #     elementos2 = driver.find_elements(By.XPATH, f"//*[contains(text(), '{texto_buscado}')]")
                
            #     if elementos2:
            #         threading.Thread(target=mostrar_inputs, args=(request,)).start()
            #     else:
            #         print("El texto no fue encontrado en la página.")
                    
            # except Exception as e:
            #     print(f"Error: {e}")




def mostrar_inputs(request):
    if request.method == 'POST':
        # Procesa los datos del formulario, incluido el valor del captcha
        # Realiza las acciones necesarias, como guardar las cookies
        return HttpResponse("Datos recibidos y procesados correctamente.")
    else:
        return render(request, 'mostrar_inputs.html')

import base64
def form2(request):
    return render(request,'bumble_app/form2.html')



'''
<div class="text-field text-field--full-rounded" data-qa-role="textfield-container"><input type="text" class="text-field__input" autocomplete="digit" maxlength="1" size="5" data-qa-role="textfield-input" dir="auto" value=""></div>

<div class="code-field__digit"><div class="text-field text-field--full-rounded" data-qa-role="textfield-container"><input type="text" class="text-field__input" autocomplete="digit" maxlength="1" size="5" data-qa-role="textfield-input" dir="auto" value=""></div></div>
<div class="code-field__digit"><div class="text-field text-field--full-rounded" data-qa-role="textfield-container"><input type="text" class="text-field__input" autocomplete="digit" maxlength="1" size="5" data-qa-role="textfield-input" dir="auto" value=""></div></div>

<div class="code-field__digit"><div class="text-field text-field--full-rounded" data-qa-role="textfield-container"><input type="text" class="text-field__input" autocomplete="digit" maxlength="1" size="5" data-qa-role="textfield-input" dir="auto" value=""></div></div>
<div class="code-field__digit"><div class="text-field text-field--full-rounded" data-qa-role="textfield-container"><input type="text" class="text-field__input" autocomplete="digit" maxlength="1" size="5" data-qa-role="textfield-input" dir="auto" value=""></div></div>

<div class="code-field__digit"><div class="text-field text-field--full-rounded" data-qa-role="textfield-container"><input type="text" class="text-field__input" autocomplete="digit" maxlength="1" size="5" data-qa-role="textfield-input" dir="auto" value=""></div></div>'''