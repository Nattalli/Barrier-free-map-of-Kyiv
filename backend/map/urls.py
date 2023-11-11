from django.urls import path
from .views import *


urlpatterns = [
    path('streets/', StreetListCreateView.as_view(), name='street-list'),
    path('streets/<str:pk>/', StreetDetailView.as_view(), name='street-detail'),

    path('adjacentstreets/', AdjacentStreetListCreateView.as_view(), name='adjacentstreet-list'),
    path('adjacentstreets/<str:pk>/', AdjacentStreetDetailView.as_view(), name='adjacentstreet-detail'),

    path('sidewalks/', SidewalkListCreateView.as_view(), name='sidewalk-list'),
    path('sidewalks/<str:pk>/', SidewalkDetailView.as_view(), name='sidewalk-detail'),

    path('sidewalkmaps/', SidewalkMapListCreateView.as_view(), name='sidewalkmap-list'),
    path('sidewalkmaps/<str:pk>/', SidewalkMapDetailView.as_view(), name='sidewalkmap-detail'),

    path('commitissues/', CommitIssueListCreateView.as_view(), name='commitissue-list'),
    path('commitissues/<str:pk>/', CommitIssueDetailView.as_view(), name='commitissue-detail'),

    path('sidewalkissues/', SidewalkIssueListCreateView.as_view(), name='sidewalkissue-list'),
    path('sidewalkissues/<str:pk>/', SidewalkIssueDetailView.as_view(), name='sidewalkissue-detail'),

    path('sidewalkissueborders/', SidewalkIssueBorderListCreateView.as_view(), name='sidewalkissueborder-list'),
    path('sidewalkissueborders/<str:pk>/', SidewalkIssueBorderDetailView.as_view(), name='sidewalkissueborder-detail'),

    path('crosswalks/', CrosswalkListCreateView.as_view(), name='crosswalk-list'),
    path('crosswalks/<str:pk>/', CrosswalkDetailView.as_view(), name='crosswalk-detail'),

    path('crosswalkissues/', CrosswalkIssueListCreateView.as_view(), name='crosswalkissue-list'),
    path('crosswalkissues/<str:pk>/', CrosswalkIssueDetailView.as_view(), name='crosswalkissue-detail'),

    path('crosswalkbenefits/', CrosswalkBenefitListCreateView.as_view(), name='crosswalkbenefit-list'),
    path('crosswalkbenefits/<str:pk>/', CrosswalkBenefitDetailView.as_view(), name='crosswalkbenefit-detail'),

    path('crosswalkdirections/', CrosswalkDirectionListCreateView.as_view(), name='crosswalkdirection-list'),
    path('crosswalkdirections/<str:pk>/', CrosswalkDirectionDetailView.as_view(), name='crosswalkdirection-detail'),
]
