from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User_parents,User_teachers

class UserRegistrationForm(UserCreationForm):

    email=forms.EmailField() 
    name=forms.CharField(max_length=20)
    user_type=forms.CharField(max_length=20)

    

    class Meta:
        model=User
        fields=['username','email','name','user_type','password1','password2']

    def save(self, commit=True):
        user=super().save(commit=False)

        user.email = self.cleaned_data["email"]
        user.name=self.cleaned_data["name"]
        user.user_type=self.cleaned_data["user_type"]

        if commit:
            user.save()
        return user

    
class User_p(forms.ModelForm):
    class Meta:
        model= User_parents
        fields=(
            'age',
            'occupation',
            'ChildName',
            'RelationToChild'
        )

class User_t(forms.ModelForm):
    class Meta:
        model = User_teachers

        fields=(
            'age',
            'grade',
        )
