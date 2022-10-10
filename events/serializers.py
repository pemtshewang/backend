from rest_framework.serializers import ModelSerializer
from .models import Event

class EventListSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
