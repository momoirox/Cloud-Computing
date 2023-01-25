from django.urls import path
from . import views

#all urls
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path('students', views.index, name="students"),
    path('professors', views.professors, name="professors"),

]