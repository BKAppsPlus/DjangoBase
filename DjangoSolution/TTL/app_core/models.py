from django.db import models
from django.urls import reverse
from django.conf import settings

from django.contrib.auth.models import User
import datetime
from django.utils import timezone

from django.db.models import signals


class BaseModel(models.Model, object,):
    name = models.CharField(max_length=30, blank=True)
    active = models.BooleanField(default=1)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, default='0', related_name='%(class)s_Creator')
    created = models.DateTimeField(auto_now_add=True, blank=False)
    modified_by = models.ForeignKey(User, on_delete=models.PROTECT, default='0', related_name='%(class)s_modified_by')
    modified = models.DateTimeField(auto_now=True, blank=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class PartyType(BaseModel):

    def get_absolute_url(self):
        return reverse('base:clienttype-list')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "1 PartyType"




class ProviderMaster(BaseModel):
    def limit_client_choices():
        return {'type__name': 'SERVICE PROVIDER'}
    
    type = models.ForeignKey(PartyType, on_delete=models.PROTECT,default=0, related_name='typeofparty')
    license_number = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return self.name


class ProviderUnit(BaseModel):
    Provider = models.ForeignKey(ProviderMaster, related_name='facilitySpaces', on_delete=models.SET_NULL,blank=True, null=True)
    capacity = models.PositiveSmallIntegerField(default=1,blank=True, null=True)
    
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name_plural = "5. ProviderMaster Spaces"

class ConsumerMaster(BaseModel):
    def limit_client_choices():
        return {'type__name': 'CONSUMER'}
    
    type = models.ForeignKey(PartyType, on_delete=models.PROTECT,default=0, related_name='typeofparty')

    license_number = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return self.name

class ConsumerUnit(BaseModel):
    consumer = models.ForeignKey(ConsumerMaster, related_name='ConsumerUnit', on_delete=models.SET_NULL,blank=True, null=True)
    kidsName =  models.CharField(max_length=30, blank=True)
    kidsBOD = models.DateTimeField(auto_now=True, blank=False)
    
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name_plural = "5. ProviderMaster Spaces"

class PartyOperator(BaseModel):
    operator = models.ForeignKey(User, on_delete=models.PROTECT, related_name='%(party)s_Creator')
    paty_unit = models.ForeignKey(ConsumerMaster, related_name='ConsumerUnit', on_delete=models.SET_NULL,blank=True, null=True)
    
    
    def __str__(self):
        return self.name  
    class Meta:
        verbose_name_plural = "5. ProviderMaster Spaces"

