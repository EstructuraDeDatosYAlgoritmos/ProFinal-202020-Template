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
    print('\nCarga Iniciada\n')
    data = LoadData.loadData(files[inputs])
    return data

def ejecutarParteA_info(database)->None:
    taxis= database.taxis.getTotal()
    companies= database.companies.getTotal()
    print("\n\tEl total de taxis es: ",taxis) 
    print("\tEl total de compañias es de: ",companies)

def ejecutarParteA_taxis(database)->None:    
    M = int(input('Ingrese el número de compañías que quisiera buscar ordenadas por la cantidad de taxis afiliados (de mayor a menor): '))
    values = Funtions.parteA_taxis(database, M)
    i = 1
    for value in values:
        print(f'\n\t{i}. {value[0]}: \n\t   Puntos: {value[1]}')
        i += 1     

def ejecutarParteA_services(database)->None:    
    N = int(input('Ingrese el número de compañías que quisiera buscar ordenadas por la cantidad de servicios prestados (de mayor a menor): '))
    values = Funtions.parteA_services(database, N)
    i = 1
    for value in values:
        print(f'\n\t{i}. {value[0]}: \n\t   Puntos: {value[1]}')
        i += 1      


def ejecutarMvpDia(database):
    date = input('Ingrese la Fecha (YYYY-MM-DD): ')
    n = int(input('Ingrese el numero de puestos: '))

    wallets = Funtions.mvpDia(database,date,n)
    i = 1
    for wallet in wallets:
        print(f'\n\t{i}. Puntos: {wallet[1]}: \n\t   {wallet[0]}')
        i += 1

def ejecutarMvpRango(database):
    date1 = input('Ingrese la Fecha Inicial (YYYY-MM-DD): ')
    date2 = input('Ingrese la Fecha Final (YYYY-MM-DD): ')
    m = int(input('Ingrese el numero de puestos: '))

    wallets = Funtions.mvpRango(database,date1,date2,m)
    i = 1
    for wallet in wallets:
        print(f'\n\t{i}. Puntos: {wallet[1]}: \n\t   {wallet[0]}')
        i += 1

def ejecutarMejorHorario(database)->None:
    area1 = input('Ingrese la Primera Area: ')
    area2 = input('Ingrese la Segunda Area: ')
    time1 = input('Ingrese la Primera Hora (HH:MM): ')
    time2 = input('Ingrese la Segunda Hora (HH:MM): ')
    
    trip = Funtions.mejorHorario(database,area1,area2,time1,time2)
    print(f'\n\tMejor hora de salida: {trip[1]} \n\tTiempo promedio: {trip[0]}')