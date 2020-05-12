from django.shortcuts import (
    render ,  
    redirect
)
from home.models import Post
from .models import (
    Profile ,  
    Follower ,   
)
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, View
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime 
from django.utils import timezone
from .forms import (
     SignupForm, 
     EditProfileForm1,
     EditProfileForm2, 
     EditProImgForm,
)

# Create your views here.

def ProfileView(request, pk):
    profile = get_object_or_404(Profile, id=pk)
    posts = Post.objects.filter(author=profile.user)
    form = EditProImgForm(instance=profile)
    form1 = EditProfileForm1(instance=profile)
    form2 = EditProfileForm2(instance=profile.user)

    context = {
        'title':profile.user.username,
        'profile':profile,
        'posts_count':posts.count(),
        'posts':posts,
        'form1':form1,
        'form2':form2,
        'form':form
        }
    try:
        follower_qs = Follower.objects.filter(follower=request.user, influncer=profile.user)
        follower = follower_qs[0]
        context.update({
        'follower':follower,
    }) 
    except:
        pass
    return render(request, 'ProfileApp/profile.html', context)

@login_required(login_url='login')
def EditProfileView(request, pk):
    profile = get_object_or_404(Profile, id=pk)
    form1 = EditProfileForm1
    form2 = EditProfileForm2
    if request.method == 'POST':
        form1 = EditProfileForm1(request.POST, instance=profile)
        form2 = EditProfileForm2(request.POST, instance=request.user)
        form1.save()
        form2.save()
        return redirect(f'/profile/{profile.id}')

@login_required(login_url='login')
def EditProImgView(request, pk):
    profile = get_object_or_404(Profile, id=pk)
    form = EditProImgForm
    
    if request.method == 'POST':
        print(f'this is request data {request.POST}')
        form = EditProImgForm(request.POST, request.FILES, instance=profile) 
        form.save()
        return redirect(f'/profile/{profile.id}')

@login_required(login_url='login')
def FollowView(request, pk):
    if request.user.is_authenticated:
        followed_profile = get_object_or_404(Profile, id=pk)
        f_request , created = Follower.objects.get_or_create(follower=request.user, influncer=followed_profile.user)

        influ = followed_profile
        follower = request.user
        influ.followers.add(follower.id)
        influ.save()
        follower.profile.following.add(influ)
        follower.save()

        return redirect('index')
    else:
        return redirect('index')



@login_required(login_url='login')
def CancelView(request, pk):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, id=pk)
        follower_qs = Follower.objects.filter(follower=request.user, influncer=profile.user)
        if follower_qs.exists():
            follower = follower_qs[0]
            follower.delete()
            user1 = request.user
            user2 = profile
            user2.followers.remove(user1.id)
            user2.save()
            user1.profile.following.remove(user2)
            user1.save()
            return redirect('index')
        else:
            return redirect('index')
    else:
        return redirect('index')


def SignupView(request):
    if request.user.is_authenticated:
        return redirect('index')
    else : 
        form = SignupForm
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                new_user = form.save(commit=False)
                new_user.set_password(form.cleaned_data['password'])
                new_user.save()

                return redirect('login')
        context = {'form':form}
        return render(request, 'ProfileApp/signup.html', context)

def LoginView(request):
    if request.user.is_authenticated:
        return redirect('index')
    else : 
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request , username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else :
                redirect('login')

        context = {}
        return render(request, 'ProfileApp/login.html', context)


def LogoutView(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect ('login')
    else :
        return redirect('login')