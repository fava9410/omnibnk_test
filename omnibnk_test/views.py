from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request,"index.html")

@csrf_exempt
def log_in(request):
    error_message = '';
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                next_url = request.GET.get('next')
                if next_url:
                    return HttpResponseRedirect(next_url)
                return HttpResponseRedirect(reverse('home'))
            else:
                error_message = 'Your account is inactived!'
        else:
            error_message = 'Username or password is wrong'

    return render(request, "login.html", {'error_message' : error_message})

@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def sign_up(request):
    context = {}
    if request.method == 'POST':
        data = request.POST
        User.objects.create(username = data['username'],
                    first_name = data['first_name'],
                    last_name = data['last_name'],
                    password = make_password(data['password']),
                    is_superuser = False)
        return redirect('home')
    else:
        return render(request, "sign_up.html", context)

@csrf_exempt
def check_username(request):
    username_exists = False

    if User.objects.filter(username = str(request.POST.get('username'))).exists():
        username_exists = True

    return HttpResponse(username_exists)
