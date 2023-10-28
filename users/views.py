from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

def signup(request):
    data = {"USERform": UserCreationForm()}
    if request.method == "GET":
        return render(request, "signup.html", data)
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                #data["mensaje"] = "Usuario creado"
                return redirect('catalogo')
            except IntegrityError:
                data["mensaje"] = "Usuario ya existe"
                return render(request, "signup.html", data)

        data["mensaje"] = "Las contrase;as no coinciden"
        return render(request, "signup.html", data)

def signout(request):
    logout(request)
    return redirect('catalogo')

def signin(request):
    data = {'AUTHform':AuthenticationForm()}
    if request.method == 'GET':
        return render(request, 'signin.html', data)
    else:
        if request.method == 'POST':
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is None:
                data['mensaje']='Usuario o contrase;as incorrectos'
                return render(request, 'signin.html', data)
            else:
                login(request, user)
                return redirect('catalogo')
