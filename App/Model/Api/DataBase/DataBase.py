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

from App.Model.Api.Container.DataCompany import DataCompany
from App.Model.Api.Container.DataPoints import DataPoints
from App.Model.Api.Container.DataTaxi import DataTaxi
from App.Model.Api.Concept.Company import Company
from App.Model.Api.Concept.Wallet import Wallet
from App.Model.Api.Concept.Taxi import Taxi

class DataBase:
    def __init__(self):
        self.companies = DataCompany()
        self.taxis = DataTaxi()
        self.points = DataPoints()
    
    def getCompany(self,name)->Company:
        return self.companies.getCompany(name)
    
    def getCompanies(self)->dict:
        return self.companies.getCompanies()

    def getTaxi(self,id)->Taxi:
        return self.taxis.getTaxi(id)

    def getTaxis(self)->dict:
        return self.taxis.getTaxis()

    def getWallet(self,date,id)->Wallet:
        return self.points.getDay(date).getWallet(id)
    
    def getPoints(self,date)->dict:
        return self.points.getDay(date).getPoints()
    
    def getDays(self,date)->dict:
        return self.points.getDays()
 
