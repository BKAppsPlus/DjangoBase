from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from .core import *


class HouseholdMembershipType(BaseModel):
    isChild = models.BooleanField(blank=False)




class Household(BaseModel):
    client = models.OneToOneField(Client,primary_key=True,on_delete=models.PROTECT)
    member = models.ManyToManyField(Person, through='HouseHoldMembership',)
    
    def __str__(self):
        return self.name


class HouseholdMembership(BaseModel):
    household = models.ForeignKey(Household, on_delete=models.PROTECT)
    member = models.ForeignKey(Person, on_delete=models.PROTECT,blank=True, null=True)
    type = models.ForeignKey(HouseholdMembershipType, on_delete=models.PROTECT)
