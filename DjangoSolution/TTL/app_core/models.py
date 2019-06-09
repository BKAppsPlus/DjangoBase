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
     
class ClientType(BaseModel):

    def get_absolute_url(self):
        return reverse('base:clienttype-list')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "1 ClientType"

class Client(BaseModel):
    type = models.ForeignKey(ClientType, on_delete=models.PROTECT,default=0, related_name='typeofclient')
    primary_user = models.ForeignKey(User, on_delete=models.PROTECT, default='0')

    def get_absolute_url(self):
        return reverse('base:client-list') 
    class Meta:
        verbose_name_plural = "2. Clients"
        unique_together = ('type', 'primary_user',)

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

    client = models.ForeignKey(Client, related_name='clientAddresses', on_delete=models.PROTECT,blank = True,null=True)
    street_line1 = models.CharField(max_length = 100, blank = True)
    street_line2 = models.CharField(max_length = 100, blank = True)
    city = models.CharField(max_length = 100, blank = True)
    state = models.CharField(max_length = 100, blank = True)
    zipcode = models.CharField(max_length = 5, blank = True)
    country = models.CharField(max_length = 100, blank = True)

    def get_absolute_url(self):
        return reverse('base:address-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "3. Addresses"

class Person(BaseModel):
    userId = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    type = models.ForeignKey(ClientType, on_delete=models.PROTECT, blank=True, null=True)

class Facility(BaseModel):
    def limit_client_choices():
        return {'type__name': 'SERVICE PROVIDER'}

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


def create_Client(sender, instance, created, **kwargs):
    """Create ModelB for every new ModelA."""
    print(instance.type.name)
    if created:
        print('created')
        if instance.type.name == 'SERVICE PROVIDER':
            print('Creating Business Client')
            print(instance.type.name)
            Facility.objects.create(client=instance, name=instance.name,
                                       created_by=instance.created_by, created=instance.created,
                                       modified_by=instance.modified_by, modified=instance.modified)
        elif instance.type.name == 'FAMILY':
            print('Creating Family Client')
            Household.objects.create(client=instance, name=instance.name, 
                                       created_by=instance.created_by, created=instance.created,
                                       modified_by=instance.modified_by, modified=instance.modified)

signals.post_save.connect(create_Client, sender=Client, weak=False,
                          dispatch_uid='models.create_Client')