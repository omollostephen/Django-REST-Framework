from rest_framework import serializers
from watchmate_app.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
    
    #adding a function which capture data from user
    def create(self, validated_data):
        #create an instance
        return Movie.objects.create(**validated_data)
    #geting updated details
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
    #creating validation
    #1. object-level validate
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and description can''t be the same')
        else:
            return data
    #2. field-level validation
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Name must be at least 2 characters long')
        else:
            return value