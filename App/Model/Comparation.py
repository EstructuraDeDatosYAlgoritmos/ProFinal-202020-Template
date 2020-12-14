from App.Model.Api.Concept.Wallet import Wallet
from App.Model.Api.Concept.Trip import Trip
from DISClib.DataStructures import mapentry

def compareId(id1, id2):
    id2 = mapentry.getKey(id2)
    if (id1 == id2):
        return 0
    elif (id1 > id2):
        return 1
    else:
        return -1
        
def compareDate(id1, id2):
    id1 = id1
    id2 = id2
    if (id1 == id2):
        return 0
    elif (id1 > id2):
        return 1
    else:
        return -1

def trip(element1:Trip, element2:Trip):
    if element1.seconds > element2.seconds:
        return True
    return False

def compareTaxis(element1, element2):
    if element1.taxis > element2.taxis:
        return True
    return False

def compareServices(element1, element2):
    if element1.services > element2.services:
        return True
    return False

def wallet(element1:Wallet, element2:Wallet):
    if element1.points > element2.points:
        return True
    return False

def points(element1, element2):
    if element1['points'] > element2['points']:
        return True
    return False