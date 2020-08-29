from django.urls import path
from . import views

urlpatterns = [
    path('search', views.index, name="index"),
    path('show_book/<pk>', views.show_book, name="show_book"),
    path('', views.home, name="home"),
    path('add', views.add, name="add")
]
