
# import statements
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render


from .models import Profile, StatusMessage
from .forms import CreateProfileForm, UpdateProfileForm, CreateStatusMessage


class ShowAllProfilesView(ListView):
    """Create subclass of Listview to display Profiles"""

    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'all_profiles_list'


class ShowProfilePageView(DetailView):
    """Create a subclass of DetailView to show a profile."""

    model = Profile
    template_name = 'mini_fb/show_profile_page.html'
    #context_object_name = 'profile'
    #queryset = Profile.objects.all()

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass;
        # this will include the Profile record for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary

        create_status_form = CreateStatusMessage()
        context['create_status_form'] = create_status_form

        # return this context dictionary
        return context


class CreateProfileView(CreateView):
    """Create a subclass of CreateView to create a profile."""

    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'
    context_object_name = 'create_profile'




class UpdateProfileView(UpdateView):
    """View to update a  quote and save it to the DB"""

    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile.html'
    queryset = Profile.objects.all()


def create_status_message(request, pk):
    """
    Process a form submission to post a new status message.
    """
    # find the profile that matches the `pk` in the URL
    profile = Profile.objects.get(pk=pk)

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # read the data from this form submission
        message = request.POST['message']


        # save the new status message object to the database
        if message:

            sm = StatusMessage()
            sm.profile = profile
            sm.message = message
            sm.save()

    # redirect the user to the show_profile_page view
    url = reverse('show_profile_page', kwargs={'pk': pk})
    return redirect(url)

