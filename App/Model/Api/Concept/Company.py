class Company:
    def __init__(self,name):
        self.name = name
        self.taxis = 1
        self.services = 1
    def addTaxi(self):
        self.taxis +=1
    def addService(self):
        self.services += 1