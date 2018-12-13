from django.db import models

# Create your models here.
class class1(models.Model):
    name = models.CharField(max_length=30, blank=True)

    class Meta:
        db_table = '_App1_class1'

class class2(models.Model):
    name = models.CharField(max_length=30, blank=True)
    
    class Meta:
        db_table = '_App1_class2'

    
