from django.db import models

# Create your models here.

class MediaFiles(models.Model):
  file_name=models.CharField(max_length=100)
  upload_file=models.FileField(upload_to="uploads/")
  
  def __str__(self):
      return self.file_name
  
