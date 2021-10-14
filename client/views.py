from django import forms
from django.shortcuts import render
from django.views.generic import (
    CreateView,
)
from django.views.generic.edit import FormMixin
from .forms import ClientForm
from .models import Client
from django.urls import reverse
from django.contrib import messages

# Create your views here.


# class ClientCreateView( CreateView):
#     model = Client
#     # template_name = 'client_create.html'
#     template_name = 'client/client_form.html'
#     fields = ['first_name', 'last_name', 'phone_number', 'email_address']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


#     def get_success_url(self):
#         return reverse('property_detail', kwargs={'lawyer_slug': self.object.lawyer_slug})
        # return reverse('property-detail')


def index(request):
    form  = ClientForm()

    if request.method == 'POST':
        form = ClientForm(request.POST)
        print(request.POST)
        if form.is_valid():
            messages.success(request , 'We will soon revert back to you : )')
            form.save()


    context = {'form' : form}
    return render(request , 'client/client_form.html' , context)