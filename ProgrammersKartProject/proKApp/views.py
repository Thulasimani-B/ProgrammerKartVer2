from django.shortcuts import render,redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
# Create your views here.
from . models import *

#importing count
from django.db.models import Count

# signUp
from django.contrib.auth.forms import UserCreationForm
from proKApp.templates.apps.forms import CreateUserForm

#signin
from django.contrib.auth import authenticate, login, logout

#importing view
from django.views import View
# MESSAGES
from django.contrib import messages

from . models import Product

def home(request):
    return render(request,'apps/home.html')

def about(request):
    return render(request,'apps/about.html')

def contactUs(request):
    return render(request,'apps/contactUs.html')

def signUp(request):
    form = CreateUserForm()

    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)   
            return redirect('signIn')   

    context = {'form':form}
    return render(request,'apps/signUp.html',context)


def signIn(request):

    if request.method == 'POST':
        username=request.POST.get('uname')
        password=request.POST.get('pword')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request,'apps/home.html')
        else:
            messages.error(request, 'Invalid Username and Password')
            return render(request,'apps/signIn.html')

    context={}
    return render(request,'apps/signIn.html',context)


class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, 'apps/category.html',locals())

class productDetail(View):
    def get(self,request,pk):
        product = Product.objects.filter(id=pk).values()    #primaryKey==pk(parameter)
        return render(request,"apps/productDetail.html",locals())

