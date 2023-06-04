from django.shortcuts import render

# Create your views here.
def c_create(request):
    return render(request, "customers/create.html")

def c_edit(request):
    return render(request, "customers/edit.html")

def c_index(request):
    return render(request, "customers/index.html")

def c_show(request):
    return render(request, "customers/show.html")
