from django.contrib import admin

from app.models import State,City, Hospital,facility,availability
# Register your models here.

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Hospital)
def afterHospitalSave(signal , instance ,**kwargs ):
    facilities= facility.objects.all()
    for Facility in facilities:
       Availability= availability(hospital=instance, Facility=Facility)
       Availability.save()
   
class facilityAdmin(admin.ModelAdmin):
    model=facility
    list_display =['title']

class HospitalAdmin(admin.ModelAdmin):
    model=Hospital
    list_display=['name', 'phone', 'address', 'city']

class CityAdmin(admin.ModelAdmin):
    model=City
    list_display=['name', 'state']

class availabilityAdmin(admin.ModelAdmin):
    model=availability
    list_display=['hospital','Facility','total','available','updated_at']
    list_editable=['total','available']

admin.site.register(State)
admin.site.register(City, CityAdmin)
admin.site.register(Hospital , HospitalAdmin)
admin.site.register(facility, facilityAdmin)
admin.site.register(availability,availabilityAdmin)