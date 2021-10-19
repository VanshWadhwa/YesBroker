from os import name
from django.urls import path
from .views import show_all_filter_page , search_address , premium_services  , developer_view
from . import views

urlpatterns = [
    path('', show_all_filter_page, name='project-filters' ),
    path('search/', search_address, name='search-address' ),
    path('premium-services/', premium_services, name='premium-services' ),
    path('developers/', developer_view, name='developers' ),
    # path('fav/<int:id>/',favourite_add , name='favourite-add-project' ),
    # path('login/', login, name='login' ),
]
