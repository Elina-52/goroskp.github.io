from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('Aries', views.Aries, name='Aries'),
    path('Taurus', views.Taurus, name='Taurus'),
    path('Gemini', views.Gemini, name='Gemini'),
    path('Cancer', views.Cancer, name='Cancer'),
    path('Leo', views.Leo, name='Leo'),
    path('Virgo', views.Virgo, name='Virgo'),
    path('Libra', views.Libra, name='Libra'),
    path('Scorpio', views.Scorpio, name='Scorpio'),
    path('Sagittarius', views.Sagittarius, name='Sagittarius'),
    path('Capricorn', views.Capricorn, name='Capricorn'),
    path('Aquarius', views.Aquarius, name='Aquarius'),
    path('Pisces', views.Pisces, name='Pisces')
]