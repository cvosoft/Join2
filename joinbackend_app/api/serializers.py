from rest_framework import serializers
from joinbackend_app.models import Contact


class ContactSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=254)
    phone_number = serializers.CharField(max_length=30)
    profileColor = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return Contact.objects.create(**validated_data)
