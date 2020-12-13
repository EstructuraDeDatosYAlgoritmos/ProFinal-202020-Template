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
import csv
import os



from App.View import config
from App.Model import Add
from App.Model.Api.DataBase.DataBase import DataBase

def getFiles()->list:
    files = []
    for filename in os.listdir(config.data_dir):
        if filename.endswith('.csv'):
            files.append(filename)       
    return files

def loadData(filename)->bool:
    Data = DataBase()
    filename = config.data_dir+filename
    dialect = csv.excel()
    dialect.delimiter = ','
    
    with open(filename, encoding="utf-8") as csvfile:
        buffer = csv.DictReader(csvfile, dialect=dialect)
        cont = 0
        for element in buffer:
            cont += 1
            Add.addService(Data,element)
        print(f"\tLineas cargadas: {cont}")
    return Data

