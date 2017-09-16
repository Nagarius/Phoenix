from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import url

# Create your views here.


def index(request):
    if request.user.is_authenticated():
       return render(request, "index.html", {})
    return render(request, 'welcome.html', {})
