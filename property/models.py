from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User




# Create your models here.


# - to be added
# blank = True
# Remove null  =    true from Check boxes

# Mod 
# When the upper text is used it means i have made temorary changes
# and this can be undone and then it will work fine

# None is in perfection
FACING_DIRECTION_CHOICES = (
    ("E", "East"),
    ("W", "West"),
    ("N", "North"),
    ("S", "South"),
    ("NE", "North-East"),
    ("NW", "North-West"),
    ("SE", "South-East"),
    ("SW", "South West"),
)


class Property(models.Model):
    # Model Of individual Properties Like DSR
    projectName = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    projectId = models.CharField(max_length=255, null=True, blank=True)
    # MOD
    # MOD
    # ghmcMortage = models.BooleanField(null=True, blank=True)
    ghmcMortage = models.CharField(max_length=50, null=True, blank=True)
    
    sft = models.IntegerField(null=True, blank=True)
    # msq = float(sft.value_from_object) / 10.764
    towerAndUnit = models.CharField(max_length=100, null=True, blank=True)
    towerNumber = models.CharField(max_length=100, null=True, blank=True)
    towerName = models.CharField(max_length=100, null=True, blank=True)
    floor = models.CharField(max_length=100, null=True, blank=True)
    # MOD

    # facing = models.CharField(
    #     max_length=50, choices=FACING_DIRECTION_CHOICES, null=True, blank=True)

    facing = models.CharField(max_length=50, null=True, blank=True)

    config1 = models.CharField(max_length=200, null=True, blank=True)
    config3 = models.CharField(max_length=200, null=True, blank=True)
    furnishing = models.CharField(max_length=200, null=True, blank=True)
    # MOD
    # servantRoom = models.BooleanField(null=True, blank=True)
    servantRoom = models.CharField(max_length=50, null=True, blank=True)
    # MOD
    # mediaRoom = models.BooleanField(null=True, blank=True)
    mediaRoom = models.CharField(max_length=50, null=True, blank=True)
    # MOD
    # poojaRoom = models.BooleanField(null=True, blank=True)
    poojaRoom = models.CharField(max_length=50, null=True, blank=True)
    # MOD
    # studyOfficeRoom = models.BooleanField(null=True, blank=True)
    studyOfficeRoom = models.CharField(max_length=50, null=True, blank=True)
    bedroom = models.TextField(null=True, blank=True)
    kitchen = models.TextField(null=True, blank=True)
    # MOD
    # forSale = models.BooleanField(null=True, blank=True)
    forSale = models.CharField(max_length=50, null=True, blank=True)
    # MOD
    # forRent = models.BooleanField(null=True, blank=True)
    forRent = models.CharField(max_length=50, null=True, blank=True)
    priceForSale = models.IntegerField(null=True, blank=True)
    priceForRent = models.IntegerField(null=True, blank=True)
    favourites = models.ManyToManyField( User, related_name='favourite_property', default=None, blank=True)


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    # def __str__(self) :
    #     return str(self.id) + " - " + self.projectName

    # msq = None
    # def getMsq(self):
    #     if self.sft != None:
    #         self.msq = float(self.sft) /  10.764
    #     return self.msq

    
        # else:
        #     return self.sft