from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from _auth.models import Manager
from _auth.permissions import ManagerPermission
from events.models import Event
from events.serializers import EventSerializer, FullEventSerializer


class EventViewSet(viewsets.ModelViewSet):
    # permission_classes = AllowAny
    # queryset = Book.objects.all()
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    @action(methods=['POST'], detail=False, url_path='create', permission_classes=(ManagerPermission,))
    def create_event(self, request):
        manager = Manager.objects.get(id = request.user.id)
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(manager=manager)
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=500)

    #
    # def get_queryset(self):
    #     return Events.objects.all()

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return EventSerializer
    #     elif self.action == 'create':
    #
    #         return EventSerializer
    #     return FullEventSerializer


    def get_permissions(self):
        if self.action == 'list':
            permission_classes = (AllowAny,)
        elif self.action == 'retrieve':
            permission_classes = (AllowAny,)
        else:
            permission_classes = (ManagerPermission,)

        return [permission() for permission in permission_classes]



    # def list(self, request):
    #     serializer = BookSerializer(self.get_queryset(), many=True)
    #     return Response(serializer.data)

    # @action(methods=['GET'], detail=False, url_path='inactive', url_name='in_active',
    #         permission_classes=(AuthorPermission,))
    #
    #     # filter = BookFilter(request.GET, queryset=Book.objects.all())
    #     # queryset = Book.objects.filter(is_active=False)
    #     serializer = BookSerializer(self.get_queryset(), many=True)
    #     return Response(serializer.data)
    #
    # @action(methods=['POST'], detail=False, permission_classes=(AllowAny,))
    # def create_book(self, request):
    #     serializer = BookSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     return Response('OK')