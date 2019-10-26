from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

class WheelView(APIView):

    def get(self, request):
        wheel = Wheel.objects.all()

        serializer = WheelSerializer(wheel, many=True)
       
        return Response(serializer.data)
    
class HealthView(APIView):
    
     def get(self, request):

        #obj = Health.objects.all().prefetch_related('many_set')
        #one_objs = One.objects.all().prefetch_related('many_set')
        obj = SubParagraphsHealth.objects.all()
        serializer = SubParagraphsHealthSerializer(obj, many=True)

        return Response({"Health": serializer.data})
    
  
class RelationshipsView(APIView):
    def get(self, request):
        obj = SubParagraphsRelationships.objects.all()
        serializer = SubParagraphsRelationshipsSerializer(obj, many=True)

        return Response({"Relationships": serializer.data})

class EnvironmentView(APIView):
    def get(self, request):

        obj = SubparagraphsEnvironment.objects.all()
        serializer = SubparagraphsEnvironmentSerializer(obj, many=True)

        return Response({"Environment": serializer.data})


class VocationView(APIView):
    def get(self, request):
        obj = SubparagraphsVocation.objects.all()
        serializer = SubparagraphsVocationSerializer(obj, many=True)

        return Response({"Vocation": serializer.data})

class ProsperityView(APIView):
    def get(self, request):
        obj = SubparagraphsProsperity.objects.all()
        serializer = SubparagraphsProsperitySerializer(obj, many=True)

        return Response({"Prosperity": serializer.data})

class SelfImprovementView(APIView):
    def get(self, request):
        obj = SubparagraphsSelfImprovement.objects.all()
        serializer = SubparagraphsSelfImprovementSerializer(obj, many=True)

        return Response({"SelfImprovement": serializer.data})

class BrightnessOfLifeView(APIView):
    def get(self, request):
        obj = SubparagraphsBrightnessOfLife.objects.all()
        serializer = SubparagraphsBrightnessOfLifeSerializer(obj, many=True)

        return Response({"BrightnessOfLife": serializer.data})

class SpiritualityView(APIView):
    def get(self, request): 
        obj = SubparagraphsSpirituality.objects.all()
        serializer = SubparagraphsSpiritualitySerializer(obj, many=True)

        return Response({"Spirituality": serializer.data})