from rest_framework import serializers

from .models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

    def create(self, validated_data):
        return Users.objects.create_user(**validated_data)
