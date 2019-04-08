from django import forms
from profiles.models import UserProfile
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user','listed_properties','contacted_properties')
    
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields=('username','email','password')
        help_texts = {
            'username': None,
            'email': None,
        }
