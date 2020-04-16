# import statements
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render

from .models import Profile, StatusMessage
from .forms import CreateProfileForm, UpdateProfileForm, CreateStatusMessageForm


class ShowAllProfilesView(ListView):
    """Create subclass of Listview to display Profiles"""

    model = Profile # retrieve the Profile object from DB
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'all_profiles_list'


class ShowProfilePageView(DetailView):
    """Create a subclass of DetailView to show a profile."""

    model = Profile
    template_name = 'mini_fb/show_profile_page.html'
    context_object_name = 'profile'


    def get_context_data(self, **kwargs):
        """Return the context data (a dictionary) to be used in the template."""

        # obtain the default context data (a dictionary) from the superclass;
        # this will include the Profile record for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)

        # create a new CreateStatusMessageForm
        create_status_form = CreateStatusMessageForm()

        # add it into the context dictionary
        context['create_status_form'] = create_status_form

        # return this context dictionary
        return context


class CreateProfileView(CreateView):
    """Create a subclass of CreateView to create a profile."""

    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'


class UpdateProfileView(UpdateView):
    """View to update a  quote and save it to the DB"""

    template_name = 'mini_fb/update_profile.html'
    form_class = UpdateProfileForm
    queryset = Profile.objects.all()


class DeleteStatusMessageView(DeleteView):
    """Delete a status and remove it from the DB."""

    template_name = 'mini_fb/delete_status.html'
    queryset = StatusMessage.objects.all()

    def get_object(self):
        """Return a StatusMessage object to be deleted"""
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']

        return StatusMessage.objects.get(pk=status_pk)

    def get_context_data(self, **kwargs):
        """Get the context data for template to use"""

        context = super(DeleteStatusMessageView, self).get_context_data(**kwargs)
        st_msg = StatusMessage.objects.get(pk=self.kwargs['status_pk'])
        context['st_msg'] = st_msg
        return context

    def get_success_url(self):
        """Redirect to URL if deleting is successful"""

        # get pk
        pk = self.kwargs.get('status_pk')
        status = StatusMessage.objects.filter(pk=pk).first()

        # get person associated w/ pk
        profile = status.profile
        return reverse('show_profile_page', kwargs={'pk': profile.pk})


def create_status_message(request, pk):
    """Process a form submission to post a new status message."""

    # find the profile that matches the `pk` in the URL
    profile = Profile.objects.get(pk=pk)

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # read the data from this form submission
        message = request.POST['message']
        image = request.FILES.get('image')

        # save the new status message object to the database
        if message:

            sm = StatusMessage()
            sm.profile = profile
            sm.message = message
            sm.image = image
            sm.save()

    # redirect the user to the show_profile_page view
    return redirect(reverse('show_profile_page', kwargs={'pk': pk}))


class ShowNewsFeedView(DetailView):
    """"A view to display a newsfeed and save it to the database."""

    model = Profile
    queryset = Profile.objects.all()
    context_object_name = 'profile'
    template_name = 'mini_fb/show_news_feed.html'


class ShowPossibleFriendsView(DetailView):
    """A view to display friend suggestions and save it to the database."""

    model = Profile
    queryset = Profile.objects.all()
    context_object_name = 'profile'
    template_name = 'mini_fb/show_possible_friends.html'


def add_friend(request, profile_pk, friend_pk):
    """The objective of this function is to process the add_friend request and to add a friend for a given profile."""

    # find the Profile object
    person_to_add_friend = Profile.objects.get(pk=profile_pk)

    # find the Profile object of the friend to add
    added_friend = Profile.objects.get(pk=friend_pk)

    # add that friend's Profile into the profile.friends object
    person_to_add_friend.friends.add(added_friend)

    # save the profile object
    added_friend.save()
    return redirect(reverse('show_profile_page', kwargs={'pk': profile_pk}))