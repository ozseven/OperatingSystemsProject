import os
from datetime import datetime

from core.middleware.exceptionMiddleware.exceptionMiddleware import exceptionMiddleware
from core.utils.slugParser import slugParser


@exceptionMiddleware
def save_file_from_bytes(request: bytes):
    """
    Bu fonksiyon byte tipinde gelen nesneleri dosya ismi, kaydedilmek istenilen dizin ve dosya olarak ayrıştırır ve istenilen klasöre kaydeder.
    :param request: Byte tipinde nesneler kabul edilir
    :return: None Bu fonksiyon herhangi bir dönüş değeri bulundurmaz.
    """
    slug =slugParser(request[:150].decode('utf-8'))
    fileNameIndex = request.find(b"filename")
    fileName , content =request[fileNameIndex+21:].split(b'"\r\n',1)
    _, fileContent= content.split(b'\r\n\r\n',1)
    print(f"C:\\ProjectFilesNKU{slug[6:]}{fileName.decode()}")  # Ters eğik çizgiler çiftlendi
    with open(f"C:\\ProjectFilesNKU{slug[6:]}\\{fileName.decode()}", "wb") as file:  # Ters eğik çizgiler çiftlendi
        file.write(fileContent)

