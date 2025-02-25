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
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.profileColor = validated_data.get('profileColor', instance.profileColor)
        instance.save()
        return instance
