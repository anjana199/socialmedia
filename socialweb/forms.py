from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from social.models import Posts

class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["title","description","image",]
        widgets={
        "title":forms.TextInput(attrs={"class":"form-control"}),
        "image":forms.FileInput(attrs={"class":"form-select"}),
        "description":forms.Textarea(attrs={"class":"form-control","rows":5})
        }

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User

        fields=["first_name","last_name","email","username","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()