from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import  RegisterForm
from django.contrib.auth.models import User

def index(request):
    return render (request, 'index.html', {


    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            messages.success(request,'Bienvenido {}'.format(user.username))
            return redirect('admin:index')
        else:
            messages.error(request,'Usuario o contraseña no validos')


    return render(request, 'login.html',{

    })



def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('login')

def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        
        
        user = form.save()
        if user:
            login(request, user)
            messages.success(request,'Usuario creado exitosamente')
            return redirect('index')

    return render (request, 'register.html', {
        'form' : form

    })