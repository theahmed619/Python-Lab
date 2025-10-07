from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth  import logout

# Create your views here.

def login_view(req):
  return render(req,"accounts/login.html")


def logout_view(req):
  logout(req)
  return redirect('login')

@login_required
def home(req):
  return render(req,"accounts/home.html")
