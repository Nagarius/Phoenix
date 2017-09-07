from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext

# Create your views here.


def account_page(request):

    if request.user.is_authenticated():
        return HttpResponse('Welcome back ' + request.user.username)
    else:
        return HttpResponse('Please login')

def register(request):
#     Will eventually wanna put a form in here. USE FORMS!

    return render(request, 'register.html', {})



def login_success(request):
    # Placeholder
    return HttpResponse('Well done!<p><a href="../logout">Logout?</a>')
