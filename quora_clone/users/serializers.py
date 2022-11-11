from .models import EndUser
from rest_framework import serializers

class EndUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndUser
        fields = ("username", "email", "password", "gender", "date_of_birth")
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = EndUser(
            email=validated_data['email'],
            username=validated_data['username'],
            gender=validated_data['gender'],
            date_of_birth=validated_data['date_of_birth']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user