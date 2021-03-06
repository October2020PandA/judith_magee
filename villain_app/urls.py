from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('villains', views.villains),
    path("add", views.add),
    path("add_villain", views.add_villain),
    path('delete', views.delete),
    path("delete_villain", views.delete_villain,)

]
