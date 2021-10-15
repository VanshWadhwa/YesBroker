from os import name
from django.urls import path
from .views import show_all_filter_page , search_address , premium_services , login
from . import views

urlpatterns = [
    path('', show_all_filter_page, name='project-filters' ),
    path('search/', search_address, name='search-address' ),
    path('premium-services/', premium_services, name='premium-services' ),
    path('login/', login, name='login' ),
]
