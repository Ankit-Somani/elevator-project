from django.urls import path

from . import views

urlpatterns = [
    path("", views.ElevatorViewSet.as_view({'get': 'list'}), name="listAll"),  # to list all the elevators in the system
    path("init", views.ElevatorViewSet.as_view({'post': 'create'}), ),   # to create a new system of 'n' elevators
    path("<int:pk>", views.ElevatorViewSet.as_view({'get': 'retrieve'})), # to get detail of pk'th elevator 
    path("update", views.ElevatorViewSet.as_view({'patch': 'partial_update'})), # to handle any request for 'pk' elevator
]