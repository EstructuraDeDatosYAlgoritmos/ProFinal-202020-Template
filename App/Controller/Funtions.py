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
from DISClib.ADT import list as lt

from App.Model.Comparation import wallet
from App.Utils import Date

from App.Model import Analysis

def mejorHorario(database,area1,area2,time1,time2):
    area1 = area1 + '.0'
    area2 = area2 + '.0'    
    time1 = Date.newTime(time1)
    time2 = Date.newTime(time2)
    trip = Analysis.getBestTime(database,area1,area2,time1,time2)
    return Date.secondsToTime(trip[0]),trip[1]

def mvpDia(database,date,n):
    date = Date.newDate(date)
    wallets = Analysis.getPoints(database,date)
    values = []
    while (n > len(values)) and (not lt.isEmpty(wallets)):
        wallet = lt.removeFirst(wallets)
        values.append((wallet.id,wallet.points))
    return values

def mvpRango(database,date1,date2,m):
    date1 = Date.newDate(date1)
    date2 = Date.newDate(date2)
    wallets = Analysis.getPointsV2(database,date1,date2)
    values = []
    while (m > len(values)) and (not lt.isEmpty(wallets)):
        wallet = lt.removeFirst(wallets)
        values.append((wallet['id'],wallet['points']))
    return values
