import socket
from urllib import parse

from core.middleware.exceptionMiddleware.exceptionMiddleware import exceptionMiddleware
from core.utils.slugParser import slugParser
from view.dataView import DataView as dataView


HOST = '127.0.0.1'
PORT = 8080
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Sunucu {HOST}:{PORT} üzerinde çalışıyor...")

while True:
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(2048).decode('utf-8')

    @exceptionMiddleware
    def getMethod():
        slug:str = slugParser(request)
        view = dataView(slug).getTemplate()
        return view

    if request.startswith("GET"):
        response = getMethod()
        client_socket.sendall(response.encode('utf-8'))

    client_socket.close()
