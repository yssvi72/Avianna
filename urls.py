from django.urls import path

from . import views

urlpatterns = [
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('SOS/',views.SOSPage,name='SOS'),
    path('map/',views.GETMAPPage,name='map'),
    path('ecom/',views.EcomPage,name='ecom'),
    path('emer/',views.EmergencyPage,name='emer'),
   # path('add',views.add, name='add')
]