from django.http import HttpResponse
# Create your views here.
# views.py
from django.shortcuts import redirect, render
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
global driver

chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--lang=es-ES")
chrome_options.add_argument("--no-sandbox")
download_dir = '/home/yandivd/'
profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
                   # Disable Chrome's PDF Viewer
                   "download.default_directory": download_dir, "plugins.always_open_pdf_externally": True,
                   "download.extensions_to_open": "applications/pdf"}
chrome_options.add_experimental_option("prefs", profile)
driver = webdriver.Chrome(options=chrome_options)

def guardar_cookies():
    cookies = driver.get_cookies()

    # Save the cookies to a JSON file
    with open("cookies_test.json", "w") as cookie_file:
        json.dump(cookies, cookie_file)

    time.sleep(random.uniform(2, 5))

    print("cookies guardadas")

guardar_cookies()