import os

from core.middleware.exceptionMiddleware.exceptionMiddleware import exceptionMiddleware



class DataService:
    @exceptionMiddleware
    def getFileList(directory:str):
            directory = directory[6:]
            print("C:\ProjectFilesNKU" + directory)
            return os.listdir("C:\ProjectFilesNKU\\" + directory)
    @exceptionMiddleware
    def createFolder(directoryParameter:str):
        directory = directoryParameter[13:].replace("?filename=", "\\")
        folder_path = "C:\ProjectFilesNKU\\" + directory
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

