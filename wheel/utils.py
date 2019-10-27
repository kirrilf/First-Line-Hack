import time
from .models import *

def cheackTimeHealth(obj):
    for toDo in obj:
        if toDo.timeEnd <=time.time():
            obi = Wheel.objects.get(id=1)
            obi.health = obj.health-1
            obi.save()
