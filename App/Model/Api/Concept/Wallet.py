class Wallet:
    def __init__(self,id:str):
        self.id = id
        self.cash = 0
        self.miles = 0
        self.services = 0
        self.points = 0

    def getPoints(self)->float:
        return (self.miles/self.cash)*self.services

    def getId(self)->str:
        return self.id

    def updateWallet(self,cash:float, miles:float):
        if miles != 0 and cash != 0:
            self.cash += cash
            self.miles += miles
            self.services += 1
            self.points = self.getPoints()