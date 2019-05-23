from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import *

#admin.site.register(class1)
#admin.site.register(class2)


class FacilityInline(admin.TabularInline):
    model = Facility
    
class HouseholdInline(admin.TabularInline):
    model = Household 

class AddressInline(admin.StackedInline):
    model = Address 
    extra = 0    

#class ClientInline(admin.TabularInline):
#    model = Client

#class TeacherInline(admin.TabularInline):
#    model = Teacher
#    #readonly_fields = ('created_by','created','modified_by','modified','active','id', )
#    extra = 1


class BaseAdmin(admin.ModelAdmin):
    #readonly_fields = ('created_by','modified_by',)
    #basic_fields = ('active','name','created_by','modified_by',) #'created','modified',
    list_display = ('name','created_by','created','modified_by','modified','active', 'id',)
    #fieldsets = [
    #        ('Administration', {
    #            'classes': ('collapse',),
    #            'fields': basic_fields
    #        })
    #    ]


class AddressAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ('client',  'street_line1',) 
    #fieldsets = [(None, {'fields': ('client', 'street_line1', 'street_line2', 'city', 'state', 'zipcode', 'country', )})] + BaseAdmin.fieldsets
    


    

class ClientTypeAdmin(BaseAdmin):
    pass


class ClientAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display+ ('type', 'primary_user', )
    #fieldsets =BaseAdmin.fieldsets + [(None, {'fields': ('primary_user', )})] 
    #readonly_fields = ['type']
    
    inlines = [FacilityInline,HouseholdInline,AddressInline] #[]
    
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []

        unfiltered = super(ClientAdmin, self).get_inline_instances(request, obj)
        #filter out the Inlines you don't want
        print(obj.name)
        if (obj.type.name == 'Family'):
            return [x for x in unfiltered if isinstance(x,(HouseholdInline,AddressInline))]
        if ( obj.type.name == 'Service Provider'):
            return [x for x in unfiltered if isinstance(x,(FacilityInline,AddressInline))]
        else:
            return [x for x in unfiltered if isinstance(x,AddressInline)]
    
    #def get_readonly_fields(self, request, obj=None):
    #    if obj: # editing an existing object
    #        return self.readonly_fields + ('type', )
    #    return self.readonly_fields




class HouseholdAdmin(BaseAdmin):
    idpos = BaseAdmin.list_display.index('id') #idpos = 6
    list_display = BaseAdmin.list_display[:(idpos)] + BaseAdmin.list_display[(idpos+1):] + ('get_members', 'client',) 

     


#admin.site.register(Household)
admin.site.register(Household,HouseholdAdmin)

#admin.site.register(Facility)
    

class PersonAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ('userId', )
    #fieldsets = BaseAdmin.fieldsets + [(None, {'fields': ('userId', )})]

admin.site.register(Address,AddressAdmin)
admin.site.register(ClientType,ClientTypeAdmin)
admin.site.register(Client,ClientAdmin)
admin.site.register(Person,PersonAdmin)





#admin.site.register(Person, PersonAdmin)
#admin.site.register(AddressType,AddressTypeAdmin)
#admin.site.register(Address, AddressAdmin)



class FacilityAdmin(BaseAdmin):
    #list_display = ('name','created_by','created','modified_by','modified','active', 'id',)
    idpos = BaseAdmin.list_display.index('id') #idpos = 6
    list_display = BaseAdmin.list_display[:(idpos)] + BaseAdmin.list_display[(idpos+1):] + ('license_number','client',) 
    #inlines = [TeacherInline]
    
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return self.readonly_fields + ('client', )
        return self.readonly_fields

    
#class FacilityAdmin(BaseAdmin):
admin.site.register(Facility,FacilityAdmin)


#admin.site.register(FacilitySpace)

class FacilitySpaceAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ( 'facility', 'capacity', )
    #fieldsets = [(None, {'fields': ('name', 'facility', 'capacity', )})] + BaseAdmin.fieldsets 

admin.site.register(FacilitySpace, FacilitySpaceAdmin)



#admin.site.register(Teacher)
class TeacherAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ( 'facility', )
    

admin.site.register(Teacher,TeacherAdmin)


#class HouseholdMembershipTypeAdmin(BaseAdmin):
#    list_display =  ('name',) + BaseAdmin.list_display
#    fieldsets = [(None, {'fields': ('name', 'isChild',)})] + BaseAdmin.fieldsets 


#class HouseholdMembershipAdmin(BaseAdmin):
#    list_display =  ('name',) + BaseAdmin.list_display
#    fieldsets = [(None, {'fields': ('name','household''member', 'type', )})] + BaseAdmin.fieldsets 


#admin.site.register(HouseholdMembership,HouseholdMembershipAdmin)



#class EventAdmin(BaseAdmin):
#    list_display =  ('name','startDateTime', 'endDateTime',) + BaseAdmin.list_display
#    fieldsets = [(None, {'fields': ('name', 'facilitySpace', 'teacher', 'startDateTime', 'endDateTime',)})] + BaseAdmin.fieldsets 

#class ChildAssignmentAdmin(BaseAdmin):
#    list_display =  ('event',) + BaseAdmin.list_display
#    fieldsets = [(None, {'fields': ('event', 'member',)})] + BaseAdmin.fieldsets 


#admin.site.register(Event,EventAdmin)
#admin.site.register(ChildAssignment,ChildAssignmentAdmin)







#admin.site.register(HouseholdMembershipType)

admin.site.register(HouseholdMembership)



#admin.site.register(Event)
#admin.site.register(ChildAssignment)




