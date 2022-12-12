from django.urls import path
from . import views


# URLconfs
urlpatterns = [path("hello/", views.say_hello), path("wow/", views.wowfn)]
