from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.conf import settings


def register(request):
    if request.method == 'POST':
        # all data from postback is given here
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Welcome {username}, your account is created')
            # 'login' is based on name=... from mysite/urls.py'
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profilepage(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL
    }
    return render(request, 'users/profile.html', context)
