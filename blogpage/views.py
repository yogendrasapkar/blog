from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.http.response import HttpResponseRedirect

# Create your views here.
def helloWorld(request):
    return HttpResponse("Hello World!")
def index(request):
    return render(request,"index.html")

def register(request):
    if request.method == "POST":
        f = CustomRegistrationForm(request.POST)
        if f.is_valid():
            f.save()
    else:
        f = CustomRegistrationForm()
    return render(request, 'register.html', {'form': f})

def signin(request):
    if request.method == "POST":
        f = AuthenticationForm(request=request, data=request.POST)
        if f.is_valid():
            un = f.cleaned_data['username']
            pd = f.cleaned_data['password']
            user = authenticate(username = un, password = pd)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/profile')
                # return render(request, 'profile.html')
    else:
        f = AuthenticationForm()
    return render(request, 'login.html', {'form': f})

def userProfile(request):
    return render(request, 'profile.html', {'name': request.user})

def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/login')