from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    """form to add new profiles to the DB"""

    class Meta:
        '''Assocate this form with the Quote model'''
        model = Profile
        fields = ['first_name', 'last_name', 'city', 'email_address', 'profile_picture_url']