from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.forms import RegistrationForm, EditProfileForm, PostForm
from django.contrib.auth.forms import UserChangeForm
from django.utils import timezone

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/') 
    else:
        form  = RegistrationForm()    
    args = {'form': form}
    return render(request, 'accounts/reg_form.html', args)    

def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/dashboard/profile/')
        
    else: 
        form = EditProfileForm(instance = request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)
    
def new_blog(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/dashboard/', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'dashboard/new_blog.html', {'form': form})

        
