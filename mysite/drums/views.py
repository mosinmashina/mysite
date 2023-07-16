import os

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from .models import *

import googleapiclient.discovery
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

def index(request):
    return render(request, 'drums/index.html')

def covers(request, genre_id):
    allCovers = Cover.objects.all()
    if (genre_id == 'all'):
        covers = allCovers
    else: covers = Cover.objects.filter(genre = genre_id)
    
    genres = list(set(map(lambda cover: cover.genre, allCovers)))

    return render(request, 'drums/covers.html', {'genres': genres, 'covers': covers, 'currentGenre': genre_id})

def main(request):
    return render(request, 'drums/main.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('Who I am?')

def videos(request):
    searchParameter = request.GET['query']
    
    if not searchParameter: 
        return JsonResponse({})
    
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyCBYnuoNSLamm7YeCP89Uy57ZR4l8zQ1-Q"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.search().list(
        part="id",
        maxResults=5,
        q="drummer " + searchParameter,
        type="youtube#video"
    )
    response = request.execute()
    
    return JsonResponse(response)