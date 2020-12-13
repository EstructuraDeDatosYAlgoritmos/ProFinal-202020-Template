from DISClib.ADT import map
from DISClib.DataStructures import mapentry

from App.Model import Comparation as cmp
from App.Model.Api.Concept.Wallet import Wallet

class Day:
    def __init__(self):
        self.points = map.newMap(comparefunction=cmp.compareId)
    
    def containsWallet(self,id:str)->bool:
        return map.contains(self.points,id)

    def getWallet(self,id:str)->Wallet:
        if self.containsWallet(id):
            wallet = map.get(self.points,id)
            wallet = mapentry.getValue(wallet)
        else:
            wallet = Wallet(id)
            map.put(self.points,id,wallet)
        return wallet

    def getPoints(self):
        return self.points

        

    