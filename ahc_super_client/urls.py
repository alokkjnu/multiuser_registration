from django.urls import path
from . import views

app_name = "ahc_super_client"

urlpatterns = [
    path('', views.index, name='index'),
    path('add_client/', views.add_client, name='add_client'),
    path('client_list', views.client_list, name='client_list'),
    ]