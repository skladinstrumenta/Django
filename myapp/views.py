from random import randint, choice
from string import ascii_uppercase

from django.shortcuts import render

def index(request):
    data = {
        "number": randint(0, 100),
        "text": ''.join(choice(ascii_uppercase) for i in range(randint(5, 10)))
    }
    return render(request, 'index.html', data)

def about(request):
    return render(request, 'about.html')

def art_num(request, article_number, slug_text = ""):
    return render(request, 'art_num.html', {'art_number': article_number, 'stext': slug_text})

def random_id(request, id):
    return render(request, 'random_id.html', {"id": id})

def random_text(request, text):
    return render(request, 'random_text.html', {"slug_text": text})


