from django.shortcuts import render, redirect
from django.http import HttpResponse
import time
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import messageform, blogform
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings
from django.db.models import Q
from.models import *

# Create your views here.
def tamil_short_stories(request,slug):
	blog=Blog.objects.get(slug=slug)
	related=Blog.objects.filter(slug__contains=slug)[1::]
	return render(request,'detail.html',{'blog':blog,'rel':related})


def index(request):
	blog=Blog.objects.all()
	context={'blogs':blog}
	return render(request,'home.html',context)

def search(request):
	if request.method =='GET':
		query=request.GET.get('q')
		result=Blog.objects.filter(title__contains=query)
		return render(request, 'home.html',{'blogs':result})
def about(request):
	return render(request,'about.html')
def contact(request):
	return render(request,'contact.html')

def message(request):
    model=Message
    form=messageform(data=request.POST)
    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        msg=request.POST['message']
        if 1==1:
            form.save()
            return redirect('/')
            messages.info(request,'message sent')
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['user_name']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user name already taken!!!!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already registerd ,,try to login')
                return redirect('register')
            else:
                
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')
          
        else:
            messages.info(request,'password not matching')
            return redirect('register')




        return redirect('/')


    else:
        return render(request, 'register.html')
def logout(request):
    auth.logout(request)
    return redirect('index')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request,'invalid credentials !!!!')
            return redirect('login')


    else:
        return render(request, 'login.html')
def rr(request):
	return render(request,'register.html')

def userpost(request):
	form=blogform(request.POST or request.FILES)
	if request.method=="POST":
		if form.is_valid():
			obj=form.save(commit=False)
			obj.author=request.user
			
			obj.save()
			return redirect('index')
	return render(request,'userpost.html',{'form':form})
def privacy(request):
    return render(request,'privacy.html')
def terms(request):
    return render(request,'terms.html')
