from django.contrib import admin
from django.urls import path
from django.urls.resolvers import LocaleRegexDescriptor 


# from .views import register , login
# from .views import register
from django.contrib.auth import views as auth_views
# import .views as user_views
from . import views as user_views

urlpatterns = [
    path('register/', user_views.register , name = 'register' ),
    # path('login/', login , name = 'login' ),
    # path('login/', login , name = 'login' ),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='user/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='user/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='user/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='user/password_reset_complete.html'
         ),
         name='password_reset_complete'),

          path('fav/<int:id>/', user_views.favourite_add, name='favourite_add'),
          path('fav/property/<int:id>/', user_views.favourite_add_property, name='favourite_add_property'),
    path('favourites/', user_views.favourite_list, name='favourite_list'),
]   

    # path('', include('blog.urls')),



