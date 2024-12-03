import socket
import urllib
from dataclasses import replace

from methodServices import MethodService

HOST = '127.0.0.1'
PORT = 8080
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Sunucu {HOST}:{PORT} üzerinde çalışıyor...")


while True:
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(1024).decode('utf-8')
    def slug():
        lines = request.splitlines()
        line = lines[0]
        _slug = line.replace("GET","").replace(" ","").replace("HTTP/1.1", "")
        _slug = urllib.parse.unquote(_slug)
        return _slug
    slug = slug()
    methods = MethodService(slug)
    response = methods.getMethod()
    #Tarayıcıya veri gönderme
    if request.startswith("GET"):
        client_socket.sendall(response.encode('utf-8'))
    client_socket.close()
