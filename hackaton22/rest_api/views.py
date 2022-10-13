from django.shortcuts import render
from rest_framework import viewsets
from .models import MotorSpeed
from .serializers import MotorSpeedSerializer
# Create your views here.

class MotorSpeedViewSet(viewsets.ModelViewSet):
    """
    API endpoint that return motorspeed in Hz.
    """
    queryset = MotorSpeed.objects.filter(pk=1)
    serializer_class = MotorSpeedSerializer