from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from .forms import EmpleadoForm, BovinoForm, ProduccionForm, EmpleadoLoginForm
from .models import empleado, bovino, produccion, cargo, empleado_login
from datetime import datetime
from django.utils.dateparse import parse_datetime


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def createuser(request):
    form = EmpleadoForm
    args = {
        'form': form
    }
    return render(request, 'user/create.html', args)


def creatuseraction(request):
    if request.method == 'POST':
        formCreate = EmpleadoForm(request.POST)
        if formCreate.is_valid():
            empleado = formCreate.save(commit=False)
            empleado.save()
            form = EmpleadoForm
    args = {
        'form': form,
        'success': True
    }
    return render(request, 'user/create.html', args)


def updateuser(request, cedula):
    data = empleado.objects.get(cedula=cedula)
    form = EmpleadoForm(instance=data)
    args = {
        'form': form,
        'success': True
    }
    return render(request, 'user/update.html', args)


def updateuseraction(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.save()
            form = EmpleadoForm
            args = {
                'form': form,
                'success': True
            }
    return render(request, 'user/update.html', args)


def searchuser(request):
    users = empleado.objects.all()
    args = {
        'users': users
    }
    return render(request, 'user/search.html', args)


def deleteuser(request, cedula):
    user = empleado.objects.get(cedula=cedula)
    user.delete()
    users = empleado.objects.all()
    args = {
        'users': users,
        'delete-success': True
    }
    return render(request, 'user/search.html', args)


def createbovine(request):
    form = BovinoForm
    args = {
        'form': form
    }
    return render(request, 'bovine/create.html', args)


def createbovineaction(request):
    if request.method == 'POST':
        formCreate = BovinoForm(request.POST)
        if formCreate.is_valid():
            bovino = formCreate.save(commit=False)
            bovino.save()
            form = BovinoForm
    args = {
        'form': form,
        'success': True
    }
    return render(request, 'bovine/create.html', args)


def updatebovine(request, codigo_bovino):
    data = bovino.objects.get(codigo_bovino=codigo_bovino)
    form = BovinoForm(instance=data)
    args = {
        'form': form,
        'success': True
    }
    return render(request, 'bovine/update.html', args)


def updatebovineaction(request):
    if request.method == 'POST':
        form = BovinoForm(request.POST)
        if form.is_valid():
            bovino = form.save(commit=False)
            bovino.save()
            form = BovinoForm
            args = {
                'form': form,
                'success': True
            }
    return render(request, 'bovine/update.html', args)


def searchbovine(request):
    bovines = bovino.objects.all()
    args = {
        'bovines': bovines
    }
    return render(request, 'bovine/search.html', args)


def deletebovine(request, codigo_bovino):
    bovine = bovino.objects.get(codigo_bovino=codigo_bovino)
    bovine.delete()
    bovines = bovino.objects.all()
    args = {
        'bovines': bovines,
        'delete-success': True
    }
    return render(request, 'bovine/search.html', args)


def createproduction(request):
    form = ProduccionForm
    args = {
        'form': form
    }
    return render(request, 'production/create.html', args)


def createproductionaction(request):
    form = None
    if request.method == 'POST':
        formCreate = ProduccionForm(request.POST)
        if formCreate.is_valid():
            produccion = formCreate.save(commit=False)
            produccion.save()
            form = ProduccionForm
    args = {
        'form': form,
        'success': True
    }
    return render(request, 'production/create.html', args)


def updateproduction(request, id_produccion):
    data = produccion.objects.get(id_produccion=id_produccion)
    form = ProduccionForm(instance=data)
    args = {
        'form': form,
        'success': True
    }
    return render(request, 'production/update.html', args)

def updateproductionaction(request):
    if request.method == 'POST':
        form = ProduccionForm(request.POST)
        if form.is_valid():
            produccion = form.save(commit=False)
            produccion.save()
            form = ProduccionForm
            args = {
                'form': form,
                'success': True
            }
    return render(request, 'production/update.html', args)


def searchproduction(request):
    productions = produccion.objects.all()
    args = {
        'productions': productions
    }
    return render(request, 'production/search.html', args)


def deleteproduction(request, id_produccion):
    production = produccion.objects.get(id_produccion=id_produccion)
    production.delete()
    productions = produccion.objects.all()
    args = {
        'productions': productions,
        'delete-success': True
    }
    return render(request, 'production/search.html', args)

def registeruser(request):
    form = EmpleadoLoginForm
    args = {
        'form': form
    }
    return render(request, 'register.html', args)

def registeruseraction(request):
    emp = empleado
    carg = cargo
    path = None
    args = None
    if request.method == 'POST':
        form = EmpleadoLoginForm(request.POST)
        if form.is_valid():
            cedu = request.POST['cedula']
            num = empleado.objects.filter(cedula = cedu).count()
            if num == 0:
                form = EmpleadoLoginForm
                args = {
                    'form': form,
                    'success': False
                }
                path = 'register.html'
            else:
                emp = empleado.objects.get(cedula = cedu)                
                empleadologin = form.save(commit=False)
                carg = emp.id_cargo
                empleadologin.cargo = carg.nombre_cargo
                empleadologin.save()
                path = 'home.html'
    return render(request, path, args)

def login(request):
    path = None
    emplog = empleado_login
    emp = empleado
    carg = cargo
    if request.method == 'POST':
        usuario = request.POST['usuario']
        clave = request.POST['clave']
        num = empleado_login.objects.filter(usuario=usuario, clave=clave).count()
        if num > 0:
            emplog = empleado_login.objects.get(usuario=usuario, clave=clave)
            emp = empleado.objects.get(cedula=emplog.cedula)
            carg = emp.id_cargo
            request.session['logged'] = True
            request.session['cargo'] = carg.nombre_cargo
            path = 'index.html'
            args = {
                'success': True
            }
        else:
            request.session['logged'] = False
            path = 'home.html'  
            args = {
                'success': False
            }
    return render(request, path, args)      

def generarreporte(request):
    return render(request, 'reporte.html')

def salir(request):
    request.session['logged'] = False
    request.session['cargo'] = ''
    return render(request, 'home.html')
    

def generarreporteaction(request):
    producciones = produccion
    if request.method == 'POST':
        fechainicial = datetime.strptime(request.POST['fecha_inicial'], '%Y-%m-%d')
        fechafinal = datetime.strptime(request.POST['fecha_final'], '%Y-%m-%d')
        producciones = produccion.objects.filter(fecha_produccion__range=(fechainicial, fechafinal))
        args = {
                'producciones': producciones
        }
    return render(request, 'reporte.html', args) 