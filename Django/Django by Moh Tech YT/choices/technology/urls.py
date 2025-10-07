
from django.urls import path,include
from . import views 
urlpatterns = [
    path('', views.select_location, name='select_location'),
    path('nested/', views.nested_choice,name="nested"),
    path('dynamic/', views.dynamic_view,name="dynamic"),
]