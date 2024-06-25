from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .serializers import *
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
import requests
from django.core.paginator import Paginator

# API
def profile (request):
    response = requests.get('https://randomuser.me/api/')
    randomuser = response.json()['results']
    response2 = requests.get('https://dog.ceo/api/breeds/image/random')
    perrito = response2.json()

    aux = {
        'randomuser' : randomuser,
        'perrito' : perrito
    }
    
    return render(request, 'core/empleados/crudapi/profile.html', aux) 

def empleadosapi(request):
    response = requests.get('http://127.0.0.1:8000/api/empleados/')
    response2 = requests.get('https://digimon-api.vercel.app/api/digimon')
    empleados = response.json()
    digimons = response2.json()

    # PAGINATOR
    paginator = Paginator(digimons, 3) # CANTIDAD DE DATOS A MOSTRAR
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    aux = {
        'lista' : empleados,
        'page_obj' : page_obj 
    }

    return render(request, 'core/empleados/crudapi/index.html', aux) 

# UTILIZAMOS LAS VIEWSET PARA MANEJAR LAS PETICIONES HTTP (GET,POST,PUT,DELETE)
class TipoEmpleadoViewset(viewsets.ModelViewSet):
    queryset = TipoEmpleado.objects.all()
    serializer_class = TipoEmpleadoSerializers
    renderer_classes = [JSONRenderer]

class EmpleadoViewset(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializers
    renderer_classes = [JSONRenderer]

def group_required(group_name):
    def in_group(u):
        if u.is_authenticated:
            if u.groups.filter(name=group_name).exists() or u.is_superuser:
                return True
        return False
    return user_passes_test(in_group)

def index(request):
    return render(request, 'core/index.html')

def servicios(request):
    return render(request, 'core/servicios.html')

def account_locked(request):
    return render(request, 'core/account_locked.html')

def register(request):
    aux = {
        'form' : CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            # AL USUARIO LE ASIGNAMOS UN GRUPO
            group = Group.objects.get(name='cliente')
            user.groups.add(group)
            # MANDA UN MENSAJE
            messages.success(request, 'Usuario creado correctamente!')
            # OPCIONAL (AUTENTICA Y LOGEA)
            user = authenticate(username=formulario.cleaned_data['username'],password=formulario.cleaned_data['password1'])
            login(request, user)
            # REDIRECCIONA
            return redirect(to="empleados")
        else:
            aux['form'] = formulario
            

    return render(request, 'registration/register.html', aux)

@permission_required('core.view_empleado')
def empleados(request):
    empleados = Empleado.objects.all() # SELECT * FROM empleado
    aux = {
        'lista' : empleados 
    }

    return render(request, 'core/empleados/index.html', aux)

@group_required('supervisor')
def empleadosadd(request):
    aux = {
        'form' : EmpleadoForm()
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Empleado almacenado correctamente')
        else:
            aux['form'] = formulario
            messages.error(request, 'No se pudo almacenar el empleado!')

    return render(request, 'core/empleados/crud/add.html', aux)

@permission_required('core.change_empleado')
def empleadosupdate(request, id):
    empleado = Empleado.objects.get(id=id)
    aux = {
        'form' : EmpleadoForm(instance=empleado)
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(data=request.POST,instance=empleado, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request, 'Empleado modificado correctamente!')
        else:
            aux['form'] = formulario
            messages.error(request, 'No se pudo modificar el empleado!')

    return render(request, 'core/empleados/crud/update.html', aux)

@permission_required('core.delete_empleado')
def empleadosdelete(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()

    return redirect(to="empleados")
