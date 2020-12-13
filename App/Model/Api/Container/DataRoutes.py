from App.Model.Api.Container.Route import Route
from DISClib.ADT import graph
from DISClib.DataStructures import mapentry 

from App.Model import Comparation as cmp
from App.Model.Api.Container.Day import Day

class DataRoutes:
    def __init__(self):
        self.Routes = graph.newGraph("ADJ_LIST",True,78,cmp.compareId)

    def containsArea(self,area)->bool:
        return graph.containsVertex(self.Routes,area)

    def getRoute(self,area1,area2)->Route:
        if not self.containsArea(area1):
            graph.insertVertex(self.Routes,area1)
        if not self.containsArea(area2):
            graph.insertVertex(self.Routes,area2)

        route = graph.getEdge(self.Routes,area1,area2)
        if route is None:
            route = Route()
            graph.addEdge(self.Routes,area1,area2,route)
            route = graph.getEdge(self.Routes,area1,area2)
        return route['weight']

    def getRoutes(self):
        return self.Routes
        
