from django.shortcuts import render
from rest_framework import generics, status


# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from _auth.models import Customer, Manager
from _auth.permissions import ManagerPermission, CustomerPermission
from review.models import Review
from review.serializers import ReviewSerializer, ReplySerializer, ReviewFullSerializer


@api_view(['POST'])
@permission_classes([CustomerPermission])
def reviewCreate_view(request):
    customer = Customer.objects.get(id = request.user.id)
    if request.method == 'POST':
        serializer = ReviewSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(customer=customer)
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=500)


@api_view(['POST'])
@permission_classes([ManagerPermission])
def replyCreate_view(request, pk):
    review = Review.objects.get(id=pk)
    manager = Manager.objects.get(id = request.user.id)

    if request.method == 'POST':
        serializer = ReplySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(manager=manager, review = review)
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=500)


class reviewAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]

class reviewFullAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewFullSerializer
    permission_classes = [IsAuthenticated]