from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import HttpResponse

# Create your views here.

def home(req):
  users=User.objects.all()
  return render(req,"accounts.html", {"users":users})


# def create_user(req):
#   User.objects.create_user(
#     username="hymenshu",
#     email="hymen@xmail.com",
#     password="hymen "

#   )
#   return redirect("home")


# def update_user(req):
#   user=User.objects.get(username="hymenshu")
#   #user.username="hymen"
#   user.set_password("hymen123")
#   user.save()
#   return redirect("home")


@login_required
def profile(req,id):
  user=User.objects.filter(id=id).first()
  
  return render(req, "profile.html", {"user":user})




# def user_login(req):
#   if req.method == "POST":
#     username = req.POST['username']
#     password = req.POST['password']
#     user = authenticate(req, username=username, password=password)
    
#     if user:
#       login(req, user)
#       # THIS RETURN STATEMENT IS MISSING
#       return redirect('home')
      
#   # This line is reached for GET requests or if the login fails
#   return render(req, "login.html")


# def register(req):
#   if req.method == "POST":
#     username = req.POST['username']
#     password = req.POST['password']
#     User.objects.create_user(
#       username=username,
#       password=password
#     )
#     return redirect("login")
#   return render(req, "register.html")

def user_logout(req):
  logout(req)
  # Remove 'req' from the redirect function
  return redirect("home")


class Home(View):
  
  def get(self, request):
    return HttpResponse("Hello World")
  
  def post(self, req):
    return HttpResponse("This is post request")

class User_login(View):
  def get(self,req):
    return render(req, "login.html")
  def post(self, req):
      username = req.POST['username']
      password = req.POST['password']
      user = authenticate(req, username=username, password=password)
      if user:
       login(req, user)
       return redirect('home')
      return render(req,'login.html')
    
    
class Register(View):
  def get(self,req):
    return render(req, "register.html")
  def post(self, req):
      username = req.POST['username']
      password = req.POST['password']
      User.objects.create_user(
        username=username,
        password=password
        )
      return redirect("login")
    
from django.views.generic.edit import CreateView
from django.urls  import reverse_lazy
    
    
# class Register(CreateView):
#   model=User
#   template_name='register.html'
#   fields=['username','password'] 
#   success_url=reverse_lazy("home")
 

              
 



