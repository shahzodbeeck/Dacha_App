from rest_framework import viewsets

from .models import Dacha, DachaImage, DachaComment, DachaLike, DachaCommentLike, DachaRating, ClientType
from .serializers import DachaSerializer, DachaImageSerializer, DachaCommentSerializer, DachaLikeSerializer, \
    DachaCommentLikeSerializer, DachaRatingSerializer, ClientTypeSerializer


class DachaViewSet(viewsets.ModelViewSet):
    queryset = Dacha.objects.all()
    serializer_class = DachaSerializer


class DachaImageViewSet(viewsets.ModelViewSet):
    queryset = DachaImage.objects.all()
    serializer_class = DachaImageSerializer


class DachaCommentViewSet(viewsets.ModelViewSet):
    queryset = DachaComment.objects.all()
    serializer_class = DachaCommentSerializer


class DachaLikeViewSet(viewsets.ModelViewSet):
    queryset = DachaLike.objects.all()
    serializer_class = DachaLikeSerializer


class DachaCommentLikeViewSet(viewsets.ModelViewSet):
    queryset = DachaCommentLike.objects.all()
    serializer_class = DachaCommentLikeSerializer


class DachaRatingViewSet(viewsets.ModelViewSet):
    queryset = DachaRating.objects.all()
    serializer_class = DachaRatingSerializer


class ClientTypeViewSet(viewsets.ModelViewSet):
    queryset = ClientType.objects.all()
    serializer_class = ClientTypeSerializer


class UserDachasViewSet(viewsets.ModelViewSet):
    queryset = Dacha.objects.all()
    serializer_class = DachaSerializer

    def get_queryset(self):
        return Dacha.objects.filter(user=self.request.user)
