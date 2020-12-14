import datetime

def getDate(timestamp:str):
    dt = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f')
    return dt.date()

def getTime(timestamp:str):
    dt = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f')
    return dt.time()

def newTime(time:str):
    dt = datetime.datetime.strptime(time,'%H:%M')
    return dt.time()

def newDate(date:str):
    dt = datetime.datetime.strptime(date, '%Y-%m-%d')
    return dt.date()

def secondsToTime(seconds:int)->datetime:
    h = (seconds // 60) // 60
    m = (seconds // 60) % 60
    s = seconds % 60

    time = f'{int(h)}:{int(m)}:{round(s)}'
    return time