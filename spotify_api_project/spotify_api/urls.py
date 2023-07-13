from django.urls import path, include

from spotify_api import views

urlpatterns = [
    path('tracks/<str:genre>/', views.GetArtistsTopTracks.as_view(), )
]