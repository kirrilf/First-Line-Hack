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
        obj = ToDoHealth.objects.all()
        serializer = ToDoHealthSerializer(obj, many=True)

        return Response({"Health": serializer.data})
    
  
class RelationshipsView(APIView):
    def get(self, request):
        obj = ToDoRelationships.objects.all()
        serializer = ToDoRelationshipsSerializer(obj, many=True)
                
        return Response({"Relationships": serializer.data})

class EnvironmentView(APIView):
    def get(self, request):

        obj = ToDoEnvironment.objects.all()
        serializer = ToDoEnvironmentSerializer(obj, many=True)

        return Response({"Environment": serializer.data})


class VocationView(APIView):
    def get(self, request):
        obj = ToDoVocation.objects.all()
        serializer = ToDoVocationSerializer(obj, many=True)

        return Response({"Vocation": serializer.data})

class ProsperityView(APIView):
    def get(self, request):
        obj = ToDoProsperity.objects.all()
        serializer = ToDoProsperitySerializer(obj, many=True)

        return Response({"Prosperity": serializer.data})

class SelfImprovementView(APIView):
    def get(self, request):
        obj = ToDoSelfImprovement.objects.all()
        serializer = ToDoSelfImprovementSerializer(obj, many=True)

        return Response({"SelfImprovement": serializer.data})

class BrightnessOfLifeView(APIView):
    def get(self, request):
        obj = ToDoBrightnessOfLife.objects.all()
        serializer = ToDoBrightnessOfLifeSerializer(obj, many=True)

        return Response({"BrightnessOfLife": serializer.data})

class SpiritualityView(APIView):
    def get(self, request): 
        obj = ToDoSpirituality.objects.all()
        serializer = ToDoSpiritualitySerializer(obj, many=True)

        return Response({"Spirituality": serializer.data})