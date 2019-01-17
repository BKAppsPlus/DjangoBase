from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from .core import *
from .family import *
from .facility import *


#class Event(BaseModel):
#    name = models.CharField(max_length=100, blank=True)
#    facilitySpace = models.ForeignKey(FacilitySpace, on_delete=models.PROTECT,blank=True, null=True)
#    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT,blank=True, null=True)
#    startDateTime = models.DateTimeField()
#    endDateTime = models.DateTimeField()
    
#    def __str__(self):
#        return self.name  


#class ChildAssignment(BaseModel):
#    event = models.ForeignKey(Event, on_delete=models.PROTECT,blank=False, null=False)
#    member = models.ForeignKey(Person, on_delete=models.PROTECT,blank=False, null=False)

         
#    def __str__(self):
#        return self.member.name + " at " + self.event.name + " with " + self.event.teacher.name
