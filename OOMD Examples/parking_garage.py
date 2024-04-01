'''
Classes:
- ParkingGarage: spaces
- ParkingSpace: Type(Sedan, Truck, Bike), isEV, isPriority
- Car: Type(Sedan, Truck, Bike), isEV
'''

class Car:
    def __init__(self, car_type, isEV):
        self.car_type = car_type
        self.isEV = isEV

class ParkingSpace:
    def __init__(self, id, space_type, isEV=False, isPriority=False):
        self.id = id
        self.space_type = space_type
        self.isEV = isEV
        self.isPriority = isPriority
        # self.vehicle = None
        self.isEmpty = True
    
    def __str__(self):
        return f"ID: {self.id}, Type: {self.space_type}, isEV: {self.isEV}, isPriority: {self.isPriority}"

class ParkingGarage:
    def __init__(self, cap):
        self.cap = cap
        self.spaces = []
        self.ctr = 0
        self.occupied = 0
    
    def addSpace(self, space_type, isEV=False, isPriority=False):
        if self.ctr == self.cap:
            print("Garage has max spaces!")
            return
        self.ctr+=1
        space = ParkingSpace(self.ctr, space_type, isEV, isPriority)
        self.spaces.append(space)

    def displayStats(self):
        print("--------")
        print(f"Total Spaces: {len(self.spaces)}")
        print(f"Available Spaces: {len(self.spaces) - self.occupied}")
        print("--------")
    
    def displaySpacesInfo(self):
        for space in self.spaces:
            print(space)
    
    def parkCar(self, space_id):
        space = self.spaces[space_id]
        if not space.isEmpty:
            print("Space is Full")
            return
        
        space.isEmpty = False
        self.occupied += 1
    
    def removeCar(self, space_id):
        space = self.spaces[space_id]
        if space.isEmpty:
            print("Space is already empty")
            return
        
        space.isEmpty = True
        self.occupied -= 1
    

garage = ParkingGarage(5)
garage.addSpace("sedan")
garage.addSpace("tuck")
garage.addSpace("bike")
garage.addSpace("sedan", isEV=True, isPriority=True)
garage.addSpace("sedan", isEV=True, isPriority=True)