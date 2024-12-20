import os

from core.middleware.exceptionMiddleware.exceptionMiddleware import exceptionMiddleware



class DataService:
    @exceptionMiddleware
    def getFileList(directory:str):
            directory = directory[6:]
            print(r"C:\ProjectFilesNKU" + directory)
            return os.listdir(r"C:\ProjectFilesNKU" + directory)

