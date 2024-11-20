from django.http.response import HttpResponse
from django.shortcuts import render
from app.models import facility, State, City,Hospital
from django.views import generic
# Create your views here.

class HospitalDetailVeiw(generic.DetailView):
    model=Hospital


def home(request):
    selected_state_id= request.GET.get('state')
    selected_city_id=request.GET.get('city')
    facilities =facility.objects.all().order_by('title')
    if selected_state_id:
        cities=City.objects.filter(state=selected_state_id)
    else:
        cities=City.objects.all()
    
    states=State.objects.all()
    hospitals=Hospital.objects.all()

    if selected_city_id:
        hospitals=Hospital.objects.filter(city=City(pk=selected_city_id))




    
    context={
        'facilities': facilities,
        'cities' : cities,
        'states':states,
        'hospitals':hospitals,
        'selected_state_id':selected_state_id,
        'selected_city_id':selected_city_id
    }
    return render(request, template_name='app/index.html',context=context )
