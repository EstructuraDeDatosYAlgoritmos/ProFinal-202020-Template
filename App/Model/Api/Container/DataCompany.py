from DISClib.ADT import map
from DISClib.DataStructures import mapentry 

from App.Model import Comparation as cmp
from App.Model.Api.Concept.Company import Company


class DataCompany:
    def __init__(self):
        self.total = 0
        self.companies = map.newMap(54135,comparefunction=cmp.compareId)

    def containsCompany(self,name:str)->bool:
        return map.contains(self.companies,name)

    def getCompany(self,name)->Company:
        companies = self.companies
        if self.containsCompany(name):
            company = map.get(companies,name)
            company = mapentry.getValue(company)
        else:
            company = Company(name)
            map.put(companies,name,company)
            self.total += 1
        
        return company

    def getTotal(self)->int:
        return self.total

    def getCompanies(self)->dict:
        return self.companies
        