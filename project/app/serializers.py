from rest_framework import serializers
from .models import Elevator

class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = ['elevator_no', 'operational', 'door', 'curr_floor', 'direction', 'dest_waiting', 'dest_list', 'max_floor']