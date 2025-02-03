from django.shortcuts import render, redirect
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
 
 