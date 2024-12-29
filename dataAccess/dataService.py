import os

from core.middleware.exceptionMiddleware.exceptionMiddleware import exceptionMiddleware
from core.middleware.threadingMiddleware.threadLockMiddleware import threadLockMiddleware



class DataService:
    def getFileList(slug:str):
        """
        Bu fonskyion, ilgili kalsördeki nesneleri liste olarak alır
        :param directory: Gitmek istenilen dizin.
        :return: İlgili dizindeki dosya isimleri.
        """
        print(r"C:\ProjectFilesNKU" + slug)
        return os.listdir(r"C:\ProjectFilesNKU" + slug)

    @threadLockMiddleware
    def createFolder(directoryParameter:str):
        """
        Bu fonksiyon, istenilen klasör altına yeni bir klasör yaratır.
        :param:directoryParameter: Nereye yeni klasör eklenileceği bilgisini verir
        :return: None: Herhangi bir veri dönülmez.
        """
        directory = directoryParameter[13:].replace("?filename=", "\\")
        folder_path = r"C:\ProjectFilesNKU\\" + directory
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    @threadLockMiddleware
    def deleteFile(directory:str):
        os.remove(r"C:\ProjectFilesNKU\\" + directory)

    @threadLockMiddleware
    def downloadFile(slug:str):
        with open(rf"C:\ProjectFilesNKU{slug}", 'r+b') as f:
            return f.read()

    def saveFile(slug:str,fileName,fileContent):
        with open(f"C:\\ProjectFilesNKU{slug[6:]}\\{fileName.decode()}", "wb") as file:
            file.write(fileContent)
