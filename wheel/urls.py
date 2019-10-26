from django.urls import path
from .views import WheelView
app_name = "wheel"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('wheel/', WheelView.as_view()),
]