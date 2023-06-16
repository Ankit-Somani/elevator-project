from rest_framework import serializers
from .models import Elevator

class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = ['lift_number', 'is_operational', 'is_selected', 'is_running', 'on_floor', 'direction', 'is_open', 'dest_list']