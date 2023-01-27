from .models import *
from users.serializers import GroupSingerAllFieldsSerializer, PlaceAllFieldsSerializer
from rest_framework import serializers


class ConcertAllFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concert
        fields = "__all__"


class ConcertDetailSerializer(serializers.ModelSerializer):
    group = GroupSingerAllFieldsSerializer()
    place = PlaceAllFieldsSerializer()
    
    class Meta:
        model = Concert
        fields = "__all__"
