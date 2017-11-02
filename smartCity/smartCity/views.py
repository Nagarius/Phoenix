from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.conf.urls import url
from accounts import models



# This function renders the search page and passes in coordinates for the JavaScript Google API.
def searchPage(request):

    # Here we create two variables to contain the longitude and latitude.
    # The 'curCity' is stored in Django's default session framework.
    # We retrieve this object and then access its longitude and latitude attributes.

    curCityLongitude = models.City.objects.get(cityName=request.session['curCity']).longitude
    curCityLatitude = models.City.objects.get(cityName=request.session['curCity']).latitude

    # Here is a dictionary containing references to the aforementioned variables.
    context = {
        "curCityLongitude": curCityLongitude,
        "curCityLatitude": curCityLatitude
    }

    # This is where the context is passed in and rendered.
    return render(request, 'search.html', context)

def index(request):
    curCity = models.City.objects.get(pk=1)

    #This section of code checks for a post method and then saves the search term to be used in the serach results page
    if request.POST:
        if 'item_id' in request.POST:
            for city in models.City.objects.all().values_list('cityName', flat=True):
                if request.POST['item_id'] == city:
                    curCity = models.City.objects.get(cityName=city)
        if 'search' in request.POST:

            #Session is a way of storing values to pass from one function to another. This avoids the problem of the script continually executing
            #and overriding values that we wish to store

            return redirect('/results')


    if request.user.is_superuser:
        return redirect('/admin')

    elif request.user.is_authenticated():
        curUserPK = request.user.pk
        curUser = models.UserInfo.objects.get(user_id=curUserPK)
        curUserType = curUser.userTypeID.typeName
        curUserName = request.user.first_name
        dropdownItems = models.City.objects.all().values_list('cityName', flat=True)
        links = {
            "restaurants": curCity.restaurantsLink,
            "colleges": curCity.collegesLink,
            "libraries": curCity.librariesLink,
            "industries": curCity.industriesLink,
            "hotels": curCity.hotelsLink,
            "parks": curCity.parksLink,
            "zoos": curCity.zoosLink,
            "museums": curCity.museumsLink,
            "malls": curCity.mallsLink
        }
        request.session['links'] = links
        curCityName = curCity.cityName
        request.session['curCity'] = curCityName

        # Based on the user type, this dictates what is displayed and what is not in this order:
        # 0. restaurants, 1. colleges, 2. libraries, 3. industries, 4. hotels, 5. parks, 6. zoos, 7. museums, 8. malls
        if curUserType == 'Student':
            toDisplay = [1, 1, 1, 0, 0, 1, 1, 1, 1]
        elif curUserType == 'Businessman':
            toDisplay = [1, 0, 0, 1, 1, 1, 1, 1, 1]
        elif curUserType == 'Tourist':
            toDisplay = [1, 0, 0, 0, 1, 1, 1, 1, 1]



        context = {
            "curUserName": curUserName,
            "curCityName": curCityName,
            "toDiscplay": toDisplay,
            "links": links,
            "toDisplay": toDisplay,
            "dropdownItems": dropdownItems
        }

        return render(request, 'main.html', context)
    return render(request, 'index.html', {})