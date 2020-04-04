
from .models import Profile
from django.views.generic import ListView, DetailView

class ShowAllProfilesView(ListView):
    '''Create subclass of Listview to display Profiles'''

    model = Profile #retrieve objects of type quote from DB
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'all_profiles_list' # how to find data in the template all_profiles_list

class ShowProfilePageView(DetailView):
    '''Create a subclass of DetailView to show a profile.'''

    model = Profile
    template_name = 'mini_fb/show_profile_page.html'
    context_object_name = 'profile'
