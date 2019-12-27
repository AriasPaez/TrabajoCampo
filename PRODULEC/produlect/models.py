from django.db import models

# Create your models here.


class cargo(models.Model):
    id_cargo = models.AutoField(primary_key=True)
    nombre_cargo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)


class empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    primer_nombre = models.CharField(max_length=45)
    segundo_nombre = models.CharField(max_length=45, blank=True)
    primer_apellido = models.CharField(max_length=45)
    segundo_apellido = models.CharField(max_length=45, blank=True)
    cedula = models.IntegerField()
    celular = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField(
        'Fecha de Nacimento', blank=False, null=False)
    fecha_contratacion = models.DateField(
        'Fecha de Contratacion', blank=False, null=False)
    sueldo = models.IntegerField()
    email = models.CharField(max_length=45, blank=True)
    id_cargo = models.ForeignKey(cargo, on_delete=models.CASCADE)


class cuenta(models.Model):
    id_cuenta = models.AutoField(primary_key=True)
    nombre_cuenta = models.CharField(max_length=45)
    usuario = models.CharField(max_length=45)
    contraseña = models.CharField(max_length=45)
    id_empleado = models.ForeignKey(empleado, on_delete=models.CASCADE)


class tipo_bovino(models.Model):
    id_tipo_bovino = models.AutoField(primary_key=True)
    tipo_bovino = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=45)


class bovino(models.Model):
    id_bovino = models.AutoField(primary_key=True)
    codigo_bovino = models.IntegerField()
    identidad_ica = models.IntegerField()
    nombre = models.CharField(max_length=45)
    nombre_madre = models.CharField(max_length=45)
    nombre_padre = models.CharField(max_length=45)
    cantidad_partos = models.CharField(max_length=45)
    fecha_ultimo_parto = models.DateField(
        'Fecha de Ultimo Parto', blank=False, null=False)
    dias_lactancia = models.CharField(max_length=45)
    id_tipo_bovino = models.ForeignKey(tipo_bovino, on_delete=models.CASCADE)


class produccion(models.Model):
    id_produccion = models.AutoField(primary_key=True)
    fecha_produccion = models.DateField(
        'Fecha de Produccion', blank=False, null=False)
    primera_produccion = models.DecimalField(
        max_digits=6, decimal_places=3)
    segunda_produccion = models.DecimalField(
        max_digits=6, decimal_places=3)
    cantidad_concentrado = models.DecimalField(
        max_digits=6, decimal_places=3)
    observaciones = models.TextField()
    id_empleado = models.ForeignKey(empleado, on_delete=models.CASCADE)
    id_bovino = models.ForeignKey(bovino, on_delete=models.CASCADE)
    
    
class empleado_login(models.Model):
    id_empleado_login = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=45)
    clave = models.CharField(max_length=45)
    cedula = models.IntegerField()
    cargo = models.CharField(max_length=45, blank=True)