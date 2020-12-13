
from DISClib.ADT import map
from DISClib.DataStructures import mapentry 

from App.Model import Comparation as cmp
from App.Model.Api.Concept import Taxi


class DataTaxi:
    def __init__(self):
        self.total = 0,
        self.taxis = map.newMap(54135,comparefunction=cmp.compareId)

    def containsTaxi(self,id)->bool:
        return map.contains(self.taxis, id)

    def getTaxi(self,id:str)->Taxi:
        taxis = self.taxis
        if not self.containsTaxi(id):
            taxi = Taxi(id)
            map.put(taxis,id,taxi)
            self.total += 1
        taxi = map.get(taxis,id)
        taxi = mapentry.getValue(taxi) 
        return taxi
    
    def updateTaxi(self,service:dict):
        taxi = self.getTaxi(service)