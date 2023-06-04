from django.shortcuts import render

# Create your views here.
def ac_login(request):
    return render(request,"accounts/login.html")

def ac_profile(request):
    return render(request,"accounts/profile.html")

def ac_register(request):
    return render(request,"accounts/register.html")

