from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from django_recaptcha.fields import ReCaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de Usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class EmpleadoForm(ModelForm):
    #captcha = CaptchaField()
    captcha = ReCaptchaField()
    
    class Meta:
        model = Empleado
        #fields = ['rut','nombre','apellido']
        fields = '__all__'

class TipoEmpleadoForm(ModelForm):

    class Meta:
        model = TipoEmpleado
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']