class LogList:
    logList =[]
    def addLog(self,data):
        self.logList.append(data)

def loggingMiddleware(func):
    def wrapper(*args, **kwargs):
        LogList().addLog(func(*args, **kwargs))
        return func(*args, **kwargs)
    return wrapper


