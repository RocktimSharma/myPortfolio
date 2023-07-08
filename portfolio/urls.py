from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash),
    path('home/', views.home,name='home'),
    path('works/', views.allWorks, name='works'),                 # Projects Path

]

