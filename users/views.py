from django.shortcuts import render, redirect
from .models import Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User name does not exist")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "User name or password is incorrect ")
    return render(request, 'login-register.html')


def logoutUser(request):
    logout(request)
    messages.error(request, "Logged out ")
    return redirect('login')


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile': profile, 'topSkills': topSkills,
               'otherSkills': otherSkills}
    return render(request, 'user-profile.html', context)
