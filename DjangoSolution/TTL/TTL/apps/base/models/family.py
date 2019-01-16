from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from .core import *


class HouseholdMembershipType(BaseModel):
    name = models.CharField(max_length=30, blank=False)
    isChild = models.BooleanField(blank=False)

    def __str__(self):
        return self.name


class Household(BaseModel):
    name = models.CharField(max_length=30, blank=True)
    member = models.ManyToManyField(Person, through='HouseHoldMembership')
    address = models.ForeignKey(Address ,on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.name


class HouseholdMembership(BaseModel):
    name = models.CharField(max_length=30, blank=True)
    household = models.ForeignKey(Household, on_delete=models.PROTECT)
    member = models.ForeignKey(Person, on_delete=models.PROTECT,blank=True, null=True)
    type = models.ForeignKey(HouseholdMembershipType, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
