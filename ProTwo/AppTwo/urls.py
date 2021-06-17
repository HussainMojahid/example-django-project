from django.contrib.auth import logout
from django.urls import path
from . import views

app_name = "AppTwo"

urlpatterns = [
    path('',views.index,name='index'),
    path('help',views.help,name= 'help'),
    path('form',views.formView,name = 'form'),
    path('ulist',views.userlist,name='ulist'),
    path('datac',views.datacoll,name='datac'),
    path('reg',views.register,name='reg'),
    path('logout',views.user_logout,name= 'logout'),
    path('special',views.special,name='special'),
    path('user_login',views.user_login,name='user_login'),
]