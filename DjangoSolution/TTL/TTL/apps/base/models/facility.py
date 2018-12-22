from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from .core import BaseModel, Address, Person



class Facility(BaseModel):
    name = models.CharField(max_length=30, blank=True)
    address = models.ForeignKey(Address ,on_delete=models.PROTECT,blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Facilities"


class Teacher(BaseModel):
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name    
    
