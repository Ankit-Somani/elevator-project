from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from app.serializers import ElevatorSerializer
from django.http import HttpResponse
from .models import Elevator

def index(request):
    return HttpResponse("Hello, world. You're at the elevator index.")

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
        elevator = get_object_or_404(queryset, lift_number=pk)
        serializer = ElevatorSerializer(elevator)
        return Response(serializer.data)
    
    def create(self, request):
        Elevator.objects.all().delete()
        pk = request.data['pk']
        for i in range(pk):
            e = Elevator(lift_number = i+1)
            e.save()
        return redirect('/app/')    #create new elevator system and redirect to elevator list page
    
    def partial_update(self, request):
        queryset = Elevator.objects.all()
        pk = request.data['pk']
        elevator = get_object_or_404(queryset, lift_number=pk)
        if('door' in request.data): 
            door = request.data['door']
            elevator.toggle_door(door)
        if('operation' in request.data):
            operation = request.data['operation']
            elevator.toggle_operation(operation)
        if('dest_floor' in request.data):
            dest_floor = request.data['dest_floor']
            if(elevator.is_operational): elevator.change_floor(dest_floor)
            else: elevator.dest_waiting_list(dest_floor)
        serializer = ElevatorSerializer(elevator)
        return Response(serializer.data)



def initialise(request, number_of_elevators):
    Elevator.objects.all().delete()
    for i in range(number_of_elevators):
        e = Elevator(lift_number = i+1)
        e.save()
    return HttpResponse("New system of %s elevators initialised." % number_of_elevators)

def show_all_elevators(request):
    elevator_list = Elevator.objects.all()
    return render(request, "app/elevators.html", {"elevator_list": elevator_list})

def open_or_close(request, elevator_no):
    e = Elevator.objects.get(lift_number=elevator_no)
    res = e.toggle_door()
    return HttpResponse(res)

def elevator_direction(request, elevator_no):
    e = Elevator.objects.get(lift_number=elevator_no)
    if(e.direction): return HttpResponse("Elevator %s is moving up!" % elevator_no)
    return HttpResponse("Elevator %s is moving down!" % elevator_no)

def elevator_call(request, elevator_no, dest_floor):
    e = Elevator.objects.get(lift_number=elevator_no)
    if(e.is_operational):
        if(e.is_open):
            x = e.dest_string_to_list()
            x.append(dest_floor)
            e.dest_list_to_string(x)
            return HttpResponse("Elevator %s called on floor %s, waiting for its door to close..."  %(elevator_no,dest_floor))
        else:
            res = e.change_floor(dest_floor)
            return HttpResponse(res)
    else:
        return HttpResponse("Elevator %s is not operational currently. Please choose any other elevator.")    
    
def elevator_waiting(request, elevator_no):
    e = Elevator.objects.get(lift_number=elevator_no)
    return HttpResponse("Elevator %s waiting list: %s" %(elevator_no, e.dest_list))
    
def elevator_operation(request, elevator_no):
    e = Elevator.objects.get(lift_number=elevator_no)
    res = e.toggle_operation()
    return HttpResponse(res)