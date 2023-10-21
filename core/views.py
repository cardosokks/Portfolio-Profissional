from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def home(request):    
    return render(request, 'home.html', context)


def logar(request):
    return render(request, 'registration/login.html')

def register(request):
    return render(request, 'registration/register.html')

def dologin(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('/')

    else:
        data['msg'] = 'Senha ou usuário incorretos!'
        data['class'] = 'alert-danger'
        return render(request, 'registration/login.html', data)

def pagina_404(request, exception):
    return render(request, '404.html')

