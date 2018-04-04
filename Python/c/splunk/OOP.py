"""
1. airplane
2. car
3. BMW
4. truck
5. helicopter
6. boat
7. train

8. engine
9. brakes

10. stop()
11. fly()
12. drive()
"""


"""
vehicle
8. engine 
9. brakes    
12. move()   
10. stop()

automobile
12. drive()   

aircrafts
8. engine 
9. brakes    
12. fly()    
10. stop()


1. airplane
5. helicopter 
8. engine       
11. fly()    
10. stop()   

2. car                            
3. BMW                        
4. truck
8. engine     
10. stop()  
12. drive()       

6. boat 
8. engine     
10. stop()   
12. drive()      

7. train
8. engine     
10. stop()   
12. drive()      
"""

class Vehicle():
    def __init__(self, engine, breaks):
        self.engine = engine
        self.breaks = breaks

    def move(self):
        pass

    def stop(self):
        pass

class Aircrafts(Vehicle):
    def __init__(self, engine, breaks):
        Vehicle(engine, breaks)

    def move(self):
        self.fly()

    def fly(self):
        pass

class automobile(Vehicle):
    def __init__(self, engine, breaks):
        Vehicle(engine, breaks)

    def move(self):
        self.drive()


def find_flyable_vehicle(arr_vehicles):
    flyable_vehicles = []

    for vehicle in vehicles:
        if vehicle isinstance Aircrafts:
            flyable_vehicles.append(...)
