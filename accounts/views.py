from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
# from .forms import UserRegistrationForm
from django.contrib import messages

class SignUpView(CreateView):
  form_class = CustomUserCreationForm

  template_name = 'signup.html'

  success_url = reverse_lazy('accounts:signup_success')

  def form_valid(seif, form):

    user = form.save()
    self.object = user

    return super(). form_valid(form)

class signUpSuccessView(TemplateView):
 template_name = 'signup_success.html'
 
 
