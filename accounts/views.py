from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from django.contrib import messages
 
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, '登録が完了しました！')
            return redirect('login')  # ログインページにリダイレクト
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
 
#from django.shortcuts import render
 
# Create your views here.

class SignUpView(CreateView):
  form_class = CustomUserCreationForm

  template_name = 'signup.html'

  success_url = reverss_lazy('accounts:signup_success')

  def form_valid(seif, form)

  user = form.save()
  self.object = user

  return super(). form_valid(form)

class signUpSuccessView(TemplateView):
 template_name = 'signup_success.html'
 
 
