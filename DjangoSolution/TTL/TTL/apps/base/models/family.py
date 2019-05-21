from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from .core import *



class Household(BaseModel):
    def limit_client_choices():
        return {'type__name': 'Family'}

    client = models.OneToOneField(Client,related_name='clientHousehole',primary_key=True,on_delete=models.PROTECT,
                                  limit_choices_to=limit_client_choices)
    member = models.ManyToManyField(Person, through='HouseHoldMembership',)
    
    def __str__(self):
        return self.name
    def get_members(self):
        return ",".join([str(p) for p in self.member.all()])


    class Meta:
        verbose_name_plural = "7. Households"



class HouseholdMembership(BaseModel):
    household = models.ForeignKey(Household, on_delete=models.PROTECT)
    member = models.ForeignKey(Person, on_delete=models.PROTECT,blank=True, null=True)
    isChild = models.BooleanField(blank=False, default=False)
    
    class Meta:
        verbose_name_plural = "8. Household Memberships"