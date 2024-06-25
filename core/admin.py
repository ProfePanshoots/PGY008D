from django.contrib import admin
from .models import *
from admin_confirm import AdminConfirmMixin
from django.contrib.admin import ModelAdmin

class EmpleadoModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['rut','nombre','apellido','edad']

class TipoEmpleadoModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['descripcion']

# Register your models here.
admin.site.register(TipoEmpleado, TipoEmpleadoModelAdmin)
admin.site.register(Empleado, EmpleadoModelAdmin)
