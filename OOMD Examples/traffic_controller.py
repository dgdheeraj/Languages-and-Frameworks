class TrafficLight:
    def __init__(self, id):
        self.id = id
        self.state = "red"
    
    def changeState(self):
        old_state = self.state
        if self.state == "red":
            self.state = "green"
        elif self.state == "yellow":
            self.state = "red"
        else:
            self.state = "yellow"

        print(f"Signal {self.id} changed from {old_state} to {self.state}")

class Controller:
    def __init__(self):
        self.up = TrafficLight("up")
        self.down = TrafficLight("down")
        self.right = TrafficLight("right")
        self.left = TrafficLight("left")

    def rotateStates(self, signal):
        while True:
            signal.changeState()
            if signal.state == "red":
                break

    def circulate_traffic(self):
        self.rotateStates(self.up)
        self.rotateStates(self.down)
        print("CrossWalk for Pedestrians!!!")
        self.rotateStates(self.right)
        self.rotateStates(self.left)
    
ctrl = Controller()
ctrl.circulate_traffic()