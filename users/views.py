from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from .forms import UserRegisterForm,UserLoginForm,ProfileUpdateForm,UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
'''
messages. debug,info,success,warning,error!.
'''
def register(request):
    if request.method == 'POST':
        new_form = UserRegisterForm(request.POST)
        if new_form.is_valid():
            new_form.save()
            username = new_form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
            return redirect('login')
    else:
        new_form = UserRegisterForm()
    return render(request,'users/register.html',{'form':new_form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'users/profile.html',context)


def Login_page(request):
    return render(request, 'users/login.html')

