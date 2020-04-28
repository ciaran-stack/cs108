from django.db import models
from django.urls import reverse


# Create your models here.
class Organization(models.Model):
    """Encapsulate idea of an Organization"""

    # data attributes
    name = models.TextField(blank=True)
    industry = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    organization_picture_url = models.URLField(blank=True)

    # establish relation between organizations
    peers = models.ManyToManyField("self")

    def __repr__(self):
        """Create string of object"""
        return '%s, %s, %s, %s,' % (
            self.name,  self.industry, self.email_address, self.organization_picture_url,)

    def __str__(self):
        """Create string of object"""
        return '%s, %s, %s, %s' % (self.name, self.industry, self.email_address, self.organization_picture_url)

    def get_name(self):
        """Return name of organization"""
        return self.name

    def get_status_initiatives(self):
        """Return status initiatives of organization"""
        inits = Initiative.objects.filter(organization=self.pk)
        return inits

    def get_absolute_url(self):
        """Return URL to display this organization object."""
        return reverse("show_org_page", kwargs={"pk": self.pk})

    def get_peers(self):
        """return a QuerySet of all peers for this Organization."""

        # return a QuerySet
        org = Organization.objects.filter(id=self.pk)[0]
        peers = org.peers.all()
        return peers

    def get_news_feed(self):
        """return a QuerySet of all statuses for this Organization."""

        peers = self.get_peers()
        news = Initiative.objects.filter(organization__in=peers)
        own = Initiative.objects.filter(organization=self.pk)
        news_page = news | own
        return news_page

    def get_peer_suggestions(self):
        """obtain and return a QuerySet of all Organization that could be added as peers."""

        peers = self.get_peers()
        peer_suggestions = Organization.objects.exclude(pk__in=peers).exclude(id=self.pk)
        return peer_suggestions


class Initiative(models.Model):
    """Idea of an Initiative"""

    # fields of an Initiative
    name = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)

    # foreign key to organization
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)

    def __repr__(self):
        return '%s, %s, %s' % (self.name, self.description, self.image)

    def __str__(self):
        return '%s, %s, %s' % (self.name, self.description, self.image)


class SDG(models.Model):
    """Idea of a UN SDG"""

    # fields of an Initiative
    name = models.TextField(blank=True)
    description = models.TextField(blank=True)
    picture_url = models.URLField(blank=True)

    def __repr__(self):
        return '%s, %s, %s' % (self.name, self.description, self.picture_url)

    def __str__(self):
        return '%s, %s, %s' % (self.name, self.description, self.picture_url)


