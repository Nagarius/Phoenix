from django import forms
from django.contrib.auth.models import User
from .models import UserType, UserInfo
from django.contrib.auth.forms import UserCreationForm



# Defines a new form for the UserInfo table inheriting from the ModelForm class.
class RegisterFormInfo(forms.ModelForm):
    class Meta:

        # Specifies the model to use and the fields from that model to include
        model = UserInfo
        fields = ['dob', 'contactNumber', 'address', 'userTypeID']

# Defines a custom form for the default django user table. Makes email compulsory.
class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    # Specifies the model to use and the fields from that model to include
    class Meta:
        model = User
        fields =("username", "email", "first_name", "last_name", "password1", "password2")

    # This overrides the built in save function of this class. It gets the 'cleaned' email data
    # as is built into Django and then saves the form.
    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
