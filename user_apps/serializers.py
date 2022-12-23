from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
    def create(self, validated_data):
        user = UserProfile.objects.create(
    						username=validated_data['username'],
    						email=validated_data['email'],
    						name=validated_data['name'],
    						)
        user.set_password(validated_data['password'])
        user.save()
        return user


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = '__all__'
    