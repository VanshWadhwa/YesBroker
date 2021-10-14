from django.db import models
# from django.urls import reverse



class Client(models.Model):
    # Model For Society

    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)	
    phone_number = models.IntegerField()
    email_address = models.EmailField(max_length = 150)
    description = models.TextField(null=True , blank=True)

    
    def __str__(self) :
        return self.first_name + " " + self.last_name