from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:kategori>', views.categori, name='categori')
]
