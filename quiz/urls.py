from django.urls import path
from . import views


urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('forgot-password', views.forgot_password, name='forgot_password'),
    path('index', views.index, name='index'),
    path('suggestion-question', views.suggest_question, name='suggestion-question'),
    path('halloffame', views.hall_of_fame, name='halloffame'),
    path('play', views.play, name='play'),
    path('play_solution', views.play_solution, name='play_solution'),
    path('profile',  views.profile, name='profile'),
    path('index_teacher', views.index_teacher, name='teacher'),
    path('report', views.report, name='profile'),



]