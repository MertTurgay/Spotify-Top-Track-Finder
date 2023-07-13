from django.shortcuts import render
from django.http import JsonResponse
from .findTracks import find_tracks
from . import selectArtist
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TrackSerializer

class GetArtistsTopTracks(APIView):
    def get(self, request, genre):

        artist_name = selectArtist.get_random_artist_from_genre(genre)
        top_tracks = find_tracks(artist_name)

        tracks = []
        for track in top_tracks:
            tracks.append({
                'artist_name': track['artists'][0]['name'],
                'track_name': track['name'],
                'album_image': track['album']['images'][0]['url'],
                'preview_url': track['preview_url'],
            })
        serializer = TrackSerializer(tracks, many=True)
        return Response(serializer.data)
        #return JsonResponse({'tracks': tracks}, json_dumps_params={'indent': 2})



