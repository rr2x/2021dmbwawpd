from . import views
from django.urls import path

app_name = 'food'  # namespacing, to prevent other apps from using the same url path
urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.anotherlink, name='anotherlink'),
    path('item/', views.item, name='item'),
    path('<int:item_id>', views.detail, name='detail'),
    path('add', views.create_item, name='create_item'),
    path('update/<int:id>', views.update_item, name='update_item'),
    path('delete/<int:id>', views.delete_item, name='delete_item')
]
