from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    url = 'https://api.twitter.com/1.1/search/tweets.json?q=Formula One&APPID=lB7eL4f3OamBS2QHAdTiQlQzR'
    search = 'Formula One'

    r = requests.get(url)
    print(r)

    return HttpResponse("")
# Create your views here.
