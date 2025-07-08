from rest_framework import viewsets

from .models import Users
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class UserMeViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return Users.objects.filter(id=self.request.user.id)
