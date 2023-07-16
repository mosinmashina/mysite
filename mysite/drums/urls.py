from django.urls import path, re_path, include

from .views import *

urlpatterns = [
    path('', main, name='home'),
    path('education/', education, name='education'),
    path('drummer/', drummer, name='drummer'),
    path('covers/<str:genre_id>/', covers, name='covers'),
    path('index/', index, name='index'),
]
