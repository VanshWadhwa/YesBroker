from django.db import models
from django.urls import reverse

# Create your models here.


class Project(models.Model):
    # Model For Society
    category = models.CharField(max_length=255, null=True, blank=True)
    # MOD
    # rera = models.BooleanField(null=True, blank=True)
    rera = models.CharField(max_length=50, null=True, blank=True)
    society = models.CharField(max_length=255, null=True, blank=True)
    developer = models.CharField(max_length=255, null=True, blank=True)
    completion = models.CharField(max_length=200, null=True, blank=True)
    age = models.CharField(max_length=200, null=True, blank=True)
    # year
    # rating =
    rating = models.CharField(max_length=50, null=True, blank=True)
    contact = models.CharField(max_length=255, null=True, blank=True)
    subLocality = models.CharField(max_length=255, null=True, blank=True)
    locality = models.CharField(max_length=255, null=True, blank=True)
    zone = models.CharField(max_length=100, null=True, blank=True)

    # MOD
    projectPinCode = models.CharField(max_length = 255 , null=True, blank=True)
    # projectPinCode = models.IntegerField(null=True, blank=True)
    googlePin = models.CharField(max_length=255, null=True, blank=True)

    # MOD
    units = models.CharField(max_length = 255 , null=True, blank=True)
    # units = models.IntegerField(null=True, blank=True)

    # MOD
    land = models.CharField(max_length = 255 , null=True, blank=True)
    # land = models.IntegerField(null=True, blank=True)

    # MOD
    floor = models.CharField(max_length = 255 , null=True, blank=True)
    # floor = models.IntegerField(null=True, blank=True)

    # MOD
    block = models.CharField(max_length = 255 , null=True, blank=True)
    # block = models.IntegerField(null=True, blank=True)
    bhk = models.CharField(max_length=255, null=True, blank=True)
    area = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    promotersMembers = models.CharField(max_length=255, null=True, blank=True)
    landOwnerDetails = models.TextField(null=True, blank=True)
    surveyNumber = models.CharField(max_length=255, null=True, blank=True)


    def get_absolute_url(self):
        return reverse("project-filters", kwargs={"slug": self.slug})