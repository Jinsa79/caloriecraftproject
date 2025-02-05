from django.urls import path
from . import views

app_name = 'acocounts'

urlpatterns = [

  path('signup/',
      views.SignUpView.as_view(),
       name='signup'),

  path('signup_success/',
      views.SignUpSuccessView.as_view(),
      name='signup_success')
  
]
