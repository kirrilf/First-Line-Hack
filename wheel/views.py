from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Wheel
from .serializers import WheelSerializer

class WheelView(APIView):

    def get(self, request):
        wheel = Wheel.objects.all()

        serializer = WheelSerializer(wheel, many=True)
       
        return Response(serializer.data)
    
'''class SubparagraphsView(APIView):
     def get(self, request):
        wheel = Wheel.objects.filter()

        serializer = WheelSerializer(wheel, many=True)

        return Response({"wheel": serializer.data})
    
    if searchQuery:
            obj = self.model.objects.filter(Q(title__icontains=searchQuery) | Q(body__icontains=searchQuery))
        else:
            obj = self.model.objects.all()'''
        
