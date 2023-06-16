from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from app.serializers import ElevatorSerializer
from django.http import HttpResponse
from .models import Elevator


class ElevatorViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving Elevators.
    """
    def list(self, request):
        queryset = Elevator.objects.all()
        serializer = ElevatorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Elevator.objects.all()
        elevator = get_object_or_404(queryset, elevator_no=pk)
        serializer = ElevatorSerializer(elevator)
        return Response(serializer.data)
    
    def create(self, request):
        Elevator.objects.all().delete()
        n = request.data['elevators']
        f = request.data['floors']
        for i in range(n):
            e = Elevator(elevator_no = i+1, max_floor=f)
            e.save()
        return redirect('/app/')    #create new elevator system and redirect to elevator list page
    
    def partial_update(self, request):
        queryset = Elevator.objects.all()
        pk = request.data['pk']
        elevator = get_object_or_404(queryset, elevator_no=pk)
        if('door' in request.data): 
            door = request.data['door']
            elevator.toggle_door(door)
        if('operation' in request.data):
            operation = request.data['operation']
            elevator.toggle_operation(operation)
        if('dest_floor' in request.data):
            dest_floor = request.data['dest_floor']
            if(dest_floor<=elevator.max_floor):
                if(elevator.operational and elevator.door=="Closed"): elevator.change_floor(dest_floor)
                else: elevator.dest_waiting_list(dest_floor, dest_floor)
            else: return Response("Floor cannot be reached. Enter a valid floor.")
        serializer = ElevatorSerializer(elevator)
        return Response(serializer.data)
