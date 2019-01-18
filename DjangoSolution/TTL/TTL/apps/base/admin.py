from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import *

#admin.site.register(class1)
#admin.site.register(class2)
class BaseAdmin(admin.ModelAdmin):
    pass
    #readonly_field = ('created','modified',)
    basic_fields = ('created_by','modified_by','active', ) #'created','modified',
    list_display = ('name','created_by','created','modified_by','modified','active','id',)
    fieldsets = [
            ('Administration', {
                'classes': ('collapse',),
                'fields': basic_fields
            })
        ]


class AddressAdmin(BaseAdmin):
    list_display = ('name','consumer',  'street_line1',) + BaseAdmin.list_display
    fieldsets = [(None, {'fields': ('name', 'consumer', 'street_line1', 'street_line2', 'city', 'state', 'zipcode', 'country', )})] + BaseAdmin.fieldsets
class ConsumerTypeAdmin(BaseAdmin):
    pass
class ConsumerAdmin(BaseAdmin):
    list_display = ('name','type', 'primary_user', ) + BaseAdmin.list_display
    fieldsets = [(None, {'fields': ('name', 'primary_user', )})] + BaseAdmin.fieldsets
class PersonAdmin(BaseAdmin):
    pass
    #list_display = ('name', 'userId', ) + BaseAdmin.list_display
    #fieldsets = [(None, {'fields': ('name', 'userId', )})] + BaseAdmin.fieldsets

admin.site.register(Address,AddressAdmin)
admin.site.register(ConsumerType,ConsumerTypeAdmin)
admin.site.register(Consumer,ConsumerAdmin)
admin.site.register(Person,PersonAdmin)

#admin.site.register(Person, PersonAdmin)
#admin.site.register(AddressType,AddressTypeAdmin)
#admin.site.register(Address, AddressAdmin)

#class TeacherInline(admin.TabularInline):
#    model = Teacher
#    #readonly_fields = ('created_by','created','modified_by','modified','active','id', )
#    extra = 1

#class FacilityAdmin(BaseAdmin):
#    list_display =  ('name',) + BaseAdmin.list_display
#    fieldsets = [(None, {'fields': ('name', 'address',)})] + BaseAdmin.fieldsets 
#    inlines = [TeacherInline]

#class FacilitySpaceAdmin(BaseAdmin):
#    list_display =  ('name',) + BaseAdmin.list_display
#    fieldsets = [(None, {'fields': ('name', 'facility', 'capacity', )})] + BaseAdmin.fieldsets 

#class TeacherAdmin(BaseAdmin):
#    list_display =  ('name',) + BaseAdmin.list_display
#    fieldsets = [(None, {'fields': ('name','facility' )})] + BaseAdmin.fieldsets 

#admin.site.register(Facility,FacilityAdmin)
#admin.site.register(FacilitySpace, FacilitySpaceAdmin)
#admin.site.register(Teacher,TeacherAdmin)


#class HouseholdMembershipTypeAdmin(BaseAdmin):
#    list_display =  ('name',) + BaseAdmin.list_display
#    fieldsets = [(None, {'fields': ('name', 'isChild',)})] + BaseAdmin.fieldsets 

#class HouseholdAdmin(BaseAdmin):
#    list_display =  ('name',) + BaseAdmin.list_display
#    fieldsets = [(None, {'fields': ('name', 'address', )})] + BaseAdmin.fieldsets 

#class HouseholdMembershipAdmin(BaseAdmin):
#    list_display =  ('name',) + BaseAdmin.list_display
#    fieldsets = [(None, {'fields': ('name','household''member', 'type', )})] + BaseAdmin.fieldsets 


#admin.site.register(HouseholdMembershipType,HouseholdMembershipTypeAdmin)
#admin.site.register(Household,HouseholdAdmin)
#admin.site.register(HouseholdMembership,HouseholdMembershipAdmin)



#class EventAdmin(BaseAdmin):
#    list_display =  ('name','startDateTime', 'endDateTime',) + BaseAdmin.list_display
#    fieldsets = [(None, {'fields': ('name', 'facilitySpace', 'teacher', 'startDateTime', 'endDateTime',)})] + BaseAdmin.fieldsets 

#class ChildAssignmentAdmin(BaseAdmin):
#    list_display =  ('event',) + BaseAdmin.list_display
#    fieldsets = [(None, {'fields': ('event', 'member',)})] + BaseAdmin.fieldsets 


#admin.site.register(Event,EventAdmin)
#admin.site.register(ChildAssignment,ChildAssignmentAdmin)


admin.site.register(Facility)
admin.site.register(FacilitySpace)
admin.site.register(Teacher)



admin.site.register(HouseholdMembershipType)
admin.site.register(Household)
admin.site.register(HouseholdMembership)



#admin.site.register(Event)
#admin.site.register(ChildAssignment)