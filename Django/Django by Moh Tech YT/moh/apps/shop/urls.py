from django.urls import path
from . import views


urlpatterns = [
    path('shops/',views.home, name="shop"),
] 
