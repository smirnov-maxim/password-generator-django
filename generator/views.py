from django.shortcuts import render
from django.http import HttpResponse, request
import random
import pyperclip


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    lenght = int(request.GET.get('lenght',10))
    thepassword = ''

    if request.GET.get('uppercase'):
        characters.extend('ABCDIFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        characters.extend('1234567890')
    if request.GET.get('special'):
        characters.extend("!#$%&'()*+,-./:;<=>?@[\]^_`{|")

    for i in range(lenght):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    return render(request, 'generator/about.html')
