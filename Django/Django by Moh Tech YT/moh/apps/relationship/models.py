from django.db import models

# Create your models here.

# One to One Relationship
class User(models.Model):
  name=models.CharField(max_length=100)
  email=models.EmailField(max_length=250)
  
  def __str__(self):
      return self.name
  


class Profile(models.Model):
  user=models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField()
  age=models.IntegerField()
  
  
# many to one
class Category(models.Model):
  name=models.CharField(max_length=100)
  
  def __str__(self):
      return self.name
  


class Products(models.Model):
  name=models.CharField(max_length=100)
  price=models.DecimalField(max_digits=10, decimal_places=2)
  Category=models.ForeignKey(Category, on_delete=models.CASCADE)
  
  
# many to many  
class Course(models.Model):
  name=models.CharField(max_length=100) 
  description=models.TextField(max_length=200)
  
  def __str__(self):
      return self.name
  

class Student(models.Model):
  name=models.CharField(max_length=100)
  email=models.EmailField(max_length=100)
  course=models.ManyToManyField(Course)
  
  def __str__(self):
      return self.name
  
  
