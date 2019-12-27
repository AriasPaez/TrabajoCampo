from django.contrib import admin
from .models import cargo, bovino, cuenta, empleado, tipo_bovino, produccion, empleado_login

# Register your models here.
admin.site.register(cargo)
admin.site.register(bovino)
admin.site.register(cuenta)
admin.site.register(empleado)
admin.site.register(tipo_bovino)
admin.site.register(produccion)
admin.site.register(empleado_login)
