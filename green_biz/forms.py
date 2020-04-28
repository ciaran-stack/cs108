from django import forms
from .models import Organization, Initiative, SDG


class CreateOrgForm(forms.ModelForm):
    """form to add new orgs to the DB"""

    class Meta:
        """Associate this form with the Quote model"""
        model = Organization
        fields = ['name', 'industry', 'email_address', 'organization_picture_url', ]


class UpdateOrgForm(forms.ModelForm):
    """A form to update an org to the DB"""

    class Meta:
        """Associate this form with the Quote model"""
        model = Organization
        fields = ['name', 'email_address', 'industry', 'organization_picture_url', ]


class CreateInitiativeForm(forms.ModelForm):
    """form to add new status messages to the DB"""

    class Meta:
        """Associate this form with the Quote model"""
        model = Initiative
        fields = ['name', 'description', 'image', ]

