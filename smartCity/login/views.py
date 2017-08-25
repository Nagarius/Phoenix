from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader, RequestContext

# Create your views here.


def login_page(request):

    return render_to_response('login/login.html')

