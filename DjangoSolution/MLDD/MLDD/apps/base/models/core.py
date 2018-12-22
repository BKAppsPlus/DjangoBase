from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

# Create your models here.
class class1(models.Model):
    name = models.CharField(max_length=30, blank=True)
        
    class Meta:
        db_table = '_App1_class1'

class class2(models.Model):
    name = models.CharField(max_length=30, blank=True)
    class1s = models.ManyToManyField(class1,)

    class Meta:
        db_table = '_App1_class2'

class BaseModel(models.Model):
    active = models.BooleanField(default=1)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, default='0', related_name='%(class)s_Creator')
    created = models.DateTimeField(auto_now_add=True, blank=False)
    modified_by = models.ForeignKey(User, on_delete=models.PROTECT, default='0', related_name='%(class)s_modified_by')
    modified = models.DateTimeField(auto_now=True, blank=False)

    class Meta:
        abstract = True


class Address(BaseModel):
    Home = 1
    Work = 2
    Other = 0
    TYPES_CHOICES = (
        (Home, 'HOME'),
        (Work, 'Work'),
        (Other, 'Other')
    )

    type = models.CharField(max_length=20, choices = TYPES_CHOICES)
    street_line1 = models.CharField(max_length = 100, blank = True)
    street_line2 = models.CharField(max_length = 100, blank = True)
    city = models.CharField(max_length = 100, blank = True)
    state = models.CharField(max_length = 100, blank = True)
    zipcode = models.CharField(max_length = 5, blank = True)
    country = models.CharField(max_length = 100, blank = True)


class Person(BaseModel):
    name = models.CharField(max_length=30, blank=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name

    