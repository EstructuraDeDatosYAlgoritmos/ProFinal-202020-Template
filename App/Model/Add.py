from App.Utils import Date
from App.Model.Api.DataBase.DataBase import DataBase


def addService(database:DataBase,service:dict)->None:
    updateCompany(database,service)
    updateTaxi(database,service)
    updatePoints(database,service)
    updateRoutes(database,service)

def updateCompany(database:DataBase,service:dict)->None:
    name = service['company']
    company = database.getCompany(name)
    company.addService()
    if not(database.taxis.containsTaxi(service['taxi_id'])):
        company.addTaxi()

def updateTaxi(database:DataBase,service:dict)->None:
    id = service['taxi_id']
    taxi = database.getTaxi(id)

def updatePoints(database:DataBase,service:dict):
    date = Date.getDate(service['trip_start_timestamp']) 
    id = service['taxi_id']
    miles = 0
    cash = 0
    if service['trip_miles'] != '':
        miles = float(service['trip_miles'])
    if service['trip_total'] != '':
        cash = float(service['trip_total'])
    wallet = database.getWallet(date,id)
    wallet.updateWallet(cash,miles)

def updateRoutes(database:DataBase,service):
    time = Date.getTime(service['trip_start_timestamp'])
    area1 = service['pickup_community_area']
    area2 = service['dropoff_community_area']
    seconds = 0
    if area1 != area2:
        if service['trip_seconds'] != '':
            seconds = float(service['trip_seconds'])
        trip = database.getTrip(area1,area2,time)
        trip.updateTrip(seconds)