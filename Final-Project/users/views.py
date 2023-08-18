from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CreateUserCreationForm
# Create your views here.


def userLogin(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exit')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, "loginAndOut.html", context={'page': page})


def userLogout(request):
    logout(request)
    return redirect('login')


def userRegister(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = CreateUserCreationForm()
    if request.method == 'POST':
        form = CreateUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'user account was created')
            login(request, user)
            return redirect('home')
    else:
        messages.error(request, 'an error occurred during register')

    return render(request, 'loginAndOut.html', context={'form': form})
