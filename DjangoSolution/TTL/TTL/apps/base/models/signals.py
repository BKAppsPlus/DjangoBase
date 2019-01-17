
from django.db.models import signals
from .core import  *
from .facility import *
from .family import *
from .reservation import *
from .signals import *

def create_Consumer(sender, instance, created, **kwargs):
    """Create ModelB for every new ModelA."""
    if created:
        if instance.type.name == 'Business':
            print('qwdqwdqwdqwdqwd')
            print(instance.type.name)
            Facility.objects.create(consumer=instance, name=instance.name,
                                       created_by=instance.created_by, created=instance.created,
                                       modified_by=instance.modified_by, modified=instance.modified)
        elif instance.type.name == 'Family':
            print('qwdqwdqwdqwdqwdqwdqwdqwdqwdqwdqwdqwdqwdqwdqwdqwdqwdqwdqwdqwd')
            Household.objects.create(consumer=instance, name=instance.name,
                                       created_by=instance.created_by, created=instance.created,
                                       modified_by=instance.modified_by, modified=instance.modified)

signals.post_save.connect(create_Consumer, sender=Consumer, weak=False,
                          dispatch_uid='models.create_Consumer')