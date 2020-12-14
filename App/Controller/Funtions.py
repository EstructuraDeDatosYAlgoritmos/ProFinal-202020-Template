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
from DISClib.Algorithms.Sorting import mergesort
from App.Model import Comparation


def parteA_taxis(DataBase, M):
    comp = DataBase.getCompanies()
    values = map.valueSet(comp)
    mergesort.mergesort(values, Comparation.compareTaxis)
    respuesta = {}
    i = 0
    while M>i:
        company = list.removeFirst(values)
        print(company.name, company.taxis)
        i+=1

def parteA_services(DataBase, N):
    comp = DataBase.getCompanies()
    values = map.valueSet(comp)
    mergesort.mergesort(values, Comparation.compareServices)
    respuesta = {}
    i = 0
    while N>i:
        company = list.removeFirst(values)
        print(company.name, company.services)
        i+=1