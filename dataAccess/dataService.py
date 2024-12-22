import os

from core.middleware.exceptionMiddleware.exceptionMiddleware import exceptionMiddleware



class DataService:
    def getFileList(directory:str):
        """
        Bu fonskyion, ilgili kalsördeki nesneleri liste olarak alır
        :param directory: Gitmek istenilen dizin.
        :return: İlgili dizindeki dosya isimleri.
        """
        print("C:\ProjectFilesNKU" + directory)
        return os.listdir("C:\ProjectFilesNKU" + directory)


    @exceptionMiddleware
    def createFolder(directoryParameter:str):
        """
        Bu fonksiyon, istenilen klasör altına yeni bir klasör yaratır.
        :param:directoryParameter: Nereye yeni klasör eklenileceği bilgisini verir
        :return: None: Herhangi bir veri dönülmez.
        """
        directory = directoryParameter[13:].replace("?filename=", "\\")
        folder_path = "C:\ProjectFilesNKU\\" + directory
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

