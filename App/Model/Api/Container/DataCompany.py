from DISClib.ADT import map
from DISClib.DataStructures import mapentry 

from App.Model import Comparation as cmp
from App.Model.Api.Concept import Company

class DataCompany:
    def __init__(self):
        self.total = 0
        self.companies = map.newMap(54135,comparefunction=cmp.compareId)

    def containsCompany(self,name:str)->bool:
        return map.contains(self.companies,name)

    def getCompany(self,name):
        companies = self.companies
        if not self.containsCompany(name):
            company = Company(name)
            map.put(companies,name,company)
            self.companies['total'] += 1
        company = map.get(companies,name)
        company = mapentry.getValue(company)
        return company

    def updateCompany(self,service:dict):
        company = self.getCompany(service)    
        company.addService()
        