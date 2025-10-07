from django.shortcuts import render
from .models import MediaFiles


# Create your views here.

def upload(req):
  if req.method=="POST":
    file_name=req.POST["file_name"]
    upload_file=req.FILES["upload_file"]
    MediaFiles.objects.create(
      file_name=file_name,
      upload_file=upload_file,
    )
    
  uploads=MediaFiles.objects.all()
    

  return render(req,"upload.html",{'uploads':uploads})