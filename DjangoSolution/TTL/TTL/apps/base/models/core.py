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


#class Booknew(BaseModel):
#    name = models.CharField(max_length=128)
#    author = models.CharField(max_length=128)

#    def get_absolute_url(self):
#        return reverse("base:booknew_list")


     
class ClientType(BaseModel):

    def get_absolute_url(self):
        return reverse('base:clienttype_list')

    def __str__(self):
        return self.name


class Client(BaseModel):
    type = models.ForeignKey(ClientType, on_delete=models.PROTECT,default=0)
    primary_user = models.ForeignKey(User, on_delete=models.PROTECT, default='0')

    def get_absolute_url(self):
        return reverse('base:client-list') #, kwargs={'pk': self.pk})



class Address(BaseModel):
    #NA = 0
    #Family = 1
    #Facility = 2
    #TYPES_CHOICES = (
    #    (NA, 'NA'),
    #    (Family, 'Family'),
    #    (Facility, 'Facility')
    #)
    #category = models.IntegerField(choices = TYPES_CHOICES, default=0)
    #type = models.ForeignKey(AddressType, on_delete=models.PROTECT)

    client = models.ForeignKey(Client, on_delete=models.PROTECT,blank = True,null=True)
    street_line1 = models.CharField(max_length = 100, blank = True)
    street_line2 = models.CharField(max_length = 100, blank = True)
    city = models.CharField(max_length = 100, blank = True)
    state = models.CharField(max_length = 100, blank = True)
    zipcode = models.CharField(max_length = 5, blank = True)
    country = models.CharField(max_length = 100, blank = True)

    def get_absolute_url(self):
        return reverse('address-detail', kwargs={'pk': self.pk})

    

class Person(BaseModel):
    userId = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    



#class Auditable(models.Model):
#    created_on = models.DateTimeField(auto_now_add = True)
#    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_by',on_delete=models.PROTECT)

#    modified_on = models.DateTimeField(auto_now = True)
#    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='modified_by',on_delete=models.PROTECT)

#    class Meta:
#        abstract = True

#class Book(Auditable):
#    name = models.CharField(max_length=128)
#    author = models.CharField(max_length=128)

#    def get_absolute_url(self):
#        return reverse("base:book_list")
