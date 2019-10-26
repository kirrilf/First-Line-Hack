from django.urls import path
from .views import *
app_name = "wheel"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('wheel/', WheelView.as_view()),

    path('wheel/health/<int:pk>',HealthDone.as_view()), 
    path('wheel/health/delete/<int:pk>',HealthDelete.as_view()), 
    path('wheel/health/',HealthView.as_view()), 

    path('wheel/relationships/<int:pk>',RelationshipsDone.as_view()),
    path('wheel/relationships/delete/<int:pk>',RelationshipsDelete.as_view()),
    path('wheel/relationships/',RelationshipsView.as_view()),

    path('wheel/environment/<int:pk>',EnvironmentDone.as_view()),
    path('wheel/environment/delete/<int:pk>',EnvironmentDelete.as_view()),   
    path('wheel/environment/',EnvironmentView.as_view()), 

    path('wheel/vocation/<int:pk>',VocationDone.as_view()), 
    path('wheel/vocation/delete/<int:pk>',VocationDelete.as_view()), 
    path('wheel/vocation/',VocationView.as_view()), 

    path('wheel/prosperity/<int:pk>',ProsperityDone.as_view()), 
    path('wheel/prosperity/delete/<int:pk>',ProsperityDelete.as_view()), 
    path('wheel/prosperity/',ProsperityView.as_view()), 

    path('wheel/selfImprovement/<int:pk>',SelfImprovementDone.as_view()), 
    path('wheel/selfImprovement/delete/<int:pk>',SelfImprovementDelete.as_view()), 
    path('wheel/selfImprovement/',SelfImprovementView.as_view()), 

    path('wheel/brightnessOfLife/<int:pk>',BrightnessOfLifeDone.as_view()), 
    path('wheel/brightnessOfLife/delete/<int:pk>',BrightnessOfLifeDelete.as_view()), 
    path('wheel/brightnessOfLife/',BrightnessOfLifeView.as_view()), 

    path('wheel/spirituality/<int:pk>',SpiritualityDone.as_view()), 
    path('wheel/spirituality/delete/<int:pk>',SpiritualityDelete.as_view()), 
    path('wheel/spirituality/',SpiritualityView.as_view()), 
]