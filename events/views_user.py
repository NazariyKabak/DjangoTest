from rest_framework import generics
from django.contrib.auth.models import User

from .serializers_register_users import UserRegistrationSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
