from django.urls import path

from .views import *

urlpatterns=[
    path("",MAIN),
    path("courses/",courses),
    path("assignment/",Assaigment),
    path("announce/",Announcements)
]