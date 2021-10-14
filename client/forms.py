from django.forms import ModelForm, fields, models
from .models import Client


class ClientForm(ModelForm):

    class Meta : 
        model = Client
        fields = '__all__'

    # first_name = ModelForm.CharField(max_length = 50)
    # last_name = ModelForm.CharField(max_length = 50)	
    # phone_number = ModelForm.IntegerField()
    # email_address = ModelForm.EmailField(max_length = 150)