from django.contrib import admin

from .models import *
# Register your models here.

class ProviderMasterInline(admin.TabularInline):
    model = ProviderMaster
    
class HouseholdInline(admin.TabularInline):
    model = Household 

class AddressInline(admin.StackedInline):
    model = Address 
    extra = 0    

#class ClientInline(admin.TabularInline):
#    model = Client

#class ProviderOperatorInline(admin.TabularInline):
#    model = ProviderOperator
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
    


    

class PartyTypeAdmin(BaseAdmin):
    pass


class ClientAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display+ ('type', 'primary_user', )
    #fieldsets =BaseAdmin.fieldsets + [(None, {'fields': ('primary_user', )})] 
    #readonly_fields = ['type']
    
    inlines = [ProviderMasterInline,HouseholdInline,AddressInline] #[]
    
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []

        unfiltered = super(ClientAdmin, self).get_inline_instances(request, obj)
        #filter out the Inlines you don't want
        print(obj.name)
        if (obj.type.name == 'FAMILY'):
            return [x for x in unfiltered if isinstance(x,(HouseholdInline,AddressInline))]
        if ( obj.type.name == 'SERVICE PROVIDER'):
            return [x for x in unfiltered if isinstance(x,(ProviderMasterInline,AddressInline))]
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

#admin.site.register(ProviderMaster)
    

class PersonAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ('userId', )
    #fieldsets = BaseAdmin.fieldsets + [(None, {'fields': ('userId', )})]

admin.site.register(Address,AddressAdmin)
admin.site.register(PartyType,PartyTypeAdmin)
admin.site.register(Client,ClientAdmin)
admin.site.register(Person,PersonAdmin)





#admin.site.register(Person, PersonAdmin)
#admin.site.register(AddressType,AddressTypeAdmin)
#admin.site.register(Address, AddressAdmin)



class ProviderMasterAdmin(BaseAdmin):
    #list_display = ('name','created_by','created','modified_by','modified','active', 'id',)
    idpos = BaseAdmin.list_display.index('id') #idpos = 6
    list_display = BaseAdmin.list_display[:(idpos)] + BaseAdmin.list_display[(idpos+1):] + ('license_number','client',) 
    #inlines = [ProviderOperatorInline]
    
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return self.readonly_fields + ('client', )
        return self.readonly_fields

    
#class ProviderMasterAdmin(BaseAdmin):
admin.site.register(ProviderMaster,ProviderMasterAdmin)


#admin.site.register(ProviderUnit)

class ProviderUnitAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ( 'facility', 'capacity', )
    #fieldsets = [(None, {'fields': ('name', 'facility', 'capacity', )})] + BaseAdmin.fieldsets 

admin.site.register(ProviderUnit, ProviderUnitAdmin)



#admin.site.register(ProviderOperator)
class ProviderOperatorAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ( 'facility', )
    

admin.site.register(ProviderOperator,ProviderOperatorAdmin)


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


admin.site.register(HouseholdMembership)

#admin.site.register(Event)
#admin.site.register(ChildAssignment)




