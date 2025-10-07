
from django.db import models

# Create your models here.
class Student(models.Model):
   # Correct format: A list of tuples
  BRANCH_CHOICE = [
        ("CS", "Computer Science"),
        ("AI", "Artificial Intelligence"),
        ("DS", "Data Science"),
  ]
  name=models.CharField(max_length=100)
  email=models.EmailField(max_length=200)
  age=models.IntegerField()
  image=models.ImageField(upload_to='images/')
  branch=models.CharField(max_length=20, choices=BRANCH_CHOICE)
  date_time=models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
      return f"{self.name} - {self.branch} "
    
    
  
  


