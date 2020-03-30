from django.db import models

# Create your models here.

class Quote(models.Model):
    '''Encapsulate idea of a quote'''

    #data attributes
    text = models.TextField(blank=True)
    author = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __repr__(self):
        '''Create string of object'''
        return '"%s" - %s' % (self.text, self.author)