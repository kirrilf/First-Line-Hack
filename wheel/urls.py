from django.urls import path
from .views import *
app_name = "wheel"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('wheel/', WheelView.as_view()),
    path('wheel/health/<int:pk>',HealthViewDelete.as_view()), 
    path('wheel/health/',HealthView.as_view()), 

    path('wheel/relationships/<int:pk>',RelationshipsViewDelete.as_view()), 
    path('wheel/relationships/',RelationshipsView.as_view()),

    path('wheel/environment/<int:pk>',EnvironmentViewDelete.as_view()),  
    path('wheel/environment/',EnvironmentView.as_view()), 

    path('wheel/vocation/<int:pk>',VocationViewDelete.as_view()), 
    path('wheel/vocation/',VocationView.as_view()), 

    path('wheel/prosperity/<int:pk>',ProsperityViewDelete.as_view()), 
    path('wheel/prosperity/',ProsperityView.as_view()), 

    path('wheel/selfImprovement/<int:pk>',SelfImprovementViewDelete.as_view()), 
    path('wheel/selfImprovement/',SelfImprovementView.as_view()), 

    path('wheel/brightnessOfLife/<int:pk>',BrightnessOfLifeViewDelete.as_view()), 
    path('wheel/brightnessOfLife/',BrightnessOfLifeView.as_view()), 

    path('wheel/spirituality/<int:pk>',SpiritualityViewDelete.as_view()), 
    path('wheel/spirituality/',SpiritualityView.as_view()), 
]