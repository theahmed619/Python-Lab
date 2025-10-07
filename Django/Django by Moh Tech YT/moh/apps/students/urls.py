from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login),
    path('students/',views.students , name="students"),
    path('add-student/',views.add_student, name="add_student"),
    path('update-student/<int:id>/',views.update_student, name="update_student"),
]
