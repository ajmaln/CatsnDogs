from django.contrib.auth.models import User
from rest_framework import serializers
from main.models import Pet


class PetSerializer(serializers.ModelSerializer):
    PET_TYPES = (
        ('1', "Cat"),
        ('2', "Dog"),
    )
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username', required=False, many=False)
    type = serializers.ChoiceField(choices=PET_TYPES, required=False)

    class Meta:
        model = Pet
        fields = ['name', 'picture', 'age', 'type', 'owner']

    def create(self, validated_data):
        return Pet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.picture = validated_data.get('picture', instance.picture)
        instance.age = validated_data.get('age', instance.age)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance
