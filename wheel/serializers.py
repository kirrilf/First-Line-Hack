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
    



class SubParagraphsHealthSerializer(serializers.Serializer):
  #category = serializers.ForeignKey("Health", related_name='subparagraphsHealth', on_delete=serializers.CASCADE)
  subparagraphs = serializers.CharField(max_length=150)


class SubParagraphsRelationshipsSerializer(serializers.Serializer):
  #category = serializers.ForeignKey("Relationships", related_name='subparagraphsRelationships', on_delete=serializers.CASCADE)
  subparagraphs = serializers.CharField(max_length=150)


class SubparagraphsEnvironmentSerializer(serializers.Serializer):
  #category = serializers.ForeignKey("Environment", related_name='subparagraphsEnvironment', on_delete=serializers.CASCADE)
  subparagraphs = serializers.CharField(max_length=150)



class SubparagraphsVocationSerializer(serializers.Serializer):
  #category = serializers.ForeignKey("Vocation", related_name='subparagraphsVocation', on_delete=serializers.CASCADE)
  subparagraphs = serializers.CharField(max_length=150)


class SubparagraphsProsperitySerializer(serializers.Serializer):
  #category = serializers.ForeignKey("Prosperity", related_name='subparagraphsProsperity', on_delete=serializers.CASCADE)
  subparagraphs = serializers.CharField(max_length=150)


class SubparagraphsSelfImprovementSerializer(serializers.Serializer):
  #category = serializers.ForeignKey("SelfImprovement", related_name='subparagraphsSelfImprovement', on_delete=serializers.CASCADE)
  subparagraphs = serializers.CharField(max_length=150)


class SubparagraphsBrightnessOfLifeSerializer(serializers.Serializer):
  #category = serializers.ForeignKey("BrightnessOfLife", related_name='subparagraphsBrightnessOfLife', on_delete=serializers.CASCADE)
  subparagraphs = serializers.CharField(max_length=150)


class SubparagraphsSpiritualitySerializer(serializers.Serializer):
  #category = serializers.ForeignKey("Spirituality", related_name='subparagraphsSpirituality', on_delete=serializers.CASCADE)
  subparagraphs = serializers.CharField(max_length=150)


