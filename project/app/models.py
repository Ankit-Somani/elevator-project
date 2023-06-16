from django.db import models
import json
# Create your models here.

class Elevator(models.Model):
    elevator_no = models.IntegerField()
    operational = models.BooleanField(default=True)
    door = models.CharField(default="Closed", max_length=10)
    curr_floor = models.IntegerField(default=0)
    direction = models.CharField(default="Up", max_length=10)  
    dest_waiting = models.CharField(default="[]", max_length=200)
    dest_list = models.CharField(default="[]", max_length=200)
    max_floor = models.IntegerField(default=0)

    def __str__(self):
        return ("Elevator %s" %self.elevator_no)
    
    def toggle_door(self, door):
        if(door): self.door = "Opened"
        else: self.door = "Closed"    
        self.save()
        if(self.operational and self.door == "Closed"): 
            all_list, wait_list = self.dest_string_to_list()
            if(len(wait_list)): self.curr_floor = wait_list[-1]
            self.dest_waiting = "[]"
            self.save()
        return 
        
    def toggle_operation(self, operation):
        self.operational = operation
        self.save()
        if(self.operational and self.door == "Closed"): 
            all_list, wait_list = self.dest_string_to_list()
            if(len(wait_list)): self.curr_floor = wait_list[-1]
            self.dest_waiting = "[]"
            self.save()
        return 
        
    def change_floor(self, dest_floor):
        if(dest_floor<self.curr_floor):
            self.direction = "Down"
            self.curr_floor = dest_floor
            self.save()
        else:
            self.direction = "Up"
            self.curr_floor = dest_floor
            self.save()
        p, q = self.dest_string_to_list()
        p.append(dest_floor)
        self.dest_list_to_string(p,q)
        
    
    def dest_string_to_list(self):
        p = json.loads(str(self.dest_list))
        q = json.loads(str(self.dest_waiting))
        return p, q
    
    def dest_list_to_string(self, x, y):
        self.dest_list = json.dumps(x)
        self.dest_waiting = json.dumps(y)
        self.save()
        return 

    def dest_waiting_list(self, x, y):
        all_dest, wait_dest = self.dest_string_to_list()
        all_dest.append(x)
        wait_dest.append(y)
        self.dest_list_to_string(all_dest, wait_dest)
        return