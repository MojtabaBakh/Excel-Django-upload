from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.http import *

from django.template import RequestContext

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            #login

            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        # user_name= request.POST.get('floatingInput')
        # pas= request.POST.get('floatingPassword')
        # print(user_name)
        # print(pas)
        form = AuthenticationForm(data=request.POST)

        
        
       
        if form.is_valid():
            # login user
            user = form.get_user()
            print(user)

            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('myapp:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html',{'form':form})



def login_view2(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # login user
            user = form.get_user()

            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login2.html',{'form':form})




def logout_view(request):
    if request.method == 'POST':
        logout(request)

        return redirect('myapp:home')
