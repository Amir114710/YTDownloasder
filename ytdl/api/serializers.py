from rest_framework import serializers
from ytdl.models import *

class YtdlSerializer(serializers.Serializer):
    url = serializers.CharField()

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('__all__')