from django.shortcuts import render,redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory

# Create your views here.
from . models import *
from .models import Cart

#importing count
from django.db.models import Count

# signUp
from django.contrib.auth.forms import UserCreationForm

#signin
from django.contrib.auth import authenticate, login, logout

#importing view
from django.views import View

# registration
from . forms import CustomerResigtrationForm, CustomerProfileForm
from django.contrib import messages

#for quantity
from django.db.models import Q    # Q - for multiple filter conditions

#importing json response for quantity count
from django.http import JsonResponse

def home(request):
    return render(request,'apps/home.html')

def about(request):
    return render(request,'apps/about.html')

def contactUs(request):
    return render(request,'apps/contactUs.html')

class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, 'apps/category.html',locals())

class productDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)    #primaryKey==pk(parameter)
        return render(request,"apps/productDetail.html",locals())

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerResigtrationForm()
        return render(request,'apps/customerRegistration.html',locals())
    def post(self,request):
        form = CustomerResigtrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User Register Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,'apps/customerRegistration.html',locals())

class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,'apps/profile.html',locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg=Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulations! Profile Save Successfully!")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,'apps/profile.html',locals())


def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,'apps/address.html',locals())

class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)       # instance=add -> it will automatically fill the data in the updateform 
        return render(request,'apps/updateAddress.html',locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)                  #fetching the datas
            add.name = form.cleaned_data['name']               #assigning new values  for the name,locality,...
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()                                         #updating the datas
            messages.success(request,"Congratualations! Profile Update Successsfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return redirect("address")                             #after updating redirect to the address page

# Add to cart

def add_to_cart(request):
    user=request.user

    if request.user.is_authenticated:
        product_id=request.GET.get('prod_id')
        product = Product.objects.get(id=product_id)
        Cart(user=user,product=product).save()
        return redirect("/cart")
    else:
        return redirect("/accounts/login")

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount=0
    for p in cart:
        value = p.quantity * p.product.selling_price
        amount = amount + value
    totalamount = amount + 40
    return render(request,'apps/addtocart.html',locals())

class checkout(View):
    def get(self,request):
        user=request.user
        add=Customer.objects.filter(user=user)
        cart_items=Cart.objects.filter(user=user)
        famount=0
        for p in cart_items:
            value=p.quantity * p.product.selling_price
            famount=famount+value
        totalamount=famount+40
        return render(request, 'apps/checkout.html',locals())


def plus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        user=request.user
        cart= Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value = p.quantity * p.product.selling_price
            amount = amount + value
            totalamount = amount + 40
        data={
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        c.quantity-=1
        c.save()
        user=request.user
        #print(prod_id)
        cart= Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value = p.quantity * p.product.selling_price
            amount = amount + value
        totalamount = amount + 40
        data={
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)

def remove_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        c.quantity-=1
        c.delete()
        user=request.user
        #print(prod_id)
        cart= Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value = p.quantity * p.product.selling_price
            amount = amount + value
        totalamount = amount + 40
        data={
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)