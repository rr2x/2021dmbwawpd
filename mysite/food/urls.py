from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.anotherlink, name='anotherlink'),
    path('item/', views.item, name='item')
]
