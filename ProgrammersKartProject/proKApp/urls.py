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
from . forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    path('about/',views.about,name='about'),
    path('contactUs',views.contactUs,name="contactUs"),
    path('',views.home,name='home'),
    path('category/<slug:val>',views.CategoryView.as_view(),name='category'),
    path('productDetail/<int:pk>',views.productDetail.as_view(),name='productDetail'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('address/',views.address,name='address'),
    path('updateAddress/<int:pk>',views.updateAddress.as_view(),name='updateAddress'),

 
    path('add-to-cart/',views.add_to_cart, name='add-to-cart'),
    path('cart/',views.show_cart, name='showcart'),
    path('checkout/',views.show_cart, name='checkout'),


    # login authentication
    path('registration/',views.CustomerRegistrationView.as_view(),name='customerRegistration'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='apps/login.html',authentication_form=LoginForm),name='login'),
   
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='apps/changepassword.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone'),name='passwordchange'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='apps/passwordchangedone.html'),name='passwordchangedone'),

    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),


    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='apps/password_reset.html',form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset-done/',auth_view.PasswordResetView.as_view(template_name='apps/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='apps/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='apps/password_reset_complete.html'),name='password_reset_complete')
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)