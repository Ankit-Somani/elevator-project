from django.urls import path

from . import views

urlpatterns = [
    path("", views.ElevatorViewSet.as_view({'get': 'list'}), name="ellist"),
    path("init", views.ElevatorViewSet.as_view({'post': 'create'}), ),
    path("<int:pk>", views.ElevatorViewSet.as_view({'get': 'retrieve'})),
    path("update", views.ElevatorViewSet.as_view({'patch': 'partial_update'})),
    # path("create/<int:pk>", views.ElevatorViewSet.as_view({'get': 'create'})),
    path("init/<int:number_of_elevators>", views.initialise), #to initialize system of n elevators
    path("show", views.show_all_elevators), #to show all the elevators in current system
    path("toggle/<int:elevator_no>", views.open_or_close), #to open/close the door of any elevator
    path("direction/<int:elevator_no>", views.elevator_direction), #to get the direction of any elevator
    path("<int:elevator_no>/goto/<int:dest_floor>", views.elevator_call),
    path("waiting/<int:elevator_no>", views.elevator_waiting)
]