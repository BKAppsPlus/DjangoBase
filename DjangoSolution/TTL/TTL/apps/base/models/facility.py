from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
import datetime
from django.utils import timezone
from .core import *


class Facility(BaseModel):
    def limit_client_choices():
        return {'type__name': 'Service Provider'}

    client = models.OneToOneField(Client,related_name='clientFacility',primary_key=True,on_delete=models.PROTECT, 
                                  limit_choices_to=limit_client_choices)
    license_number = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "4. Facilities"



class FacilitySpace(BaseModel):
    facility = models.ForeignKey(Facility, related_name='facilitySpaces', on_delete=models.SET_NULL,blank=True, null=True)
    capacity = models.PositiveSmallIntegerField(default=1,blank=True, null=True)
    
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name_plural = "5. Facility Spaces"

class Teacher(BaseModel):
    facility = models.ForeignKey(Facility,related_name='facilityteachers', on_delete=models.SET_NULL,blank=True, null=True)

    def __str__(self):
        return self.name    
    class Meta:
        verbose_name_plural = "6. Facility Teacher"

