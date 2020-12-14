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

import sys

def mainMenu()->None:
    """
    Imprime el menu de opciones
    """
    inputs = None
    switch =True
    while switch:
        print("\nBienvenido")
        print("*******************************************")
        print("\n\tParte A")
        print("1- Mostrar informacion general")
        print("2- Top de las compañias segun taxis")
        print("3- Top de las compañias segun servicios")
        print("\n\tParte B")
        print("4- Taxistas mas valorados del dia")
        print("5- Taxistas mas valorados (Rango)")
        print("\n\tParte C")
        print("6- Dar Mejor Horario")
        print("\n0- Salir")
        print("*******************************************")
        inputs = input('Selección: ')
        if (len(inputs)>0):
            try:
                inputs = int(inputs)
                switch = False
            except:
                print('\nEntrada no valida')
    if inputs == 0:
        sys.exit(0)
    return inputs

def fileMenu(files:list)->int:
    """
    Imprime un menu con los archivos disponibles
    """
    inputs = None
    switch =True
    while switch:
        print("\nEscoja el archivo que desea cargar")
        print("*******************************************")
        i = 0
        for file in files:
            i += 1
            print(f'{i}. {file}')
        print('0. Salir')
        print("*******************************************")
        inputs = input('Selección: ')
        if (len(inputs)>0):
            try:
                inputs = int(inputs)
                inputs -= 1
                if (inputs != -1):
                    files[inputs]
                switch = False
            except:
                print('\nEntrada no valida')

    if (inputs == -1):
        sys.exit(0)
    return inputs
