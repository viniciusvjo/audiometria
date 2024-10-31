from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("tipo_perda_auditiva:index")
        else:
            messages.error(request, "Usuário inválido")
            return redirect("authentication:login")
    else:
        return render(request, 'authentication/login.html')

def user_logout(request):
    logout(request)
    return redirect("authentication:login")