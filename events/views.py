from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
from rest_framework import generics
from .models import EventRegistration
from .serializers import EventRegistrationSerializer
from rest_framework.permissions import IsAuthenticated

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventRegistrationView(generics.CreateAPIView):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer
    permission_classes = [IsAuthenticated]