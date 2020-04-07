from django.db import models
import time
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

    def __repr__(self):
        """Create string of object"""
        return '%s, %s, %s, %s, %s,' % (
        self.first_name, self.last_name, self.city, self.email_address, self.profile_picture_url,)

    def __str__(self):
        """Create string of object"""
        return '%s, %s, %s, %s, %s' % (
        self.first_name, self.last_name, self.city, self.email_address, self.profile_picture_url,)

    def get_name(self):
        """Return name of profile"""
        return self.first_name

    def get_status_messages(self):
        """Return status messages of profile"""
        messages = StatusMessage.objects.filter(profile=self.pk)
        return messages

    def get_absolute_url(self):
        """Return URL to display this quote object."""
        return reverse("show_profile_page", kwargs={"pk": self.pk})


class StatusMessage(models.Model):
    """Idea of a status message"""

    message = models.TextField(blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    timestamp = time.ctime()

    def __repr__(self):
        return self.message

    def __str__(self):
        return self.message
