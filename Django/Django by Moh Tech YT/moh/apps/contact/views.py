from django.shortcuts import render,redirect
from .forms import ContactForm

# Create your views here.

def home(req):
  if req.method=="POST":
    form=ContactForm(req.POST)
    if form.is_valid():
      form.save()
      return redirect("students")
       
      
  else:
      form=ContactForm()
  return render(req,"contact.html",{"form":form})
