from django import forms
from .models import Quote

class CreateQuoteForm(forms.ModelForm):
    '''A form to add new quotes to the DB '''

    class Meta:
        '''Assocate this form with the Quote model'''
        model = Quote
        fields = ['person', 'text',] # determines which fields of model that we use'

class UpdateQuoteForm(forms.ModelForm):
    '''A form to update a quote to the DB'''

    class Meta:
        '''Assocate this form with the Quote model'''
        model = Quote
        fields = ['person', 'text',] # determines which fields of model that we use'