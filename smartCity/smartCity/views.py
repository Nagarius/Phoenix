from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.conf.urls import url
from accounts import models
import re

# Create your views here.

searchTerm = ''

def searchResults(request):

    # Perhaps it would be better to check the search against a dictionary here before passing it to render. That way,
    # can determine what to render and have another page for a fail or something.
    searchTerm = request.session['searchTerm']

    possibleSearches = ['colleges', 'college', 'libraries', 'library', 'industries', 'industry', 'hotels', 'hotel', 'parks', 'park', 'zoos', 'zoo',
                        'museums', 'museum', 'restaurants', 'restaurant', 'malls', 'mall']


    for word in possibleSearches:
        if word in str.lower(searchTerm):

            context = {
                "searchTerm": word,
            }

            return render(request, 'searchResults.html', context)
    return HttpResponse("<html><body>No results</body></html>")

def index(request):

    #This section of code checks for a post method and then saves the search term to be used in the serach results page

    if request.method == 'POST':

        #Session is a way of storing values to pass from one function to another. This avoids the problem of the script continually executing
        #and overriding values that we wish to store

        request.session['searchTerm'] = request.POST['search']
        return redirect('/results')

    if request.user.is_superuser:
        return redirect('/admin')
    elif request.user.is_authenticated():
        curUserPK = request.user.pk
        curUser = models.UserInfo.objects.get(user_id=curUserPK)
        curUserType = curUser.userTypeID.pk
        firstName = request.user.first_name

        context = {
            "curUserType": curUserType,
            "firstName": firstName
        }

        return render(request, 'main.html', context)
    return render(request, 'index.html', {})