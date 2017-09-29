from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterFormInfo, UserCreateForm
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

    # String to print on success of creation
    success = ""

    # Dictionaries for prepopulated field data:
    formUserDic = {
        'username': 'Username',
        'email': 'Email',
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'password1': 'Password',
        'password2': 'Confirm Password'

    }
    formInfoDic = {
        'dob': 'DOB',
        'contactNumber': '0364278173',
        'address': 'Address',
        'userTypeID': 'PLEASE SELECT'
    }

    formUser = UserCreateForm(request.POST or None, initial= formUserDic)
    formInfo = RegisterFormInfo(request.POST or None, initial= formInfoDic)
    print(formUser.errors)

    if formUser.is_valid() and formInfo.is_valid():
        temp_user = formUser.save()
        temp_user.set_password(temp_user.password)
        instance = formInfo.save(commit=False)

        # This is important. It sets the user_id (OneToOneField) of the UserInfo table to the
        # respective User primary key. Basically, it insures they are linked.
        instance.user_id = temp_user.pk
        instance.save()
        success = "Success!!!"


    context = {
        "formInfo": formInfo,
        "formUser": formUser,
        "success": success
    }

    return render(request, 'register.html', context)

# This is the function that is called upon a successful login.
def login_success(request):
    # Placeholder
    #return HttpResponse('Well done!<p>Here is where there will be a profile page? Anyway, you can see the main screen now<p><a href="../../">Here</a><p><a href="../logout">Logout?</a>')
    if request.user.is_authenticated():
        return render(request, 'main.html', {})
    return redirect('../../')
