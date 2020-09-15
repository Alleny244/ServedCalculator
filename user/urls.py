
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('main', views.main, name='main'),
    path('logout', views.logout, name='logout')

]
