from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf.urls import url
from accounts import models

# Create your views here.


def index(request):

    if request.user.is_superuser:
        return redirect('/admin')
    elif request.user.is_authenticated():
        curUserPK = request.user.pk
        curUser = models.UserInfo.objects.get(user_id=curUserPK)
        curUserType = curUser.userTypeID


        context = {
            "curUserType": curUserType
        }

        return render(request, 'main.html', context)
    return render(request, 'index.html', {})