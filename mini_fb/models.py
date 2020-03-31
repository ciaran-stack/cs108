from django.db import models

# Create your models here.

class Profile(models.Model):
    '''Encapsulate idea of a Profile'''

    #data attributes
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    profile_picture_url = models.URLField(blank=True)

    def __repr__(self):
        '''Create string of object'''
        return '%s, %s, %s, %s, %s,' % (self.first_name, self.last_name, self.city, self.email_address, self.profile_picture_url,)

    def __str__(self):
        '''Create string of object'''
        return '%s, %s, %s, %s, %s' % (self.first_name, self.last_name, self.city, self.email_address, self.profile_picture_url,)