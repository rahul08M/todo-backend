from django.apps.registry import apps
from rest_framework import serializers


User = apps.get_model('user', 'User')


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password',)

    def validate_username(self, value):

        if User.objects.filter(username=value):
            raise serializers.ValidationError('Username already exits.')
        return value