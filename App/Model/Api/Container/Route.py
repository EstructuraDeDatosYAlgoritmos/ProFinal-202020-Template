from App.Model.Api.Concept.Trip import Trip
from DISClib.ADT import orderedmap
from DISClib.DataStructures import mapentry 

from App.Model import Comparation as cmp
from App.Model.Api.Concept.Company import Company


class Route:
    def __init__(self):
        self.Route = orderedmap.newMap(comparefunction=cmp.compareDate)

    def containsTrip(self,time)->bool:
        return orderedmap.contains(self.Route,time)

    def getTrip(self,time)->Trip:
        if self.containsTrip(time):
            trip = orderedmap.get(self.Route,time)
            trip = mapentry.getValue(trip)
        else:
            trip = Trip(time)
            orderedmap.put(self.Route,time,trip)
        return trip

    def getRoute(self)->dict:
        return self.Route