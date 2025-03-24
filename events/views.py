from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
from rest_framework import generics
from .models import EventRegistration
from .serializers import EventRegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'location', 'organizer']


class EventRegistrationView(generics.CreateAPIView):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer
    permission_classes = [IsAuthenticated]