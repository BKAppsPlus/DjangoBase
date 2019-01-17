from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

from django.db.models import signals


class BaseModel(models.Model):
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

    
class ConsumerType(BaseModel):
    pass

class Consumer(BaseModel):
    type = models.ForeignKey(ConsumerType, on_delete=models.PROTECT,default=0)


class ConsumerProfile(BaseModel):
    consumer = models.OneToOneField(Consumer,primary_key=True,on_delete=models.PROTECT)
    

def create_ConsumerProfile(sender, instance, created, **kwargs):
    """Create ModelB for every new ModelA."""
    if created:
        ConsumerProfile.objects.create(consumer=instance, name=instance.name,
                                       created_by=instance.created_by, created=instance.created,
                                       modified_by=instance.modified_by, modified=instance.modified)

signals.post_save.connect(create_ConsumerProfile, sender=Consumer, weak=False,
                          dispatch_uid='models.create_ConsumerProfile')


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

    consumer = models.ForeignKey(Consumer, on_delete=models.PROTECT,blank = True,null=True)
    street_line1 = models.CharField(max_length = 100, blank = True)
    street_line2 = models.CharField(max_length = 100, blank = True)
    city = models.CharField(max_length = 100, blank = True)
    state = models.CharField(max_length = 100, blank = True)
    zipcode = models.CharField(max_length = 5, blank = True)
    country = models.CharField(max_length = 100, blank = True)


class Person(BaseModel):
    userId = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    
    def __str__(self):
        return self.name



