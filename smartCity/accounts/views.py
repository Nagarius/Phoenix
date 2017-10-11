from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegisterFormInfo, UserCreateForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


# Function that is called to render either a logged in user page or a non-logged in one.
def account_page(request):

    if request.user.is_authenticated():
        return HttpResponse('Welcome back ' + request.user.username)
    else:
        return HttpResponse('Please login')

# This function renders the registration page and on a POST request, submits the data to the
# database.
def register(request):

    formUser = UserCreateForm(request.POST or None)
    formInfo = RegisterFormInfo(request.POST or None)
    print(formUser.errors)

    if formUser.is_valid() and formInfo.is_valid():
        temp_user = formUser.save()
        temp_user.set_password(temp_user.password)
        instance = formInfo.save(commit=False)

        # This is important. It sets the user_id (OneToOneField) of the UserInfo table to the
        # respective User primary key. Basically, it insures they are linked.
        instance.user_id = temp_user.pk
        instance.save()
        messages.success(request, "Thanks for registering " + temp_user.username + ", you are now logged in.")
        new_user = authenticate(username=formUser.cleaned_data['username'],
                                password=formUser.cleaned_data['password1'],
                                )
        login(request, new_user)
        return HttpResponseRedirect("/")


    context = {
        "formInfo": formInfo,
        "formUser": formUser,
    }

    return render(request, 'register.html', context)

# This is the function that is called upon a successful login.
def login_success(request):
    #
    if request.user.is_authenticated():
        return redirect('../../')
