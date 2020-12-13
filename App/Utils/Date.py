import datetime

def getDate(timestamp:str):
    dt = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f')
    return dt.date()

def getTime(timestamp:str):
    dt = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f')
    return dt.time()

