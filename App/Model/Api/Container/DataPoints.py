from DISClib.ADT import orderedmap
from DISClib.DataStructures import mapentry 

from App.Model import Comparation as cmp
from App.Model.Api.Container.Day import Day

class DataPoints:
    def __init__(self):
        self.Days = orderedmap.newMap(comparefunction=cmp.compareDate)

    def containsDay(self,date)->bool:
        return orderedmap.contains(self.Days,date)

    def getDay(self,date)->Day:
        if self.containsDay(date):
            day = orderedmap.get(self.Days,date)
            day = mapentry.getValue(day)
        else:
            day = Day()
            orderedmap.put(self.Days,date,day)
        return day

    def getDays(self):
        return self.Days