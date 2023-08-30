from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .forms import CreateUserCreationForm,ChangeUserData
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

    return render(request, 'registration.html', context={'form': form})


# Dashboard
@login_required
def dashboard(request):
    return render(request,'dashboard.html')

# Edit Profile
def change_user_data(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=ChangeUserData(request.POST,instance=request.user)
            if form.is_valid():
                messages.success(request,'Profile Edited Successfully')
                form.save(commit=True)
                return redirect('dashboard')
        else:
            form=ChangeUserData(instance=request.user)
        return render(request,'edit_profile.html',{'form':form})
    else:
        return redirect('registration')
    
# password change
def pass_change(request):
    if request.method=='POST':
        form=PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user) # password change
            return redirect('dashboard')
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'passchange.html', {'form':form})