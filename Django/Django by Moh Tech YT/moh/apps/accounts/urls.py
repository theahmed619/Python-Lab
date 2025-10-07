from django.urls import path
from . import views
from .views import Home, User_login, Register

urlpatterns = [
    path('home/',views.home, name="home"),
    #path('create/',views.create_user),
    # path('update/',views.update_user)
    path('profile/<int:id>/',views.profile, name="profile"),
    #path('login/',views.user_login, name="login"),
    path('login/',User_login.as_view(), name="login"),
    path('logout/',views.user_logout, name="logout"),
    #path('register/',views.register, name="register"),
    path('register/',Register.as_view(), name="register"),
    path('homes',Home.as_view())
    
    
]
