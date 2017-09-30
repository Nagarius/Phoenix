from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf.urls import url

# Create your views here.


def index(request):
    if request.user.is_superuser:
        return redirect('/admin')
    elif request.user.is_authenticated():
        #return render(request, "main.html", {})
        return render(request, 'main.html', {})
    return render(request, 'index.html', {})