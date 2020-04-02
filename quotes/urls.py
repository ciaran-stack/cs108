from django.urls import path
from .views import HomePageView, QuotePageView, RandomQuotePageView
import random

urlpatterns = [
    path('all', HomePageView.as_view(), name='home'), # generic class based view
    path('quote/<int:pk>', QuotePageView.as_view(), name='quote'),
    path('', RandomQuotePageView.as_view(), name='random'),# show one quote
]