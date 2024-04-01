class Lift:
    def __init__(self, max_floors):
        self.lift_id = 1
        self.max_floors = max_floors
        self.current_floor = 1
        self.direction = 0
        self.requests = set()

    def move_to_floor(self, floor_num):
        if floor_num == self.current_floor:
            print(f"Lift {self.lift_id} is already on Floor {floor_num}.")
            return

        if floor_num > self.current_floor:
            self.direction = 1
            print(f"Lift {self.lift_id} is moving up from Floor {self.current_floor} to Floor {floor_num}.")
        else:
            self.direction = -1
            print(f"Lift {self.lift_id} is moving down from Floor {self.current_floor} to Floor {floor_num}.")

        self.current_floor = floor_num
        print(f"Lift {self.lift_id} now at Floor {self.current_floor}")
        
    
    def process_requests(self):
        if not self.requests:
            print("No Requests")
            return

        #### THIS LOGIC NEEDS TO BE CHANGED
        next_floor = min(self.requests) if self.direction == 1 else max(self.requests)
        if self.direction == 1 or self.direction == 0:
            above_floors = [floor for floor in self.requests if floor > self.current_floor]
            if above_floors:
                next_floor = min(above_floors)
        else:
            below_floors = [floor for floor in self.requests if floor < self.current_floor]
            if below_floors:
                next_floor = max(below_floors)

        self.move_to_floor(next_floor)
        self.requests.remove(next_floor)
        self.process_requests()

class Controller:
    def __init__(self, max_floors):
        self.max_floors = max_floors
        self.lift = Lift(max_floors)
    
    def handle_request(self, req_floor):
        self.lift.requests.add(req_floor)
        self.lift.process_requests()

ctrl = Controller(10)
ctrl.lift.requests.add(4)
ctrl.handle_request(2)