from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('index', views.index, name='index'),
    path('creatuser', views.createuser, name='createuser'),
    path('creatuseraction', views.creatuseraction, name='creatuseraction'),
    path('updateuser/<int:cedula>', views.updateuser, name='updateuser'),
    path('updateuser/updateuseraction', views.updateuseraction, name='updateuseraction'),
    path('searchuser', views.searchuser, name='searchuser'),
    path('deleteuser/<int:cedula>', views.deleteuser, name='deleteuser'),
    path('createbovine', views.createbovine, name='createbovine'),
    path('createbovineaction', views.createbovineaction, name='createbovineaction'),
    path('updatebovine/<int:codigo_bovino>', views.updatebovine, name='updatebovine'),
    path('updatebovine/updatebovineaction', views.updatebovineaction, name='updatebovineaction'),
    path('searchbovine', views.searchbovine, name='searchbovine'),
    path('deletebovine/<int:codigo_bovino>', views.deletebovine, name='deletebovine'),
    path('createproduction', views.createproduction, name='createproduction'),
    path('createproductionaction', views.createproductionaction, name='createproductionaction'),
    path('updateproduction/<int:id_produccion>', views.updateproduction, name='updateproduction'),
    path('updateproduction/updateproductionaction', views.updateproductionaction, name='updateproductionaction'),
    path('searchproduction', views.searchproduction, name='searchproduction'),
    path('deleteproduction/<int:id_produccion>', views.deleteproduction, name='deleteproduction'),
    path('registeruser', views.registeruser, name='registeruser'),
    path('registeruseraction', views.registeruseraction, name='registeruseraction'),
    path('login', views.login, name='login'),
    path('generarreporte', views.generarreporte, name='generarreporte'),
    path('generarreporteaction', views.generarreporteaction, name='generarreporteaction'),
    path('salir', views.salir, name='salir'),
]
