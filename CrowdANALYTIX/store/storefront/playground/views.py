from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    # pull data from databse
    # transform data
    # send emails
    return HttpResponse("Hello world")


def wowfn(request):
    return HttpResponse("YOU ARE AWESOME!!!!")
