from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import *



#admin.site.register(class1)
#admin.site.register(class2)

admin.site.register(Person)
admin.site.register(AddressType)
admin.site.register(Address)

admin.site.register(Facility)
admin.site.register(FacilitySpace)
admin.site.register(Teacher)

admin.site.register(HouseHoldMembershipType)
admin.site.register(Household)
admin.site.register(HouseHoldMembership)

admin.site.register(Event)
admin.site.register(ChildAssignment)
