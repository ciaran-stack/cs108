# import
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render

from .models import Organization, Initiative, SDG
from .forms import CreateInitiativeForm, CreateOrgForm, UpdateOrgForm


class ShowAllOrganizationsView(ListView):
    """Create subclass of Listview to display Orgs"""

    model = Organization # retrieve the Organization object from DB
    template_name = 'green_biz/show_all_orgs.html'
    context_object_name = 'all_orgs_list'


class ShowOrganizationPageView(DetailView):
    """Create a subclass of DetailView to show an Organization."""

    model = Organization
    template_name = 'green_biz/show_org_page.html'
    context_object_name = "organization"

    def get_context_data(self, **kwargs):
        """Return the context data (a dictionary) to be used in the template."""

        # obtain the default context data (a dictionary) from the superclass;
        # this will include the Profile record for this page view
        context = super(ShowOrganizationPageView, self).get_context_data(**kwargs)

        # create a new CreateInitiativeForm
        create_initiative_form = CreateInitiativeForm()

        # add it into the context dictionary
        context['create_initiative_form'] = create_initiative_form

        # return this context dictionary
        return context


class CreateOrganizationView(CreateView):
    """Create a subclass of CreateView to create an org."""

    form_class = CreateOrgForm
    template_name = 'green_biz/create_org_form.html'


class UpdateOrgView(UpdateView):
    """View to update an Org and save it to the DB"""

    template_name = 'green_biz/update_org.html'
    form_class = UpdateOrgForm
    queryset = Organization.objects.all()


class DeleteInitiativeView(DeleteView):
    """Delete an Initiative and remove it from the DB."""

    template_name = 'green_biz/delete_initiative.html'
    queryset = Initiative.objects.all()

    def get_object(self):
        """Return an Initiative object to be deleted"""
        organization_pk = self.kwargs['organization_pk']
        initiative_pk = self.kwargs['initiative_pk']

        return Initiative.objects.get(pk=initiative_pk)

    def get_context_data(self, **kwargs):
        """Get the context data for template to use"""

        context = super(DeleteInitiativeView, self).get_context_data(**kwargs)
        init = Initiative.objects.get(pk=self.kwargs['initiative_pk'])
        context['init'] = init
        return context

    def get_success_url(self):
        """Redirect to URL if deleting is successful"""

        # get pk
        pk = self.kwargs.get('initiative_pk')
        initiative = Initiative.objects.filter(pk=pk).first()

        # get org associated w/ pk
        organization = initiative.organization
        return reverse('show_org_page', kwargs={'pk': organization.pk})


def create_initiative(request, pk):
    """Process a form submission to post a new initiative."""

    # find the profile that matches the `pk` in the URL
    organization = Organization.objects.get(pk=pk)

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # read the data from this form submission
        name = request.POST['name']
        description = request.POST['description']
        image = request.FILES.get('image')

        # save the new initiative object to the database
        if name:

            init = Initiative()
            init.organization = organization
            init.name = name
            init.description = description
            init.image = image
            init.save()

    # redirect the user to the show_org_page view
    return redirect(reverse('show_org_page', kwargs={'pk': pk}))


class ShowNewsFeedView(DetailView):
    """"A view to display a newsfeed and save it to the database."""

    model = Organization
    queryset = Organization.objects.all()
    context_object_name = 'organization'
    template_name = 'green_biz/show_news_feed.html'


class ShowPossiblePeersView(DetailView):
    """A view to display peer suggestions and save it to the database."""

    model = Organization
    queryset = Organization.objects.all()
    context_object_name = 'organization'
    template_name = 'green_biz/show_possible_peers.html'


def add_peer(request, organization_pk, peer_pk):
    """The objective of this function is to process the add_peer request and to add a peer for a given org."""

    # find the org object
    org_to_add_peer = Organization.objects.get(pk=organization_pk)

    # find the org object of the peer to add
    added_peer = Organization.objects.get(pk=peer_pk)

    # add that peer's Profile into the profile.peers object
    org_to_add_peer.peers.add(added_peer)

    # save the profile object
    added_peer.save()
    return redirect(reverse('show_org_page', kwargs={'pk': organization_pk}))
