"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
"""
from DISClib.ADT import map 
from DISClib.ADT import list 
from DISClib.ADT import orderedmap
from DISClib.DataStructures import mapentry
from DISClib.DataStructures import listiterator as lti
from DISClib.Algorithms.Sorting import mergesort as sort

from App.Model import Comparation as cmp
from App.Model.Api.DataBase.DataBase import DataBase


def getPoints(database:DataBase,date)->dict:
    day = database.getPoints(date)
    day = map.valueSet(day)
    sort.mergesort(day,cmp.wallet)
    return day

def getPointsV2(database:DataBase,date1,date2)->dict:
    days = database.getDays()
    days = orderedmap.values(days,date1,date2)
    days = lti.newIterator(days)
    top = map.newMap(comparefunction=cmp.compareId)
    while lti.hasNext(days):
        day = lti.next(days).points
        day = map.valueSet(day)
        day = lti.newIterator(day)
        while lti.hasNext(day):
            wallet = lti.next(day)
            if map.contains(top,wallet.id):
                node = map.get(top,wallet.id)
                value = mapentry.getValue(node)
                value['points'] += wallet.points
            else:
                value = {
                    'id' : wallet.id,
                    'points': wallet.points
                    }
                
                map.put(top,wallet.id,value)

    top = map.valueSet(top)
    sort.mergesort(top,cmp.points)
    return top

def getBestTime(database:DataBase,area1:str,area2:str,time1,time2)->dict:
    route = database.getRoute(area1,area2).getRoute()
    route = orderedmap.values(route,time1,time2)
    sort.mergesort(route,cmp.trip)
    trip = list.removeFirst(route)
    return (trip.seconds,trip.time)