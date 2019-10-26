from django.urls import path
from .views import *
app_name = "wheel"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('wheel/', WheelView.as_view()),
    path('wheel/health/',HealthView.as_view()), 
    path('wheel/relationships/',RelationshipsView.as_view()), 
    path('wheel/environment/',EnvironmentView.as_view()), 
    path('wheel/vocation/',VocationView.as_view()), 
    path('wheel/prosperity/',ProsperityView.as_view()), 
    path('wheel/selfImprovement/',SelfImprovementView.as_view()), 
    path('wheel/brightnessOfLife/',BrightnessOfLifeView.as_view()), 
    path('wheel/spirituality/',SpiritualityView.as_view()), 
]