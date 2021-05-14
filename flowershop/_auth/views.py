from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from _auth.models import Customer, Manager
from _auth.permissions import ManagerPermission, AdminPermission
from _auth.serializers import RegisterSerializer, UserSerializer, CustomerSerializer, ManagerSerializer, CustomerProfileSerializer
from rest_framework import mixins, viewsets

from ordering.models import Order


class RegisterAPIView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = RegisterSerializer


class CustomersViewSet(mixins. ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = [ManagerPermission]
    # queryset = Book.objects.all()
    # serializer_class = EventSerializer
    queryset = Customer.objects.get_related()
    # customer = Customer.objects.all()

    #
    # def get_queryset(self):
    #     return Events.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return UserSerializer
        return CustomerSerializer

class ManagersViewSet(viewsets.ModelViewSet):
    permission_classes = [AdminPermission]
    # queryset = Book.objects.all()
    # serializer_class = EventSerializer
    queryset = Manager.objects.get_related()
    # customer = Customer.objects.all()

    #
    # def get_queryset(self):
    #     return Events.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return UserSerializer
        return ManagerSerializer


class profileAPIView(APIView):
    def get(self, request):
        customer = Customer.objects.get(username=request.user)
        serializer = CustomerProfileSerializer(customer)
        return Response(serializer.data)
