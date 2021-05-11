from rest_framework import serializers

from _auth.serializers import ManagerSerializer
from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    # quantity = serializers.IntegerField()
    class Meta:
        model = Event
        fields = ('title', 'image', 'manager')

class FullEventSerializer(EventSerializer):
    manager = ManagerSerializer()

    # quantity = serializers.IntegerField()
    class Meta(EventSerializer.Meta):
        model = Event
        fields = EventSerializer.Meta.fields + ('manager', 'description')
