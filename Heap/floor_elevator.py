class Floor:

    def __init__(self, FloorNumber, NoOfPassengers):
        self.Passengers = NoOfPassengers
        self.FloorNumber = FloorNumber

    def check(self):
        print("Floor ", self.FloorNumber, "P ", self.Passengers)


class Elevator:

    def __init__(self, GivenFloor, Enum):
        self.CurrentFloor = GivenFloor
        self.destined = 0
        self.Capacity = 0
        self.Steps = 0
        self.differ = 0
        self.Enum = Enum

    def check(self):
        print("Identifier",self.Enum, "     CFloor ", self .CurrentFloor, "     DFloor ", self.destined, "      Cap ",self.Capacity)

    def boarder(self, Floor):
        while self.Capacity < 20 and Floor.Passengers != 0:
            self.Capacity += 1
            Floor.Passengers -= 1
        self.destined = Floor.FloorNumber

    def differential(self, Floor):
        diff = abs(self.CurrentFloor - Floor.FloorNumber)
        return diff