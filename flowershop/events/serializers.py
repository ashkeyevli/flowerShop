from rest_framework import serializers

from events.models import Event


class EventSerializer(serializers.ModelSerializer):

    # quantity = serializers.IntegerField()
    class Meta:
        model = Event
        fields = ('id', 'title', 'image')

class FullEventSerializer(EventSerializer):
    # manager = ManagerSerializer(read_only=True)

    # quantity = serializers.IntegerField()
    class Meta(EventSerializer.Meta):
        model = Event
        fields = EventSerializer.Meta.fields + ('manager', 'description')

