from django import forms
from django.contrib.auth.models import User
from account.models import Profile
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('first_name','last_name','email', 'password1','password2')

        labels = {
            'password1' : 'Password',
            'password2': 'Confirm Password'
        }


class ProfileForm(forms.ModelForm):
    teacher = 'teacher'
    student = 'student'
    user_types = [
        (student,'Student'),
        (teacher,'Teacher')
    ]

    user_type = forms.ChoiceField(required=True, choices=user_types)


    class Meta():
        model = Profile
        fields = ('profile_image','user_type')