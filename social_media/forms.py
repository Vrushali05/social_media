from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class SignInForm(forms.Form):
    username = forms.CharField(required=True, label="User Name",
                               widget=forms.TextInput(
                                   attrs={"placeholder": "username"}))

    password = forms.CharField(required=True, label="Password",
                               widget=forms.PasswordInput(
                                   attrs={"placeholder": "password"}
        # adding new Constraint : special char, Uppercase letter
                               ))


    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username,password=password)
        print("Sign In View")
        if user is None:
            raise forms.ValidationError("User name or Password is INVALID/INCORRECT")

