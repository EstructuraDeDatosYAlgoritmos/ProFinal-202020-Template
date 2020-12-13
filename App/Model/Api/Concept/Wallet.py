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
        self.cash += cash
        self.miles += miles
        self.services += 1
        if self.miles != 0 and self.cash != 0:
            self.points = self.getPoints()