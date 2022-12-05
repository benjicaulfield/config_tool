from django.urls import path
from . import views

urlpatterns = [
  path('', views.getRoutes, name='routes'),
  path('api/units/', views.getUnits, name='units'),
  path('api/units/<str:pk>', views.getUnit, name='unit'),
  path('api/topics/', views.getTopics, name='topics'),
  path('api/topics/<str:pk>', views.getTopic, name='topic'),
  path('api/contents/', views.getContents, name='contents'),
  path('api/contents/<str:pk>', views.getContent, name='content'),



]