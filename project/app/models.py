from django.db import models
import json
# Create your models here.

class Elevator(models.Model):
    lift_number = models.IntegerField(default=0)
    is_operational = models.BooleanField(default=True)
    is_selected = models.BooleanField(default=False)
    is_running = models.BooleanField(default=False)
    on_floor = models.IntegerField(default=0)
    direction = models.BooleanField(default=True)   #true means up and false means down
    is_open = models.BooleanField(default=False)
    dest_list = models.CharField(default="[]", max_length=200)

    def __str__(self):
        return ("Elevator %s" %self.lift_number)
    
    def toggle_door(self, door):
        self.is_open = door
        self.save()
        return 
        # if(self.is_open): 
        #     self.is_open = False
        #     x = self.dest_string_to_list()
        #     s = ""
        #     if(len(x)):
        #         s = self.change_floor(x[len(x)-1])
        #         self.dest_list = "[]"
        #     self.save()
        #     return("Closed door for elevator %s." %self.lift_number) + s    
        # else: 
        #     self.is_open = True
        #     self.save()
        #     return("Opened door for elevator %s" %self.lift_number)
        
    def toggle_operation(self, operation):
        self.is_operational = operation
        self.save()
        return 
        # if(self.is_operational): 
        #     self.is_operational = False
        #     self.save()
        #     return("Elevator %s set to not operational." %self.lift_number)    
        # else: 
        #     self.is_operational = True
        #     self.save()
        #     return("Elevator %s set to operational." %self.lift_number)
        
    def change_floor(self, dest_floor):
        if(dest_floor<self.on_floor):
            self.direction = False
            self.on_floor = dest_floor
            self.save()
            # return ("Elevator %s moved down to floor %s."  %(self.lift_number,dest_floor))
        else:
            self.direction = True
            self.on_floor = dest_floor
            self.save()
            # return ("Elevator %s moved up to floor %s."  %(self.lift_number,dest_floor))
        
    
    def dest_string_to_list(self):
        # print(self.dest_list)
        p = json.loads(str(self.dest_list))
        return p
    
    def dest_list_to_string(self, x):
        self.dest_list = json.dumps(x)
        self.save()
        return 

    def dest_waiting_list(self, x):
        p = self.dest_string_to_list()
        p.append(x)
        self.dest_list_to_string(p)
        return