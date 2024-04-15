from django.urls import path
from . import views

urlpatterns = [
    path('', views.handle_registration, name='register'),
    path('form2/', views.form2, name='form2'),
    path('form3/', views.form3, name='form3'),
    # Puedes agregar más rutas aquí
]
