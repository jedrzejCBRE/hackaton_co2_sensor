from rest_framework import serializers
from .models import MotorSpeed


class MotorSpeedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MotorSpeed
        fields = ['hz_speed']