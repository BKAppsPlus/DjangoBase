from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Facility, Teacher, HouseHoldMembershipType, Person, Household, HouseHoldMembership, Address

from .models import class1, class2

admin.site.register(class1)
admin.site.register(class2)


admin.site.register(Facility)
admin.site.register(Teacher)
admin.site.register(HouseHoldMembershipType)
admin.site.register(HouseHoldMembership)
admin.site.register(Person)
admin.site.register(Household)
admin.site.register(Address)
