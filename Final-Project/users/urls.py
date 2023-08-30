from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('registration/', views.userRegister, name='registration'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('edit_profile/',views.change_user_data,name='edit_profile'),
    path('password_change/',views.pass_change,name='passchange'),
]
