"""
URL configuration for AskPupkin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from members import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index_auth', views.index_auth, name='index_auth'),
    path('hot/', views.hot, name='hot'),
    path('hot_auth/', views.hot_auth, name='hot_auth'),
    path('bender/', views.bender, name='bender'),
    path('bender_auth/', views.bender_auth, name='bender_auth'),
    path('black_jack/', views.black_jack, name='black_jack'),
    path('black_jack_auth/', views.black_jack_auth, name='black_jack_auth'),
    path('user_settings/', views.user_settings, name='user_settings'),
    path('user_login/', views.user_login, name='user_login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('ask/', views.ask, name='ask'),
    path('question/<int:question_id>', views.question, name='one_question'),
    path('question_auth/<int:question_id>', views.question_auth, name='one_question_auth'),
    path('one_question_answers', views.one_question_answers, name='one_question_answers'),
    path('one_question_answers_auth', views.one_question_answers_auth, name='one_question_answers_auth'),
    # path('answer/<int:answer_id>', views.answer, name='one_question_answers'),
    path('admin/', admin.site.urls),
]
