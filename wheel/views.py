from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
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
    

    def post(self, request):
        health = request.data.get('health')
        # Create an article from the above data
        serializer = ToDoHealthSerializer(data=health)

        if serializer.is_valid(raise_exception=True):
            health_saved = serializer.save()
        return Response({"success": "health '{}' created successfully".format(health_saved.id)})

class HealthViewDelete(APIView):

    def delete(self, request, pk):
    # Get object with this pk
        health = get_object_or_404(ToDoHealth.objects.all(), pk=pk)
        health.delete()
        return Response({"message": "healthе with id `{}` has been deleted.".format(pk)}, status=204)
  
class RelationshipsView(APIView):
    def get(self, request):
        obj = ToDoRelationships.objects.all()
        serializer = ToDoRelationshipsSerializer(obj, many=True)
                
        return Response({"Relationships": serializer.data})

    def post(self, request):
        relationships = request.data.get('relationships')
        # Create an article from the above data
        serializer = ToDoRelationshipsSerializer(data=relationships)

        if serializer.is_valid(raise_exception=True):
            relationships_saved = serializer.save()
        return Response({"success": "relationships '{}' created successfully".format(relationships_saved.id)})

class RelationshipsViewDelete(APIView):
    
    def delete(self, request, pk):
    # Get object with this pk
        relationships = get_object_or_404(ToDoRelationships.objects.all(), pk=pk)
        relationships.delete()
        return Response({"message": "relationships with id `{}` has been deleted.".format(pk)}, status=204)


class EnvironmentView(APIView):
    def get(self, request):

        obj = ToDoEnvironment.objects.all()
        serializer = ToDoEnvironmentSerializer(obj, many=True)

        return Response({"Environment": serializer.data})

    def post(self, request):
        environment = request.data.get('environment')
        # Create an article from the above data
        serializer = ToDoEnvironmentSerializer(data=environment)

        if serializer.is_valid(raise_exception=True):
            environment_saved = serializer.save()
        return Response({"success": "environment '{}' created successfully".format(environment_saved.id)})

class EnvironmentViewDelete(APIView):
    
    def delete(self, request, pk):
    # Get object with this pk
        environment = get_object_or_404(ToDoEnvironment.objects.all(), pk=pk)
        environment.delete()
        return Response({"message": "environment with id `{}` has been deleted.".format(pk)}, status=204)


class VocationView(APIView):
    def get(self, request):
        obj = ToDoVocation.objects.all()
        serializer = ToDoVocationSerializer(obj, many=True)

        return Response({"Vocation": serializer.data})

    def post(self, request):
        vocation = request.data.get('vocation')
        # Create an article from the above data
        serializer = ToDoVocationSerializer(data=vocation)

        if serializer.is_valid(raise_exception=True):
            vocation_saved = serializer.save()
        return Response({"success": "vocation '{}' created successfully".format(vocation_saved.id)})

class VocationViewDelete(APIView):
    
    def delete(self, request, pk):
    # Get object with this pk
        vocation = get_object_or_404(ToDoVocation.objects.all(), pk=pk)
        vocation.delete()
        return Response({"message": "vocation with id `{}` has been deleted.".format(pk)}, status=204)




class ProsperityView(APIView):
    def get(self, request):
        obj = ToDoProsperity.objects.all()
        serializer = ToDoProsperitySerializer(obj, many=True)

        return Response({"Prosperity": serializer.data})

    def post(self, request):
        prosperity = request.data.get('prosperity')
        # Create an article from the above data
        serializer = ToDoProsperitySerializer(data=prosperity)

        if serializer.is_valid(raise_exception=True):
            prosperity_saved = serializer.save()
        return Response({"success": "rosperity '{}' created successfully".format(prosperity_saved.id)})

class ProsperityViewDelete(APIView):
    
    def delete(self, request, pk):
    # Get object with this pk
        prosperity = get_object_or_404(ToDoProsperity.objects.all(), pk=pk)
        prosperity.delete()
        return Response({"message": "prosperity with id `{}` has been deleted.".format(pk)}, status=204)



class SelfImprovementView(APIView):
    def get(self, request):
        obj = ToDoSelfImprovement.objects.all()
        serializer = ToDoSelfImprovementSerializer(obj, many=True)

        return Response({"SelfImprovement": serializer.data})

    def post(self, request):
        selfImprovement = request.data.get('selfImprovement')
        # Create an article from the above data
        serializer = ToDoSelfImprovementSerializer(data=selfImprovement)

        if serializer.is_valid(raise_exception=True):
            selfImprovement_saved = serializer.save()
        return Response({"success": "selfImprovement '{}' created successfully".format(selfImprovement_saved.id)})

class SelfImprovementViewDelete(APIView):
    
    def delete(self, request, pk):
    # Get object with this pk
        selfImprovement= get_object_or_404(ToDoSelfImprovement.objects.all(), pk=pk)
        selfImprovement.delete()
        return Response({"message": "selfImprovement with id `{}` has been deleted.".format(pk)}, status=204)




class BrightnessOfLifeView(APIView):
    def get(self, request):
        obj = ToDoBrightnessOfLife.objects.all()
        serializer = ToDoBrightnessOfLifeSerializer(obj, many=True)

        return Response({"BrightnessOfLife": serializer.data})

    def post(self, request):
        brightnessOfLife = request.data.get('brightnessOfLife')
        # Create an article from the above data
        serializer = ToDoBrightnessOfLifeSerializer(data=brightnessOfLife)

        if serializer.is_valid(raise_exception=True):
            brightnessOfLife_saved = serializer.save()
        return Response({"success": "brightnessOfLife '{}' created successfully".format(brightnessOfLife_saved.id)})

class BrightnessOfLifeViewDelete(APIView):
    
    def delete(self, request, pk):
    # Get object with this pk
        brightnessOfLife = get_object_or_404(ToDoBrightnessOfLife.objects.all(), pk=pk)
        brightnessOfLife.delete()
        return Response({"message": "brightnessOfLife with id `{}` has been deleted.".format(pk)}, status=204)



class SpiritualityView(APIView):
    def get(self, request): 
        obj = ToDoSpirituality.objects.all()
        serializer = ToDoSpiritualitySerializer(obj, many=True)

        return Response({"Spirituality": serializer.data})

    def post(self, request):
        spirituality = request.data.get('spirituality')
        # Create an article from the above data
        serializer = ToDoSpiritualitySerializer(data=spirituality)

        if serializer.is_valid(raise_exception=True):
            spirituality_saved = serializer.save()
        return Response({"success": "Health '{}' created successfully".format(spirituality_saved.id)})

class SpiritualityViewDelete(APIView):
    
    def delete(self, request, pk):
    # Get object with this pk
        spirituality = get_object_or_404(ToDoSpirituality.objects.all(), pk=pk)
        spirituality.delete()
        return Response({"message": "Spirituality with id `{}` has been deleted.".format(pk)}, status=204)
