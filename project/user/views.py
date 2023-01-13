from django.shortcuts import render

# Create your views here.

def expage(request):
    return render(request, 'user_templates/expage.html')

def home(request):
    return render(request, 'user_templates/home.html')

def login(request):
    return render(request, 'user_templates/login.html')

def signup(request):
     return render(request, 'user_templates/signup.html')

def shop(request):
    return render(request, 'user_templates/shop.html')

def info(request):
    return render(request, 'user_templates/info.html')

    