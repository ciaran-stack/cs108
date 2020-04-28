from django.db import models
from django.urls import reverse


# Create your models here.
class Profile(models.Model):
    """Encapsulate idea of a Profile"""

    # data attributes
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    profile_picture_url = models.URLField(blank=True)

    # establish relation between profiles
    friends = models.ManyToManyField("self")

    def __repr__(self):
        """Create string of object"""
        return '%s, %s, %s, %s, %s,' % (
            self.first_name, self.last_name, self.city, self.email_address, self.profile_picture_url,)

    def __str__(self):
        """Create string of object"""
        return '%s, %s, %s, %s, %s' % (self.first_name, self.last_name, self.city, self.email_address, self.profile_picture_url)

    def get_name(self):
        """Return name of profile"""
        return self.first_name

    def get_status_messages(self):
        """Return status messages of profile"""
        messages = StatusMessage.objects.filter(profile=self.pk)
        return messages

    def get_absolute_url(self):
        """Return URL to display this profile object."""
        return reverse("show_profile_page", kwargs={"pk": self.pk})

    def get_friends(self):
        """return a QuerySet of all friends for this Profile."""

        # return a QuerySet
        person = Profile.objects.filter(id=self.pk)[0]
        friends = person.friends.all()
        return friends

    def get_news_feed(self):
        """return a QuerySet of all statuses for this Profile."""

        friends = self.get_friends()
        news = StatusMessage.objects.filter(profile__in=friends).order_by("-timestamp")
        own = StatusMessage.objects.filter(profile=self.pk)
        news_page = news | own
        return news_page

    def get_friend_suggestions(self):
        """obtain and return a QuerySet of all Profile that could be added as friends."""

        friends = self.get_friends()
        friend_suggestions = Profile.objects.exclude(pk__in=friends).exclude(id=self.pk)
        return friend_suggestions


class StatusMessage(models.Model):
    """Idea of a status message"""

    # fields of a Status Message
    message = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    # foreign key to profile
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __repr__(self):
        return '%s, %s, %s' % (self.message, self.timestamp, self.image)

    def __str__(self):
        return '%s, %s, %s' % (self.message, self.timestamp, self.image)
