from django.shortcuts import render
from .models import Country, State,City

# Create your views here.

# chained choice field
def select_location(req):
  countries=Country.objects.all()
  selected_country=req.GET.get('country')
  states=State.objects.filter(country_id=selected_country).all()
  return render(req, "chained_form.html",{'countries':countries, "states":states, "selected_country":selected_country})



def nested_choice(req):
  countries =Country.objects.prefetch_related("state_set_city_set")
  return render(req, "nested_form.html",{"countries":countries})

def dynamic_view(req):
  countries=Country.objects.all()
  return render(req, "dynamic_form.html", {"countries":countries})
