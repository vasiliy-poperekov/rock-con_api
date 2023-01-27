from .models import *
from concert.models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class GroupSingerSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(username=self.validated_data['username'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': "password do not match"})
        user.set_password(password)
        user.is_group_singer = True
        user.save()

        GroupSinger.objects.create(id=user.id, user=user)

        return user


class PlaceSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(username=self.validated_data['username'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': "password do not match"})
        user.set_password(password)
        user.is_place = True
        user.save()

        Place.objects.create(id=user.id, user=user)

        return user


class ConcertAllFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concert
        fields = "__all__"


class GroupSingerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupSinger
        fields = ("id", "name", "profile_photo", "genres")


class PlacesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ("id", "name", "profile_photo", "address")


class GroupSingerAllFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupSinger
        fields = "__all__"


class GroupSingerPutFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupSinger
        fields = ("name", "genres", "description")


class GroupSingerDetailSerializer(serializers.ModelSerializer):
    concerts = ConcertAllFieldsSerializer(many=True)

    class Meta:
        model = GroupSinger
        fields = "__all__"


class PlaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupSinger
        fields = ("id", "name", "profile_photo")


class PlaceAllFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"


class PlacePutFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ("name", "place_type", "description", "address", "phone_number")


class PlaceDetailSerializer(serializers.ModelSerializer):
    concerts = ConcertAllFieldsSerializer(many=True)

    class Meta:
        model = Place
        fields = "__all__"


class PutGroupImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupSinger
        fields = ("profile_photo", "image1", "image2", "image3")


class PutPlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ("profile_photo", "image1", "image2", "image3")
