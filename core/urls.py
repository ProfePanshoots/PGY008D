from django.urls import path, include
from .views import *
from rest_framework import routers

# CONFIGURACION PARA EL API
router = routers.DefaultRouter()
router.register('tipoempleados', TipoEmpleadoViewset)
router.register('empleados', EmpleadoViewset)


urlpatterns = [
    path('', index, name="index"),
    path('empleados/', empleados, name="empleados"),
    path('empleados/add/', empleadosadd, name="empleadosadd"),
    path('empleados/update/<id>/', empleadosupdate, name="empleadosupdate"),
    path('empleados/delete/<id>/', empleadosdelete, name="empleadosdelete"),
    path('register/', register, name="register"),
    # API
    path('api/', include(router.urls)),
    path('empleadosapi/', empleadosapi, name="empleadosapi"),
    path('profile/', profile, name="profile"),
    # ACCOUNT LOCKED
    path('account_locked/', account_locked, name="account_locked"),
    path('servicios/', servicios, name="servicios"),
]
