from django.shortcuts import render
from rest_framework import generics, status


# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from _auth.models import Customer, Manager
from review.models import Review
from review.serializers import ReviewSerializer, ReplySerializer


#
# class InvoiceAPIView(APIView):
#     def post(self, request):
#         serializer = ReviewSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(customer=request.user)
#         return Response(status=status.HTTP_201_CREATED)
@api_view(['POST'])
def reviewCreate_view(request):
    customer = Customer.objects.get(id = request.user.id)

    if request.method == 'POST':

        serializer = ReviewSerializer(data = request.data)

        # serializer.customer = customer
        if serializer.is_valid():
            serializer.save(customer=customer)
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=500)


@api_view(['POST'])
def replyCreate_view(request, pk):
    review = Review.objects.get(id=pk)
    manager = Manager.objects.get(id = request.user.id)

    if request.method == 'POST':

        serializer = ReplySerializer(data = request.data)

        # serializer.customer = customer
        if serializer.is_valid():
            serializer.save(manager=manager, review = review)
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=500)


class reviewAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
