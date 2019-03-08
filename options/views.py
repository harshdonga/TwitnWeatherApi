from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    return render(request , 'options/options.html')

def currentweather(request):
    city_name = request.POST['city_name']
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=b9414d4deb551547027ecf1dedae169e'
    #city_name = 'London'
    r = requests.get(url.format(city_name)).json()
    return render(request , 'options/currentweather.html' , { 'r' : r , 'city_name': city_name})

def fiveday3h(request):
    city_name = request.POST['city_name']
    url = 'https://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&APPID=b9414d4deb551547027ecf1dedae169e'
    r = requests.get(url.format(city_name)).json()
    #print(r['list'][1]['dt_txt'])
    return render(request , 'options/fiveday3h.html' , { 'r' : r , 'city_name': city_name})
