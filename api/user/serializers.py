from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = get_user_model()
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'avatar', 'password')  # noqa:E501
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """Create and return a new user"""
        # user = get_user_model().objects.create_user(
        #     email=validated_data['email'],
        #     password=validated_data['password'],
        #     first_name=validated_data['first_name'],
        #     last_name=validated_data['last_name'],
        # )
        # return user
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return a user."""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user
