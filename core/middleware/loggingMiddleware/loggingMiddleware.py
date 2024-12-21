import datetime


class LogList:
    logList =[]
    def addLog(self,data):
        self.logList.append(data)

def loggingMiddleware(func):
    def wrapper(*args, **kwargs):
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        LogList().addLog(func(*args, **kwargs)+"-->"+date)
        return func(*args, **kwargs)
    return wrapper


