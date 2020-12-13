
from DISClib.ADT import map
from DISClib.DataStructures import mapentry 

from App.Model import Comparation as cmp
from App.Model.Api.Concept.Taxi import Taxi


class DataTaxi:
    def __init__(self):
        self.total = 0
        self.taxis = map.newMap(54135,comparefunction=cmp.compareId)

    def containsTaxi(self,id)->bool:
        return map.contains(self.taxis, id)

    def getTaxi(self,id:str)->Taxi:
        taxis = self.taxis
        if self.containsTaxi(id):
            taxi = map.get(taxis,id)
            taxi = mapentry.getValue(taxi) 
        else:
            taxi = Taxi(id)
            map.put(taxis,id,taxi)
            self.total += 1
        
        return taxi

    def getTotal(self)->int:
        return self.total

    def getTaxis(self)->map:
        return self.taxis
    
