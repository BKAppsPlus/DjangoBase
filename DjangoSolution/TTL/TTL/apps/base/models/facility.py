from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
import datetime
from django.utils import timezone
from .core import *






class Facility(BaseModel):
    client = models.OneToOneField(Client,primary_key=True,on_delete=models.PROTECT)
    license_number = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Facilities"



class FacilitySpace(BaseModel):
    facility = models.ForeignKey(Facility, on_delete=models.PROTECT,blank=True, null=True)
    capacity = models.PositiveSmallIntegerField(default=1,blank=True, null=True)
    
    def __str__(self):
        return self.name  


class Teacher(BaseModel):
    facility = models.ForeignKey(Facility, on_delete=models.PROTECT,blank=True, null=True)

    def __str__(self):
        return self.name    

