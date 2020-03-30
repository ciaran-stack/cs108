from django.shortcuts import render

# Create your views here.
from .models import Quote
from django.views.generic import ListView

class HomePageView(ListView):
    '''Create subclass of Listview to display quotes'''

    model = Quote #retrieve objects of type quote from DB
    template_name = 'quotes/home.html'
    context_object_name = 'all_quotes_list' # how to find data in the template file