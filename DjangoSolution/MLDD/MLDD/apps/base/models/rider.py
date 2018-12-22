from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from .core import BaseModel, Address, Person



class Rider(BaseModel):
    name = models.CharField(max_length=30, blank=True)
    address = models.ForeignKey(Address ,on_delete=models.PROTECT, blank=True, null=True)
    member = models.ForeignKey(Person, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

