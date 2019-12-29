from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User_parents,User_teachers

class UserRegistrationForm(UserCreationForm):

    email=forms.EmailField() 
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    usertype=forms.CharField(max_length=20)

    

    class Meta:
        model=User
        fields=['username','email','first_name','last_name','usertype','password1','password2']

    def save(self, commit=True):
        user=super().save(commit=False)

        user.email = self.cleaned_data["email"]
        user.first_name=self.cleaned_data["first_name"]
        user.last_name=self.cleaned_data["last_name"]
        user.usertype=self.cleaned_data["usertype"]

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
            
            'RelationToChild',
        )

class User_t(forms.ModelForm):
    class Meta:
        model = User_teachers
        fields=(
            'age',
            'grade'
        )
