from django.shortcuts import render
from django.http import HttpResponse
import random
from string import ascii_lowercase as alphabet


def home(req):
    return render(req, 'generator/home.html', {'password': 'fn478fh'})


def about(req):
    return render(req, 'generator/about.html')


def password(req):
    characters = list(alphabet)
    length = int(req.GET.get('length', 12))
    thepassword = ''

    if req.GET.get('uppercase'):
        characters.extend(list(alphabet.upper()))
    if req.GET.get('special'):
        characters.extend('~!@#$%^&*<>?')
    if req.GET.get('numbers'):
        characters.extend('0123456789')

    for x in range(length):
        thepassword += random.choice(characters)
    return render(req, 'generator/password.html', {'password': thepassword})
