from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
<<<<<<< HEAD
from .models import Profile, StudentId, Attendance, Food
=======
from .models import Profile, StudentId, Attendance, Routine
>>>>>>> 9d6339d79500626496eef02e34ee9448514e376c


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class StudentRegisterForm(forms.ModelForm):

    class Meta:

        model = StudentId

        fields = ('full_name', 'roll', 'childid')


class AttendanceForm(forms.ModelForm):

    class Meta:

        model = Attendance

        fields = ('full_name', 'roll', 'childid')


<<<<<<< HEAD
class FoodForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = ('full_name','roll','childid','food','day')
=======
class RoutineForm(forms.ModelForm):

    class Meta:

        model = Routine

        fields = ('day', 'ten_ten45', 'ten45_eleven30', 'eleven45_twelve30',
                  'twelve30_one15', 'two_two45', 'two45_three30')
>>>>>>> 9d6339d79500626496eef02e34ee9448514e376c
