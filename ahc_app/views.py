from django.shortcuts import redirect, render
from django.views.generic import TemplateView

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.User.is_super_client:
            return redirect('teachers:quiz_change_list')
        elif request.User.is_client:
            return redirect('students:quiz_list')
        elif request.User.is_broker:
            return redirect('students:quiz_list')
        else:
            return redirect('students:quiz_list')
    return render(request, 'classroom/home.html')



# from django.shortcuts import render, redirect, get_object_or_404
# from .models import *
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import auth
# from django.contrib import messages
# from django.core.exceptions import ObjectDoesNotExist,FieldDoesNotExist
#
#
# # Create your views here.
#
def index(request):
    return render(request, 'ahc_app/index4.html')


def dashboard(request):
    return render(request, 'ahc_app/index.html')
#
#
# def dashboard2(request):
#     return render(request, 'ahc_app/index2.html')
#
def user_login(request):
    return render(request, 'ahc_app/pages/forms/login-v2.html')

# def user_signup(request):
#     return render(request, 'ahc_app/pages/forms/register-v2.html')
#
#
# def ahc_client_signup(request):
#     if request.method == 'POST':
#         if request.POST.get('ahc_client_name') and request.POST.get('ahc_client_mobile') and request.POST.get(
#                 'ahc_client_email') and request.POST.get('ahc_client_password'):
#             ahc_client_signup = Signup_Ahc_Client()
#             ahc_client_signup.ahc_client_name = request.POST.get('ahc_client_name')
#             ahc_client_signup.ahc_client_mobile = request.POST.get('ahc_client_mobile')
#             ahc_client_signup.ahc_client_email = request.POST.get('ahc_client_email')
#             ahc_client_signup.ahc_client_password = request.POST.get('ahc_client_password')
#
#             ahc_client_signup.save()
#
#             return redirect('ahc_app:dashboard')
#         else:
#             return render(request, 'ahc_app/pages/forms/client_signup.html')
#
#
# def ahc_client_signin(request):
#     if request.method == "POST":
#         errors = Signup_Ahc_Client.objects.login_validator(request.POST)
#         if len(errors):
#             for key, value in errors.items():
#                 messages.add_message(request, messages.ERROR, value, extra_tags='login')
#             return redirect('/')
#         try:
#             user = Signup_Ahc_Client.objects.all()
#             user_email = Signup_Ahc_Client.objects.get(ahc_client_email=request.POST['ahc_client_email'])
#             if user_email:
#                 for user in user:
#                     if user.ahc_client_email == request.POST['ahc_client_email'] and user.ahc_client_password==request.POST['ahc_client_password']:
#                         return redirect('ahc_app:dashboard2')
#                     elif user.ahc_client_email != request.POST['ahc_client_email'] and user.ahc_client_password==request.POST['ahc_client_password']:
#                         return redirect('ahc_app:user_signup')
#                     else:
#                         return redirect('ahc_app:user_login')
#             else:
#                 return redirect('ahc_app:user_signup')
#             # user = Signup_Ahc_Client.objects.filter(
#             #     ahc_client_email=request.POST['ahc_client_email']).first() and Signup_Ahc_Client.objects.filter(
#             #     ahc_client_password=request.POST['ahc_client_password']).first()
#             # request.session['ahc_client_email'] = user.ahc_client_email
#             # return redirect('ahc_app:dashboard2')
#         except user.DoesNotExist :
#             print("error")


