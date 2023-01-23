from django.urls import path
from . import views

#all urls
urlpatterns = [
    path('register', views.index, name="register")
]