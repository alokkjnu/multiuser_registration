from django.urls import path
from . import views

app_name = "ahc_super_app"

urlpatterns = [
    path('', views.index, name='index'),
    ]