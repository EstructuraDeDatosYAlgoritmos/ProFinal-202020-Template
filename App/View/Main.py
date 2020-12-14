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
import config
import sys

from App.View import Init
from App.View import Menu
from DISClib.ADT import map
from DISClib.ADT import list

def main()->None:
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
        Args: None
        Return: None 
    """
    database = Init.ejecutarLoadData()
    

    while True:
        inputs = Menu.mainMenu() #imprimir el menu de opciones en consola
        if int(inputs) == 1:  #opcion 1 
            taxis= database.taxis.getTotal()
            companies= database.companies.getTotal()
            print("El total de taxis es de ", taxis, " y el total de compañias es de ",companies)
            Init.ejecutarParteA_taxis(database)
            Init.ejecutarParteA_services(database)
        if int(inputs) == 2:
            Init.ejecutar_mvpRango(database)
        if int(inputs) == 3:
            Init.ejecutarDarMejorHorario(database)

if __name__ == "__main__":
    main()