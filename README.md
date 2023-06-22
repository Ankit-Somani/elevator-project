# Elevator Project #
The main project resides in project/ directory.

## Instructions to run the app locally: ##
* Clone the repo, install the requirements and move to this directory
  * `git clone https://github.com/Ankit-Somani/elevator-project.git`
  * `cd elevator-project/` 
  * `pip install -r requirements.txt`
  * `cd project/` 
* Run the django app
  * `python manage.py runserver`
* Copy the url shown in the terminal and open it in a browser.
  * http://127.0.0.1:8000/app/init : Send a POST request with body as `{"elevators": n, "floors": m}` to initialise a system of `n` elevators and `m` max number of floor. (m,n should be any positive integer values)
  * http://127.0.0.1:8000/app/ : This endpoint shows the list of all elevators in the system with details of each of them.
  * http://127.0.0.1:8000/app/k: This endpoint gives detail of k'th elevator. (k should be an integer less than equal to n)
  * http://127.0.0.1:8000/app/update: Send a PATCH request with body as `{"pk": k, "door": 0/1, "operation": 0/1, "dest_floor": d}` to make requests to k'th elevator.  <i>  pk is only mandatory field, door(0: closed, 1: open), operation(0:not working/maintainence, 1:working), dest_floor(d<=m)] </i>
  
* About the fields of model Elevator:
  * elevator_no: Unique number for each elevator from 1 to n
  * operational: True->Working, False->Under Maintainence/Not working
  * door: Gives current door status of that elevator
  * curr_floor: Gives the value of current floor at which elevator is stopped
  * direction: Gives the last direction in which elevator was moving to reach curr_floor
  * dest_waiting: List which gives floors which are waiting for the elevator to come. This list increases when the lift is not operational or door is not closed and requests are made to call elevator at these floors. Once lift is operational & door is closed, waiting list is cleared.
  * dest_list: List which gives all the floors from which requests are made to the elevator
  * max_floor: Maximum floor allowed in the system
  
  
  
