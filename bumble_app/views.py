from django.http import HttpResponse
# Create your views here.
# views.py
from django.shortcuts import redirect, render
from .forms import RegistrationForm, CaptchaForm, CodeForm
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

from queue import Queue

cola_comandos = Queue()

def guardar_cookies():
    cookies = driver.get_cookies()

    # Save the cookies to a JSON file
    with open("cookies_test.json", "w") as cookie_file:
        json.dump(cookies, cookie_file)

    time.sleep(random.uniform(2, 5))

    print("cookies guardadas")
# region proceso
def handle_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Iniciar el proceso con Selenium en un hilo separado
            threading.Thread(target=registro_cookies, args=(request, form.cleaned_data,)).start()
            while True:
                if not cola_comandos.empty():
                    comando = cola_comandos.get()
                    if comando['tipo'] == 'find_element':
                        element = driver.find_element(By.NAME, comando['name'])
                    elif comando['tipo'] == 'send_keys':
                        element.send_keys(comando['texto'])

                    elif comando['tipo'] == 'find_elementCode':
                        element = driver.find_element(By.CSS_SELECTOR, comando['css_selector'])
                    elif comando['tipo'] == 'send_keysCode':
                        element.send_keys(comando['texto'])
            
            # Devolver una respuesta JSON
            # return JsonResponse({'message': 'Espere hasta que se le solicite el código de verificación'})
    
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
        global driver
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
            time.sleep(random.uniform(10, 15))
            # pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
            try:
                def GetCaptchaImage():
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

                    if response.status_code == 200:
                        # Guardar la imagen del CAPTCHA
                        with open('captcha_image.png', 'wb') as img_file:
                            img_file.write(response.content)
                        print("Imagen del captcha guardada como captcha_image.png")

                        # Construye la ruta completa de la imagen
                        image_path = os.path.join(settings.MEDIA_ROOT, 'captcha_image.png')

                        # Mover la imagen a la carpeta 'media'
                        shutil.move('captcha_image.png', image_path)

                    return response
                
                response = GetCaptchaImage()
                # Verificar si la respuesta es exitosa
                # Verificar si la respuesta es exitosa
                if response.status_code == 200:

                    time.sleep(random.uniform(60, 61))
                    # region s-captcha
                    try:
                        def MainCaptcha():
                            try:
                                print('entra al maincaptcha')
                                time.sleep(10)
                                txt = "Welcome back! You last signed in with a cell phone number"
                                el = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{txt}')]")))

                                if el:
                                    print(el)

                                texto_buscado = "Next, please enter the 6-digit code we just sent you"
                                # Espera explícita para el texto buscado
                                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{texto_buscado}')]")))
                                elementos2 = driver.find_elements(By.XPATH, f"//*[contains(text(), '{texto_buscado}')]")
                                print(elementos2)
                                if elementos2:
                                    threading.Thread(target=mostrar_inputs, args=(request,)).start()
                                else:
                                    print("El texto no fue encontrado en la página.")
                            except Exception as e:
                                print(f"Error: {e}")

                        def campo_no_vacio(driver, nombre_campo):
                            return driver.find_element(By.NAME, nombre_campo).get_attribute("value") != ""

                        def FillCaptchaInput():

                            WebDriverWait(driver, 30).until(lambda driver: campo_no_vacio(driver, "captcha"))
                            try:
                                continue_buttons = WebDriverWait(driver, 10).until(
                                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Submit')]"))
                                )
                            except Exception as e:
                                print('error: ', e)
                                continue_buttons = WebDriverWait(driver, 10).until(
                                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Continue')]"))
                                )
                            driver.execute_script("arguments[0].click();", continue_buttons)
                            print('llego aqui')
                            return continue_buttons

                        FillCaptchaInput()
                        time.sleep(15)
                        print('submit')
                        MainCaptcha()

                        # cuando se le da click a continue te vuelve al numero de telefono
                        # para que se haga click en continue y entonces abre el captcha de submit

                    except Exception as e:
                        print('error: ', e)
                
                else:
                    print('Error al descargar la imagen del captcha')
            except Exception as e:
                print(f"Error: {e}")
                print("No encontró imagen de captcha en ninguno de los métodos")
        guardar_cookies()


def mostrar_inputs(request):
    if request.method == 'POST':
        # Procesa los datos del formulario, incluido el valor del captcha
        # Realiza las acciones necesarias, como guardar las cookies
        return HttpResponse("Datos recibidos y procesados correctamente.")
    else:
        return render(request, 'mostrar_inputs.html')

# region captcha
import base64
def form2(request):
    if request.method == 'POST':
        form = CaptchaForm(request.POST)
        if form.is_valid():
            # Aquí puedes manejar la validación del CAPTCHA y cualquier otra acción necesaria
            captcha_code = form.cleaned_data['captcha_text']
            print(captcha_code)
            
            comando_find_element = {'tipo': 'find_element', 'name': 'captcha'}
            comando_send_keys = {'tipo': 'send_keys', 'texto': captcha_code}
            cola_comandos.put(comando_find_element)
            cola_comandos.put(comando_send_keys)
            image_path = os.path.join(settings.MEDIA_ROOT, 'captcha_image.png')
            try:
                # Verificar si el archivo existe antes de eliminarlo
                if os.path.exists(image_path):
                    os.remove(image_path)
                    print(f"Imagen {image_path} eliminada")
                else:
                    print(f"El archivo {image_path} no existe")
            except Exception as e:
                print(f"Error al eliminar la imagen {image_path}: {e}")
    
    else:
        # Si el método es GET, simplemente muestra el formulario con el CAPTCHA
        form = CaptchaForm()
        # return render(request, 'bumble_app/form2.html', {'form': form})
    return render(request, 'bumble_app/form2.html', {'form': form})

def form3(request):
    form = None  # Define form con un valor inicial
    
    if request.method == 'POST':
        # Obtener los valores de los campos del formulario y guardarlos en una lista
        sms_codes = [request.POST.get(f'sms_code_{i}', '') for i in "123456"]
        
        # Filtrar los códigos no vacíos (si el usuario no ingresó un código completo)
        valid_sms_codes = [code for code in sms_codes if code]
        
        # Convertir la lista a una cadena si es necesario
        sms_code_str = ''.join(valid_sms_codes)
        
        # Imprimir o guardar la cadena con los códigos SMS
        print(sms_code_str)
        
        # Aquí puedes manejar la validación del código SMS y cualquier otra acción necesaria
        comando_find_element = {'tipo': 'find_elementCode', 'css_selector': '.text-field__input'}
        comando_send_keys = {'tipo': 'send_keysCode', 'texto': sms_code_str}
        cola_comandos.put(comando_find_element)
        cola_comandos.put(comando_send_keys)
    
    else:
        # Si el método es GET, simplemente muestra el formulario con los campos para el código SMS
        form = CodeForm()
    
    return render(request, 'bumble_app/form3.html', {'form': form})





'''
<div class="text-field text-field--full-rounded" data-qa-role="textfield-container"><input type="text" class="text-field__input" autocomplete="digit" maxlength="1" size="5" data-qa-role="textfield-input" dir="auto" value=""></div>

<div class="code-field__digit"><div class="text-field text-field--full-rounded" data-qa-role="textfield-container"><input type="text" class="text-field__input" autocomplete="digit" maxlength="1" size="5" data-qa-role="textfield-input" dir="auto" value=""></div></div>
<div class="code-field__digit"><div class="text-field text-field--full-rounded" data-qa-role="textfield-container"><input type="text" class="text-field__input" autocomplete="digit" maxlength="1" size="5" data-qa-role="textfield-input" dir="auto" value=""></div></div>

<div class="code-field__digit"><div class="text-field text-field--full-rounded" data-qa-role="textfield-container"><input type="text" class="text-field__input" autocomplete="digit" maxlength="1" size="5" data-qa-role="textfield-input" dir="auto" value=""></div></div>
<div class="code-field__digit"><div class="text-field text-field--full-rounded" data-qa-role="textfield-container"><input type="text" class="text-field__input" autocomplete="digit" maxlength="1" size="5" data-qa-role="textfield-input" dir="auto" value=""></div></div>

<div class="code-field__digit"><div class="text-field text-field--full-rounded" data-qa-role="textfield-container"><input type="text" class="text-field__input" autocomplete="digit" maxlength="1" size="5" data-qa-role="textfield-input" dir="auto" value=""></div></div>'''