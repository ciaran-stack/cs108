from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.shortcuts import redirect
from .models import Quote, Person
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import random
from .forms import CreateQuoteForm, UpdateQuoteForm, AddImageForm




class HomePageView(ListView):
    '''Create subclass of Listview to display quotes'''

    model = Quote  # retrieve objects of type quote from DB
    template_name = 'quotes/home.html'
    context_object_name = 'all_quotes_list'  # how to find data in the template file all_quotes_list


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
        r = random.randint(0, len(all_quotes) - 1)
        q = all_quotes[r]
        return q  # return this object


class PersonPageView(DetailView):
    """Show all quotes and all images for one person."""

    model = Person
    template_name = 'quotes/person.html'
    #context_object_name = 'person'

    def get_context_data(self, **kwargs):
        """Return a dictionary with context data for this template to use."""

        # get default context data
        # this will include the Person record for this page view
        context = super(PersonPageView, self).get_context_data(**kwargs)

        # create add image form
        add_image_form = AddImageForm()
        context['add_image_form'] = add_image_form

        # return the context dictionary
        return context

class CreateQuoteView(CreateView):
    """View to create a new quote and save it to the DB"""

    form_class = CreateQuoteForm
    template_name = 'quotes/create_quote.html'
    context_object_name = 'create_quote'


class UpdateQuoteView(UpdateView):
    '''View to update a  quote and save it to the DB'''

    form_class = UpdateQuoteForm
    template_name = 'quotes/update_quote.html'
    queryset = Quote.objects.all()


class DeleteQuoteView(DeleteView):
    """Delete a quote and remove it from the DB."""

    template_name = 'quotes/delete_quote.html'
    queryset = Quote.objects.all()
    success_url = "../../all" # what to do after deleting a quote

    def get_success_url(self):
        """Return a URL to which we should be directed after the delete."""

        # Get the PK
        pk = self.kwargs.get('pk')
        quote = Quote.objects.filter(pk=pk).first() # one object from query set

        # Find the person associated with the PK
        person = quote.person
        return reverse('person', kwargs={'pk':person.pk})

        # Reverse to show the person page


def add_image(request, pk):
    """A custom view function to handle the submission of an image upload."""

    # find the person for whom we are submitting the image
    person = Person.objects.get(pk=pk)

    # read request data into AddImageForm object
    form = AddImageForm(request.POST or None, request.FILES or None)

    # check if form is valid, save to DB
    if form.is_valid():

        image = form.save(commit=False) # create the Image object, but not save
        image.person = person
        image.save() # story to the DB

    else:
        print("Error: The form was not valid ")

    # redirect to a new URL, display person page
    url = reverse('person', kwargs={'pk':pk})
    return redirect(url)