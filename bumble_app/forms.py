# forms.py
from django import forms

class RegistrationForm(forms.Form):
    phone_number = forms.CharField(label='Número de teléfono', max_length=100)
    username = forms.CharField(label='Usuario', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class CaptchaForm(forms.Form):
    captcha_text = forms.CharField(label='Contenido de la imagen', max_length=9)