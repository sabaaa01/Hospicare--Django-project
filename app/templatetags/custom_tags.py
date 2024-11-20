from django import template
from app.models import availability

register = template.Library()

@register.simple_tag
def get_table_class(value):
    if value:
        return 'bg-success'
    

@register.simple_tag
def get_availabilities(hospital):
        return availability.objects.filter(hospital=hospital).order_by('Facility_id')
    
@register.simple_tag
def is_state_selected(selected_state, pk):
        if selected_state==str(pk):
              return 'selected'
        return ' '
    
@register.simple_tag
def is_city_selected(selected_city, pk):
        if selected_city==str(pk):
              return 'selected'
        return ' '
