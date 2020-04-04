from django.db import models
import random

# Create your models here.

class Person(models.Model):
    '''Encapsulate idea of a person, who said a famous quote.'''
    name = models.TextField(blank=False)

    def __str__(self):
        '''Return string representation of this person.'''
        return self.name

    # Get an image at random
    def get_random_image(self):
        '''Return an image of this person at random.'''

        # get all images of this person
        images = Image.objects.filter(person=self.pk)

        # pick a photo and return
        i = random.randint(0, len(images) - 1)

        return images[i]

    # Get all images of a person
    def get_all_images(self):
        '''Returns queryset of all images of a person'''
        images = Image.objects.filter(person=self.pk)
        return images

    def get_all_quotes(self):
        quotes = Quote.objects.filter(person=self.pk)
        return quotes


class Quote(models.Model):
    '''Encapsulate idea of a quote.'''

    #data attributes
    text = models.TextField(blank=True)
    person = models.ForeignKey('Person', on_delete="CASCADE ")

    def __str__(self):
        '''Create string of object'''
        return '"%s" - %s' % (self.text, self.person.name)

class Image(models.Model):
    '''Represent an image which is associated with a person.'''
    image_url = models.URLField(blank=True)
    person = models.ForeignKey('Person', on_delete="Cascade")

    def __str__(self):
        '''Return a string representation of this image.'''
        return self.image_url
