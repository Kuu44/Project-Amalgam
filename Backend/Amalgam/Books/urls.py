from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('show_book/<pk>', views.show_book, name="show_book")
]
