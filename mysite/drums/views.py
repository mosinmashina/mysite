
from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import *

import wikipediaapi
import json
import requests
import random


def education(request):
    return render(request, 'drums/lessons.html')

def drummer(request):
    
    wiki_wiki = wikipediaapi.Wikipedia('CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)', 'en')

    pagePy = wiki_wiki.page('List_of_drummers')
    
    def check_is_drummer(drummer):
        isBand = "(band)" in drummer
        if isBand:
           return False
        firstSentence = pagePy.links[drummer].text.partition('.')[0]
        if 'born ' in firstSentence:
           return True
        return False
    
    linkList = list(pagePy.links.keys())
    randomAttribute = random.choice(linkList)
    while True:
        if (check_is_drummer(randomAttribute)):
            break;
        randomAttribute = random.choice(linkList)
        
    randomDrummer = pagePy.links[randomAttribute]
    
    images = []
    
    # try extract from wiki 
    res = requests.get('https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles='+randomAttribute)
    data = json.loads(res.text)
    pageInfo = next(iter(data['query']['pages'].values()))
    if 'original' in pageInfo:
        images.append(pageInfo['original']['source'])

    
    context = {'originalTitle': randomDrummer.title, 'content': randomDrummer.text, 'images': images}
    return render(request, 'drums/drummer.html', context)
    return render(request, 'drums/drummer.html')

def index(request):
    return render(request, 'drums/index.html')

def covers(request):
    covers = Cover.objects.all()
    return render(request, 'drums/covers.html')

def main(request):
    return render(request, 'drums/main.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('Who I am?')
