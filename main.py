import numpy as np

class Elevator:

    def __init__(self, lift_number, floor_min, floor_max, on_floor = 0):
        self.lift_number = lift_number
        self.is_operational = True
        self.floor_max = floor_max
        self.floor_min = floor_min
        self.is_selected = False
        self.is_running = False
        self.on_floor = on_floor
        self.direction = 1
        self.is_overload = False
        self.service_list = []

    def current_status(self):
        print("lift {} is currently @ floor {}".format(self.lift_number, self.on_floor))
        print("lift {} running status {} ".format(self.lift_number, self.is_running))

    def open_door(self):
        print("lift {} door opening".format(self.lift_number))
        self.door_open = True

    # close door
    def close_door(self):
        print("lift {} door closing".format(self.lift_number))
        self.door_open = False

    def calculate_service_in_directions(self):
        """
        Creates 2 list from a single service list
        service_in_up_direction - contains all the floor number which are above
        service_in_down_direction - all floor which are below
        """
        self.service_list = np.sort(self.service_list)
        service_in_up_direction = list(self.service_list[self.service_list > self.on_floor])
        service_in_down_direction = list(self.service_list[self.service_list < self.on_floor])
        service_in_down_direction = service_in_down_direction[::-1]
        return service_in_up_direction, service_in_down_direction

    def process_request(self):
        """
        recieves service_list and process them.
        Broabdly 2 tasks:

        TASK 1
        # case when button is pressed from outside
        # go to the requested floor

        TASK 2
        # process request when button from inside are pressed.
        """

        # go to requested floor
        print("Need To Process => ", self.service_list)
        if self.service_list[0] != self.on_floor:
            self.current_status()
            self.execute_request(self.service_list[0:1])
        else:
            self.current_status()
            self.open_door()
            self.close_door()

        # then user presses the buttons
        # lift decides automatically
        self.service_list = self.service_list[1:]
        service_in_up_direction, service_in_down_direction = self.calculate_service_in_directions()


        # nothing to service in up direction, go down
        if len(service_in_up_direction) == 0:
            self.direction = -1
        # nothing to service in down direction, go up
        elif len(service_in_down_direction) == 0:
            self.direction = 1
        # calculate cost and then decide direction
        # strategy could be improved
        # currently it just checks the first request for cost calculation
        else:
            # effort_up = distance between first up floor and current floor
            effort_up = abs(service_in_up_direction[0] - self.on_floor)
            # effort_down = distance between first down floor and current floor
            effort_down = abs(service_in_down_direction[0] - self.on_floor)

            # choose direction
            if effort_up <= effort_down:
                self.direction = 1
            else:
                self.direction = -1


        # execute once for up
        # once for down
        for turn in range(0,2):
            if self.direction == -1:
                self.execute_request(service_in_down_direction)

            else:
                self.execute_request(service_in_up_direction)

            # reverse the direction
            self.direction = - self.direction


        # set params to denote that it is available
        self.reset_lift_params()

    def reset_lift_params(self):
        # when request finishes reset the direction
        self.direction = 1
        self.is_running = False
        self.is_selected = False
        self.service_list = []


active_floors = 5

    # default position of lifts, as of now we have got 5 lifts in place
lift_positions = 9

# no_of_lifts, floor_min, floor_max = initialize_system()
no_of_lifts, floor_min, floor_max = 5, -4, 20

# request for each elevator
request_each = [[-3,12, 8, 6 ,4 ,0, 5],
                [-3,0, 5],
                [4,0, 5],
                [8, 6 ,4 ,0, 5],
                [2,4,8,10,12]]

new_elevator = Elevator(1, floor_min, floor_max, 0)

new_elevator.current_status()
new_elevator.open_door()
print(new_elevator.door_open)

