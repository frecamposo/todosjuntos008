from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as login_aut
# Create your views here.
# crear los controladores para visualizar
# las paginas web

def index(request):
    categorias = Categoria.objects.all()
    contexto={'categorias':categorias}
    mascotas=Mascota.objects.order_by("idMascota").reverse()[:2]
    contexto["mascotas"]=mascotas
    return render(request,"index.html",contexto)

def galeria(request):
    mascotas= Mascota.objects.filter(publicado=True)
    cantidad =Mascota.objects.filter(publicado=True).count()
    contexto={"mascotas":mascotas,'cantidad':cantidad}

    return render(request,"galeria.html",contexto)

def formulario(request):
    return render(request,"formulario_perris.html")

def quienes_somos(request):
    return render(request,"quienes_somos.htm")

def admin_mascotas(request):
    cate = Categoria.objects.all()
    print(request.user.username)
    nom_user=request.user.username
    usu=User.objects.get(username=nom_user)
    print(usu)
    mascotas= Mascota.objects.filter(usuario=usu)
    contexto={'categorias':cate,'mascotas':mascotas}
    if request.POST:
        
        nombre = request.POST.get("txtNombre")
        edad = request.POST.get("txtEdad")
        raza = request.POST.get("txtRaza")
        desc = request.POST.get("txtDesc")
        img = request.FILES.get("txtImg")
        cat = request.POST.get("cboCategoria")        
        usu=request.user.username
        usu_request=User.objects.get(username=usu)
        obj_cate = Categoria.objects.get(nombre=cat)
        mas = Mascota(           
            nombre=nombre,
            raza=raza,
            edad=edad,
            descripcion=desc,
            foto=img,
            categoria= obj_cate,
            comentario='--',
            usuario=usu_request)
        mas.save()
        contexto["mensaje"]="grabo"
    return render(request,"admin_perris.html",contexto)

def ficha_mascota(request,id):
    mascota = Mascota.objects.get(idMascota=id)
    contexto={'mascota':mascota}
    return render(request,"mascota.html",contexto)

def buscar_nombre(request):
    nombre = request.POST.get("txtMascota")
    mascotas = Mascota.objects.filter(nombre__contains=nombre)
    cantidad= Mascota.objects.filter(nombre__contains=nombre).count()
    contexto={'mascotas':mascotas,'cantidad':cantidad}
    return render(request,"galeria.html",contexto)

def fitro_categoria(request,id):
    cate = Categoria.objects.get(nombre=id)
    mascotas = Mascota.objects.filter(categoria=cate)
    contexto={'mascotas':mascotas}
    return render(request,"galeria.html",contexto)

def buscar_palabra_clave(request):
    palabra = request.POST.get("txtDesc")
    mascotas = Mascota.objects.filter(descripcion__contains=palabra)
    cantidad= Mascota.objects.filter(descripcion__contains=palabra).count()
    contexto={'mascotas':mascotas,'cantidad':cantidad}
    return render(request,"galeria.html",contexto)

def login(request):
    contexto={'mensaje':''}
    if request.POST:
        usuario = request.POST.get("txtUser")
        pas = request.POST.get("txtPass")
        us = authenticate(request,username=usuario,password=pas)
        if us is not None and us.is_active:
            login_aut(request,us)
            categorias = Categoria.objects.all()
            contexto={'categorias':categorias}
            mascotas=Mascota.objects.order_by("idMascota").reverse()[:2]
            contexto["mascotas"]=mascotas
            return render(request,"index.html",contexto)
    contexto={'mensaje':'usuario incorrecto'}
    return render(request,"login.html",contexto)

def cerrar_sesion(request):
    logout(request)
    categorias = Categoria.objects.all()
    contexto={'categorias':categorias}
    mascotas=Mascota.objects.order_by("idMascota").reverse()[:2]
    contexto["mascotas"]=mascotas
    return render(request,"index.html",contexto)

def registro(request):
    contexto={'mensaje':''}
    if request.POST:
        nombre=request.POST.get("txtNombre")
        apellido=request.POST.get("txtApellido")
        usuario=request.POST.get("txtNombreUser")
        password= request.POST.get("pwdPass1")
        email=request.POST.get("txtEmail")
        usu = User()
        usu.first_name=nombre
        usu.last_name=apellido
        usu.email=email
        usu.username=usuario
        usu.set_password(password)
        try:
            usu.save()
            contexto['mensaje']='Grabo Usuario'
        except:
            contexto['mensaje']='No Grabo usuario'

    return render(request,"registro.html",contexto)
