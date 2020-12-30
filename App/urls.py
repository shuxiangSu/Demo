from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainPage, name='index'),
    path('freshTable', views.FreshStatus, name='fresh')
]