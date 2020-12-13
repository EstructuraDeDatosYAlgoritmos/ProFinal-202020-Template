class Trip:
    def __init__(self,time):
        self.time = time
        self.services = 0
        self.seconds = 0

    def updateTrip(self,seconds):
        total = self.seconds * self.services
        self.services += 1
        self.seconds = (total+seconds)/self.services 