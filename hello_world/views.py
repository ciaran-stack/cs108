from django.shortcuts import render

# Create your views here.
# create response to web request
from django.http import HttpResponse

import time


def homePageView(request):
    '''Respond to an HTTP request with a simple webpage.'''

    response_html = '''
    <html>
    <h1> Hello, world! </h1>
    <p>
    This is our first Django app!
    </p>
    <hr>
    This was generated at %s
    </html>
    ''' %time.ctime()
    return HttpResponse(response_html)