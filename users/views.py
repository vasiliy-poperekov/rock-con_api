from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from .permissions import *

from .serializers import *


class PlaceSignupView(generics.GenericAPIView):
    serializer_class = PlaceSignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'id': user.id,
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': Token.objects.get(user=user).key,
            'message': "account created successfully"
        })


class GroupSingerSignupView(generics.GenericAPIView):
    serializer_class = GroupSingerSignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'id': user.id,
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': Token.objects.get(user=user).key,
            'message': "account created successfully"
        })


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'is_group_singer': user.is_group_singer,
            'is_place': user.is_place
        })


class LogoutView(APIView):
    def post(self, request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)


class GroupSingerOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated & IsGroupSingerUser]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class PlaceOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated & IsGroupSingerUser]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class PlaceView(APIView):
    def get(self, request):
        places = Place.objects
        serializer = PlacesListSerializer(places, many=True)
        return Response(serializer.data)


class PlaceDetailsView(APIView):
    def get(self, request, pk):
        place = Place.objects.get(id=pk)
        serializer = PlaceDetailSerializer(place)
        return Response(serializer.data)


class PlaceMutationView(APIView):
    permission_classes = [permissions.IsAuthenticated & IsPlaceUser]

    def put(self, request, pk):
        place = Place.objects.get(id=pk)
        serializer = PlacePutFieldsSerializer(place, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(PlaceDetailSerializer(Place.objects.get(id=pk)).data)
        else:
            return Response(status=400)

    def delete(self, request, pk):
        place = Place.objects.get(id=pk)
        place.delete()
        return Response(status=201)


class GroupSingerView(APIView):
    def get(self, request):
        groups = GroupSinger.objects
        serializer = GroupSingerListSerializer(groups, many=True)
        return Response(serializer.data)


class GroupSingerDetailsView(APIView):
    def get(self, request, pk):
        group_singer = GroupSinger.objects.get(id=pk)
        serializer = GroupSingerDetailSerializer(group_singer)
        return Response(serializer.data)


class GroupSingerMutationView(APIView):
    permission_classes = [permissions.IsAuthenticated & IsGroupSingerUser]

    def put(self, request, pk):
        group_singer = GroupSinger.objects.get(id=pk)
        serializer = GroupSingerPutFieldsSerializer(group_singer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(GroupSingerDetailSerializer(GroupSinger.objects.get(id=pk)).data)
        else:
            return Response(status=400)

    def delete(self, request, pk):
        group = GroupSinger.objects.get(id=pk)
        group.delete()
        return Response(status=201)


class GroupImageView(APIView):
    permission_classes = [permissions.IsAuthenticated & IsGroupSingerUser]

    def put(self, request, pk):
        group = GroupSinger.objects.get(id=pk)
        serializer = PutGroupImageSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "done"})
        return Response(serializer.errors)


class PlaceImageView(APIView):
    permission_classes = [permissions.IsAuthenticated & IsPlaceUser]

    def put(self, request, pk):
        place = Place.objects.get(id=pk)
        serializer = PutPlaceImageSerializer(place, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "done"})
        return Response(serializer.errors)
