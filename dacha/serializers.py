from rest_framework import serializers

from .models import Dacha, DachaImage, DachaComment, DachaLike, DachaCommentLike, DachaRating


class DachaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dacha
        fields = '__all__'


class DachaImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DachaImage
        fields = '__all__'


class DachaCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DachaComment
        fields = '__all__'


class DachaLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DachaLike
        fields = '__all__'


class DachaCommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DachaCommentLike
        fields = '__all__'


class DachaRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DachaRating
        fields = '__all__'
