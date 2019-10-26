from rest_framework import serializers
from .models import *

class WheelSerializer(serializers.Serializer):
   
    health = serializers.IntegerField()
    relationships = serializers.IntegerField()
    environment = serializers.IntegerField()
    vocation = serializers.IntegerField()
    prosperity = serializers.IntegerField()
    selfImprovement = serializers.IntegerField()
    brightnessOfLife = serializers.IntegerField()
    spirituality = serializers.IntegerField()
    



class ToDoHealthSerializer(serializers.Serializer):
  toDo = serializers.CharField(max_length=150)
  id = serializers.IntegerField()

  def create(self, validated_data):
    return ToDoHealth.objects.create(**validated_data)


class ToDoRelationshipsSerializer(serializers.Serializer):
  toDo = serializers.CharField(max_length=150)
  id = serializers.IntegerField()

  def create(self, validated_data):
    return ToDoRelationships.objects.create(**validated_data)


class ToDoEnvironmentSerializer(serializers.Serializer):
  toDo = serializers.CharField(max_length=150)
  id = serializers.IntegerField()

  def create(self, validated_data):
    return ToDoEnvironment.objects.create(**validated_data)

  
class ToDoVocationSerializer(serializers.Serializer):
  toDo = serializers.CharField(max_length=150)
  id = serializers.IntegerField()

  def create(self, validated_data):
    return ToDoVocation.objects.create(**validated_data)

class ToDoProsperitySerializer(serializers.Serializer):
  toDo = serializers.CharField(max_length=150)
  id = serializers.IntegerField()

  def create(self, validated_data):
    return ToDoProsperity.objects.create(**validated_data)

class ToDoSelfImprovementSerializer(serializers.Serializer):
  toDo = serializers.CharField(max_length=150)
  id = serializers.IntegerField()

  def create(self, validated_data):
    return ToDoSelfImprovement.objects.create(**validated_data)

class ToDoBrightnessOfLifeSerializer(serializers.Serializer):
  toDo = serializers.CharField(max_length=150)
  id = serializers.IntegerField()

  def create(self, validated_data):
    return ToDoBrightnessOfLife.objects.create(**validated_data)

class ToDoSpiritualitySerializer(serializers.Serializer):
  toDo = serializers.CharField(max_length=150)
  id = serializers.IntegerField()

  def create(self, validated_data):
    return ToDoSpirituality.objects.create(**validated_data)

