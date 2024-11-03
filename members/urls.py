from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/ask/', views.ask, name='ask'),
    path('members/question/1/', views.question, name='question'),
    path('members/tag/bender/', views.bender, name='bender'),
    path('members/settings/', views.settings, name='settings'),
    path('members/login/', views.login, name='login'),
    path('members/register/', views.signup, name='sighUp'),
]
