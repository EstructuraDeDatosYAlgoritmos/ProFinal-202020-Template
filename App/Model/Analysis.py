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

from App.Model.Api.DataBase.DataBase import DataBase


from DISClib.ADT import graph
from DISClib.ADT import map 
from DISClib.ADT import list 
from DISClib.ADT import stack
from DISClib.ADT import queue
from DISClib.ADT import orderedmap
from DISClib.DataStructures import listiterator 
from DISClib.DataStructures import edge 
from DISClib.DataStructures import mapentry
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Sorting import mergesort as sort

from App.Model import Comparation as cmp

def getBestTime(database:DataBase,area1:str,area2:str,time1,time2)->dict:
    route = database.getRoute(area1,area2).getRoute()
    route = orderedmap.values(route,time1,time2)
    sort.mergesort(route,cmp.trip)
    trip = list.removeFirst(route)
    return (trip.seconds,trip.time)