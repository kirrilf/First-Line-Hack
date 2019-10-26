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
    