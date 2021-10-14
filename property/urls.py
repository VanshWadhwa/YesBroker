from django.urls import path
from .views import PropertyDetailView , show_property_list  , render_pdf_view , contact

from . import views

urlpatterns = [
    # path('', property_detail, name='property-detail'),
    path('<int:pk>', PropertyDetailView, name='property-detail'),
    path('<str:slug>', show_property_list, name='property-list'),
    path('pdf/pdf', render_pdf_view, name='pdf'),
    path('contact/contact', contact, name='contact'),
    # path('l/<str:slug>', show_property_list, name='property-list'),
    # path('l/', show_property_list, name='property-list'),

]

