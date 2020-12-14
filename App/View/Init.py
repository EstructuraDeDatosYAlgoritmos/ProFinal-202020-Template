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
from App.View import Menu
from App.Controller import LoadData
from App.Controller import Funtions
from App.Model.Api.DataBase.DataBase import DataBase


def ejecutarLoadData()->DataBase:
    files = LoadData.getFiles()
    inputs = Menu.fileMenu(files)
    print('\nIniciando Carga:')
    data = LoadData.loadData(files[inputs])
    return data

def ejecutarParteA_taxis(DataBase)->DataBase:    
    M = int(input('Ingrese el número de compañías que quisiera buscar ordenadas por la cantidad de taxis afiliados (de mayor a menor): '))
    print(Funtions.parteA_taxis(DataBase, M))
def ejecutarParteA_services(DataBase)->DataBase:    
    N = int(input('Ingrese el número de compañías que quisiera buscar ordenadas por la cantidad de servicios prestados (de mayor a menor): '))
    print(Funtions.parteA_services(DataBase, N))   

def ejecutar_mvpRango(DataBase)->DataBase:
    M = int(input('Ingrese el número de taxis con más puntos que desea conocer: '))
    fechai = input('Ingrese la fecha inicial deseada en forma YYYY-MM-DD: ')
    fechaf = input('Ingrese la fecha final deseada en forma YYYY-MM-DD: ')
    print(Funtions.mvpRango(DataBase, M, fechai, fechaf))
    
def ejecutarEstacionesCriticas(dataBase)->None:
    analysis = Funtions.estacionesCriticas(dataBase)
    topIn = listiterator.newIterator(analysis[0]) 
    topOut = listiterator.newIterator(analysis[1]) 
    bot = listiterator.newIterator(analysis[2])     

def ejecutarDarMejorHorario(database)->None:
    area1 = input('Ingrese la Primera Area: ')
    area2 = input('Ingrese la Segunda Area: ')
    time1 = input('Ingrese la Primera Hora (HH:MM): ')
    time2 = input('Ingrese la Segunda Hora (HH:MM): ')
    
    trip = Funtions.DarMejorHorario(database,area1,area2,time1,time2)
    print(f'\n\t{trip[1]} es la mejor hora de salida, con un tiempo promedio de {trip[0]}')