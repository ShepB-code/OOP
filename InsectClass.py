import random
class Insect:

    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.flightDuration = 0
    
    def lengthOfFlight(self):
        self.flightDuration = random.randint(1, 10)
    
    def getFlightDuration(self):
        return self.flightDuration

    