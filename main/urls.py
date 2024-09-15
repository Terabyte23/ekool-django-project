from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sisine/', views.sisine, name='sisine'),
    path('menu/', views.menu, name='menu'),
    path('profil/', views.profil, name='profil'),
    path('ulesaned/', views.ulesaned, name='ulesaned'),
]


