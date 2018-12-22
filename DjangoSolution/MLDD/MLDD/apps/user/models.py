from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    APPADMIN = 1
    PROVIDER = 2
    PARENT = 3
    ROLE_CHOICES = (
        (APPADMIN, 'Application Admin'),
        (PROVIDER, 'Provider'),
        (PARENT, 'Parent'),
    )
    MOTHER = 1
    FATHER = 2
    RELATIVE = 3
    PARENT_TYPE = (
        (MOTHER, 'Mother'),
        (FATHER, 'Father'),
        (RELATIVE, 'Relative'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #location = models.CharField(max_length=30, blank=True)
    #birthdate = models.DateField(null=True, blank=True)
    user_type = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    phone = models.IntegerField(default=0, null=True, blank=True)
    daycareId = models.IntegerField(default=0) # for user_type:PROVIDER 
    parent_type = models.PositiveSmallIntegerField(choices=PARENT_TYPE, null=True, blank=True) # for user_type:PROVIDER 
    

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
