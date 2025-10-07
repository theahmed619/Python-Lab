from django.shortcuts import render, redirect
from .models import Student

# Create your views here.

def login(req):
  return render(req,"accounts.html")


def students(req):
  students= Student.objects.all()
  return render(req,"student_list.html", {"students":students})


def add_student(req):
  if req.method=="POST":
    name=req.POST.get('name')
    email=req.POST.get('email')
    age=req.POST.get('age')
    branch=req.POST.get('branch')
    image=req.FILES.get('image')
    student =Student(
      name=name,
      email=email,
      age=age,
      branch=branch,
      image=image
    )
    student.save()
    return redirect('students')
  return render(req, "add_student.html")



# In views.py

def update_student(req, id):
  # Use .get() instead of .filter().first() for fetching a single object
  student = Student.objects.get(id=id)

  if req.method == "POST":
    # Get the new data from the form
    name = req.POST.get('name')
    email = req.POST.get('email')
    age = req.POST.get('age')
    branch = req.POST.get('branch')
    image = req.FILES.get('image')

    # Update the student object with the new data
    student.name = name
    student.email = email
    student.age = age
    student.branch = branch

    # Only update the image if a new one was uploaded
    if image:
      student.image = image

    # Save the changes to the database
    student.save()

    # Redirect to the student list page after a successful update
    return redirect('students')

  # For a GET request, show the form with the student's current data
  return render(req, 'update_student.html', {'student': student})
