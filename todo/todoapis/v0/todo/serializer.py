from rest_framework import serializers
from django.apps.registry import apps


Tasks = apps.get_model('notes', 'Tasks')


class NotesSerializers(serializers.ModelSerializer):

    title = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Tasks
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        object = Tasks.objects.create(**validated_data)
        return object
