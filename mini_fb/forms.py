from django import forms
from .models import Profile, StatusMessage


class CreateProfileForm(forms.ModelForm):
    """form to add new profiles to the DB"""

    class Meta:
        """Associate this form with the Quote model"""
        model = Profile
        fields = ['first_name', 'last_name', 'city', 'email_address', 'profile_picture_url', ]


class UpdateProfileForm(forms.ModelForm):
    """A form to update a profile to the DB"""

    class Meta:
        """Associate this form with the Quote model"""
        model = Profile
        fields = ['city', 'email_address', 'profile_picture_url', ]


class CreateStatusMessageForm(forms.ModelForm):
    """form to add new status messages to the DB"""

    class Meta:
        """Associate this form with the Quote model"""
        model = StatusMessage
        fields = ['message', 'image', ]






