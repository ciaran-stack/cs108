from django.urls import path
from .views import *
import random

urlpatterns = [
    path('', RandomQuotePageView.as_view(), name='random'),  # show one quote
    path('all', HomePageView.as_view(), name='home'), # generic class based view
    path('person/<int:pk>', PersonPageView.as_view(), name='person'), #show one profile
    path('create_quote', CreateQuoteView.as_view(), name='create_quote'), #create a new quote
    path('quote/<int:pk>', QuotePageView.as_view(), name='quote'), #show one quote
    path('quote/<int:pk>/update', UpdateQuoteView.as_view(), name='update_quote'), # update
]