from rest_framework import serializers

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


class ToDoRelationshipsSerializer(serializers.Serializer):
  toDo = serializers.CharField(max_length=150)


class ToDoEnvironmentSerializer(serializers.Serializer):
  toDo = serializers.CharField(max_length=150)



class ToDoVocationSerializer(serializers.Serializer):
  toDo = serializers.CharField(max_length=150)


class ToDoProsperitySerializer(serializers.Serializer):
  toDo = serializers.CharField(max_length=150)


class ToDoSelfImprovementSerializer(serializers.Serializer):
  toDo = serializers.CharField(max_length=150)


class ToDoBrightnessOfLifeSerializer(serializers.Serializer):
  toDo = serializers.CharField(max_length=150)


class ToDoSpiritualitySerializer(serializers.Serializer):
  toDo = serializers.CharField(max_length=150)


