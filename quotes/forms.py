from django import forms
from .models import Quote, Image


class CreateQuoteForm(forms.ModelForm):
    """A form to add new quotes to the DB """

    class Meta:
        """Associate this form with the Quote model"""
        model = Quote
        fields = ['person', 'text', ]  # determines which fields of model that we use'


class AddImageForm(forms.ModelForm):
    """A form to collect an image from the user."""

    class Meta:
        model = Image
        fields = ["image_file", ]


class UpdateQuoteForm(forms.ModelForm):
    """A form to update a quote to the DB"""

    class Meta:
        """Associate this form with the Quote model"""
        model = Quote
        fields = ['person', 'text', ]  # determines which fields of model that we use'
