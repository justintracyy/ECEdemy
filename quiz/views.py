from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from quiz.models import ECESubject


def loginPage(request):
    return render(request, '../account/templates/account/login.html')


def forgot_password(request):
    return render(request, 'forgot-password.html')


def index(request):
    subjects = ECESubject.objects.all()
    context = dict(
      title="ECEDEMY",
      subjects=subjects
    )

    return render(request, 'index.html', context)


def index_teacher(request):
    return render(request, 'index-teacher.html')


def suggest_question(request):
    return render(request, 'suggest-question.html')


def hall_of_fame(request):
    return render(request, 'hall-of-fame.html')


def play(request):
    return render(request, 'play.html')


def play_solution(request):
    return render(request, 'play-solution.html')


def profile(request):
    return render(request, 'profile.html')


def report(request):
    return render(request, 'report.html')



