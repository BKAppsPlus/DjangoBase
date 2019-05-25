
from django.db.models import signals
from .core import  *
from .facility import *
from .family import *
from .reservation import *
from .signals import *

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