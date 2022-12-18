"""ProgrammersKartProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# authentication
from django.contrib.auth import views as auth_view
from . forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm

urlpatterns = [
    path('about/',views.about,name='about'),
    path('contactUs',views.contactUs,name="contactUs"),
    path('',views.home,name='home'),
    path('category/<slug:val>',views.CategoryView.as_view(),name='category'),
    path('productDetail/<int:pk>',views.productDetail.as_view(),name='productDetail'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('address/',views.address,name='address'),
    path('updateAddress/<int:pk>',views.updateAddress.as_view(),name='updateAddress'),

    # login authentication
    path('registration/',views.CustomerRegistrationView.as_view(),name='customerRegistration'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='apps/login.html',authentication_form=LoginForm),name='login'),
   
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='apps/password_reset.html',form_class=MyPasswordResetForm), name='password_reset'),
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='apps/changepassword.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone'),name='passwordchange'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='apps/passwordchangedone.html'),name='passwordchangedone'),

    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout')
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)