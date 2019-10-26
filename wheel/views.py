from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Wheel
from .serializers import WheelSerializer

class WheelView(APIView):

    def get(self, request):
        wheel = Wheel.objects.all()

        serializer = WheelSerializer(wheel, many=True)
        return Response({"wheel": serializer.data})