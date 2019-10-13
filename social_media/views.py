from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponseRedirect  # to response the request and redirect to new page

from . import forms as loginform


class SignInView(generic.FormView):  # generic package and FormView module is inherited to class SignInView.
    # their are different types of ----View. FormView is mostly used.

    template_name = "index.html"  # when the SignInView is opened it goes to index.html file.
    forms_class = loginform.SignInForm  # this convert data and pass to index.html
    # success_url = reverse_lazy("twitter:credentials")

    def form_valid(self, form):
        username = self.request.POST("username")
        password = self.request.POST("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
        else:
            raise forms.ValidationError(['user name or password is INVALID'])

        return super(SignInView, self).form_valid(form)  # constructor of generic.FormView parent class
