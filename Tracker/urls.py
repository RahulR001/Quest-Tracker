from django.urls import path
from . import views

urlpatterns = [
     
    path('', views.home),
    path('quest/',views.task,name='quest'),
    path('viewtask/', views.viewtask, name='viewtask'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup')
]