from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'one/index.html')


def about(request):
    return render(request, 'one/about.html')

def Aries(request):
    return render(request, 'one/Aries.html')

def Taurus(request):
    return render(request, 'one/Taurus.html')

def Gemini(request):
    return render(request, 'one/Gemini.html')

def Cancer(request):
    return render(request, 'one/Cancer.html')

def Leo(request):
    return render(request, 'one/Leo.html')

def Virgo(request):
    return render(request, 'one/Virgo.html')

def Libra(request):
    return render(request, 'one/Libra.html')

def Scorpio(request):
    return render(request, 'one/Scorpio.html')

def Sagittarius(request):
    return render(request, 'one/Sagittarius.html')

def Capricorn(request):
    return render(request, 'one/Capricorn.html')

def Aquarius(request):
    return render(request, 'one/Aquarius.html')


def Pisces(request):
    return render(request, 'one/Pisces.html')

