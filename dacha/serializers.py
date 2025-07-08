from rest_framework import serializers

from .models import Dacha, DachaImage, DachaComment, DachaLike, DachaCommentLike, DachaRating, ClientType


class ClientTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientType
        fields = '__all__'


class DachaImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DachaImage
        fields = '__all__'


class DachaSerializer(serializers.ModelSerializer):
    images = DachaImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False),
        write_only=True,
        required=False
    )

    class Meta:
        model = Dacha
        fields = '__all__'

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        facilities_data = validated_data.pop('facilities', [])

        dacha = Dacha.objects.create(**validated_data)

        if facilities_data:
            dacha.facilities.set(facilities_data)

        for image_data in uploaded_images:
            DachaImage.objects.create(dacha=dacha, image=image_data)

        return dacha

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.popular_place = validated_data.get('popular_place', instance.popular_place)
        instance.facilities.set(validated_data.get('facilities', instance.facilities.all()))
        instance.beds_count = validated_data.get('beds_count', instance.beds_count)
        instance.hall_count = validated_data.get('hall_count', instance.hall_count)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.client_type = validated_data.get('client_type', instance.client_type)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.user = validated_data.get('user', instance.user)
        instance.transaction_type = validated_data.get('transaction_type', instance.transaction_type)
        instance.property_type = validated_data.get('property_type', instance.property_type)
        instance.save()

        if uploaded_images:
            instance.dachaimage_set.all().delete()
            for image_data in uploaded_images:
                DachaImage.objects.create(dacha=instance, image=image_data)
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = DachaImageSerializer(instance.dachaimage_set.all(), many=True).data
        return representation


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
