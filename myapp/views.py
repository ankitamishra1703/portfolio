from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def career(request):
    return render(request, 'career.html')

def education(request):
    return render(request, 'ed.html')
