from datetime import datetime

now = datetime.now()


def dateString():
    date = str(now.strftime("%-y%m%d"))
    return date


def timeString():
    time = now.strftime("%H%M%S%f")
    return time
