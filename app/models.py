from django.db import models

# Create your models here.

class State(models.Model):
    name=models.CharField(max_length=50 , null=False,blank=False )

    def __str__(Self):
        return Self.name

class City(models.Model):
    name=models.CharField(max_length=50 , null=False,blank=False )
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')
    
    def __str__(Self):
        return Self.name

 

class Hospital(models.Model):
    name =models.CharField(max_length=50 , null=False,blank=False )
    phone =models.CharField(max_length=12 , null=False,blank=False )
    address =models.CharField(max_length=200 , null=False,blank=False )
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hospitals')
    
    def __str__(Self):
        return Self.name

class facility(models.Model):
     title = models.CharField(max_length=60, null=False, blank=False , default="")
    
     def __str__(Self):
        return Self.title

class availability(models.Model):
      hospital =models.ForeignKey(
          Hospital, on_delete=models.CASCADE, related_name='availabilities')
      Facility= models.ForeignKey(
          facility, on_delete=models.CASCADE, related_name='availabilities',default='')
      total=models.IntegerField(default=0)
      available=models.IntegerField(default=0)
      updated_at=models.DateTimeField(auto_now=True)
      


      def __str__(Self):
         return f'{Self.hospital.name}-{Self.Facility.title}'



    