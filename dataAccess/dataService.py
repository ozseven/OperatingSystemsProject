import os

from core.middleware.exceptionMiddleware.exceptionMiddleware import exceptionMiddleware



class DataService:
    @exceptionMiddleware
    def getFileList(directory:str):
            directory = directory[6:]
            print("C:\ProjectFilesNKU" + directory)
            return os.listdir("C:\ProjectFilesNKU" + directory)

