from django.shortcuts import render

# Create your views here.
from .models import Quote, Person
from django.views.generic import ListView, DetailView
import random

class HomePageView(ListView):
    '''Create subclass of Listview to display quotes'''

    model = Quote #retrieve objects of type quote from DB
    template_name = 'quotes/home.html'
    context_object_name = 'all_quotes_list' # how to find data in the template file all_quotes_list

class QuotePageView(DetailView):
    '''Show details for one quote.'''
    model = Quote
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'

class RandomQuotePageView(DetailView):
    '''Show details for one quote.'''
    model = Quote
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'

    # pick a quote at random
    def get_object(self):
        '''Return a single instance of a Quote object, selected at random.'''

        # get all quotes
        all_quotes = Quote.objects.all()

        # pick a random number
        r = random.randint(0, len(all_quotes) -1)
        q = all_quotes[r]
        return q # return this object

class PersonPageView(DetailView):
    '''Show all quotes and all images for one person.'''

    model = Person
    template_name = 'quotes/person.html'
    context_object_name = 'Person'
