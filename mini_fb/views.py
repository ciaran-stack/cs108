from .models import Profile, StatusMessage
from django.views.generic import ListView, DetailView, CreateView
from .forms import CreateProfileForm


class ShowAllProfilesView(ListView):
    '''Create subclass of Listview to display Profiles'''

    model = Profile  # retrieve objects of type quote from DB
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'all_profiles_list'  # how to find data in the template all_profiles_list


class ShowProfilePageView(DetailView):
    '''Create a subclass of DetailView to show a profile.'''

    model = Profile
    template_name = 'mini_fb/show_profile_page.html'
    context_object_name = 'profile'


class CreateProfileView(CreateView):
    '''Create a subclass of CreateView to create a profile.'''

    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html.'
    context_object_name = 'create_profile'
