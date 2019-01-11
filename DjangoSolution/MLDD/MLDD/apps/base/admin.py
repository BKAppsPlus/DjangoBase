from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Person, Address, Mule, Rider, Service

from .models import class1, class2

admin.site.register(class1)
admin.site.register(class2)


admin.site.register(Mule)
admin.site.register(Rider)
admin.site.register(Service)
admin.site.register(Person)
admin.site.register(Address)
