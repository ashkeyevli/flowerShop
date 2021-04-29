from django.shortcuts import render
from rest_framework import generics, status
import logging
from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# Create your views here.
from product.models import Category, Flower
from product.serializers import CateogriesSerializer, FlowerSerializer, FlowerNewSerializer


@api_view(['GET', 'POST'])
def categories_view(request):
    if request.method == 'GET':
        category_items = Category.objects.all()
        serializer = CateogriesSerializer(category_items, many=True)
        return Response(serializer.data, status=200)
    elif request.method == 'POST':
        serializer = CateogriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=500)

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CateogriesSerializer


# class CategoryFlowers(generics.ListCreateAPIView):
#     queryset = Flower.objects.all()
#     serializer_class = FlowerSerializer

class FlowerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
     queryset = Flower.objects.all()
     serializer_class = FlowerSerializer


@api_view(['GET', 'POST'])
def flowers_view(request, pk):
    try:
        flowers = Flower.objects.filter(category=pk)
    except Flower.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = FlowerNewSerializer(flowers, many=True)
        return Response(serializer.data, status=200)

    elif request.method == 'POST':
        context = {"category_id": pk}

        serializer = FlowerNewSerializer(data=request.data, context = context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=500)





# class FlowersViewSet(APIView,viewsets.ViewSet):
#     permission_classes = (AllowAny,)
#     # queryset = Book.objects.all()
#     serializer_class = FlowerSerializer
#     # queryset = Flower.objects.all()
#
#     def get_object(self, pk):
#          try:
#              return Category.objects.get(category=pk)
#          except Category.DoesNotExist as e:
#                      return Response({'error': str(e)})
#
#     def get(self, request, pk):
#         category = self.get_object(pk)
#         flowers = category.flowers
#         serializer = FlowerSerializer(flowers, many=True)
#         return Response(serializer.data)
#     def post(self, request, pk):
#         category = self.get_object(pk)
#         flower = category.flowers
#         serializer = FlowerSerializer(instance=flower, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response({'error': serializer.errors},
#                         status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # pagination_class = LimitOffsetPagination
    # def get_queryset(self):
    #     return Flower.objects.all()
    #
    #
    # @action(methods=['GET'], detail=True,
    #         permission_classes=(AllowAny,))
    # def available(self, request, pk):
    #     # filter = BookFilter(request.GET, queryset=Book.objects.all())
    #     # queryset = Book.objects.filter(is_active=False)
    #     queryset = Flower.objects.get(category=pk)
    #     serializer = FlowerSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # @action(methods=['POST'], detail=False, permission_classes=(AllowAny,))
    # def create_flower(self, request):
    #     serializer = FlowerSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     return Response('OK')



# class FlowersAPIView(APIView):
#
#     # queryset = Flower.objects.all()
#     # serializer_class = FlowerSerializer
#     def get_object(self, pk):
#         try:
#             return Category.objects.get(id=pk)
#         except Category.DoesNotExist as e:
#             return Response({'error': str(e)})
#
#     def get(self, request, pk):
#         category = self.get_object(pk)
#         flowers = category.flowers
#         serializer = FlowerSerializer(flowers, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, pk):
#         category = self.get_object(pk)
#
#         flower = category.flowers
#         serializer = FlowerSerializer(instance=flower, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response({'error': serializer.errors},
#                         status=status.HTTP_500_INTERNAL_SERVER_ERROR)