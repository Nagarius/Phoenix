from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import url

# Create your views here.


def index(request):
    if request.user.is_authenticated():
        return HttpResponse("Already logged in mate<p> <a href='/accounts/logout'> Logout?</a>")
    return render(request, 'welcome.html', {})
