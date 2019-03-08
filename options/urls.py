from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.index , name = 'index' ),
    path('currentweather/', views.currentweather , name = "currentweather"),
    path('fiveday3h/', views.fiveday3h , name = "fiveday3h")
]
