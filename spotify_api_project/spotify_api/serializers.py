from rest_framework import serializers

class TrackSerializer(serializers.Serializer):
    artist_name = serializers.CharField()
    track_name = serializers.CharField()
    album_image = serializers.URLField()
    preview_url = serializers.URLField()
