from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from users.serializers import ConcertAllFieldsSerializer
from users.permissions import *
from .serializers import *


class ConcertView(APIView):

    def get(self, request):
        concert = Concert.objects.order_by("date")
        serializer = ConcertDetailSerializer(concert, many=True)
        return Response(serializer.data)


class ConcertCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated & IsPlaceUser]

    def post(self, request):
        serializer = ConcertAllFieldsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)


class ConcertMutationView(APIView):
    permission_classes = [permissions.IsAuthenticated & IsPlaceUser]

    def put(self, request, pk):
        concert = Concert.objects.get(id=pk)
        serializer = ConcertAllFieldsSerializer(concert, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(ConcertDetailSerializer(Concert.objects.get(id=pk)).data)
        else:
            return Response(status=400)

    def delete(self, request, pk):
        concert = Concert.objects.get(id=pk)
        concert.delete()
        return Response(status=201)
