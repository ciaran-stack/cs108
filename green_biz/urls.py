
from django.urls import path
from .views import *

urlpatterns = [
    path('', ShowAllOrganizationsView.as_view(), name='show_all_orgs'),
    path('organization/<int:pk>', ShowOrganizationPageView.as_view(), name='show_org_page'),
    path('create_org', CreateOrganizationView.as_view(), name='create_org'),
    path('organization/<int:pk>/update', UpdateOrgView.as_view(), name='update_org'),
    path('organization/<int:organization_pk>/delete_initiative/<int:initiative_pk>', DeleteInitiativeView.as_view(),
         name='delete_initiative'),
    path('organization/<int:pk>/post_initiative', create_initiative, name='post_initiative'),
    path('organization/<int:pk>/news_feed', ShowNewsFeedView.as_view(), name='news_feed'),
    path('organization/<int:pk>/show_possible_peers', ShowPossiblePeersView.as_view(), name='show_possible_peers'),
    path('organization/<int:organization_pk>/add_peer/<int:peer_pk>', add_peer, name='add_peer'),

]