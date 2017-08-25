from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import url

# Create your views here.


def index(request):
    return HttpResponse("<a href=/login>Click here to login</a>")
