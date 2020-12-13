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

def targetVal(element1, element2):
    if element1['weight'] > element2['weight']:
        return True
    return False
