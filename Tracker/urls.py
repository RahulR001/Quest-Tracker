from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('quest/',views.task,name='quest'),
    path('viewtask/', views.viewtask, name='viewtask'),
    path('update/<int:id>', views.updatetask, name='update'),
    path('delete/<int:id>', views.deletetask, name='delete'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup')
]