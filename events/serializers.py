from rest_framework import serializers
from .models import Event, EventRegistration


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegistration
        fields = ['event', 'user']

    def validate(self, data):
        if EventRegistration.objects.filter(event=data['event'], user=data['user']).exists():
            raise serializers.ValidationError("User has already registered for this event.")
        return data