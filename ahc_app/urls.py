from django.urls import path,include
from . import views

app_name = "ahc_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('dashboard2/', views.dashboard2, name='dashboard2'),
    #path('login/', views.user_login, name='user_login'),
    # path('signup/', views.user_signup, name='user_signup'),
    # path('ach_client_login/', views.ahc_client_signin, name='ahc_client_signin'),
    # path('ach_client_signup/', views.ahc_client_signup, name='ahc_client_signup'),
]