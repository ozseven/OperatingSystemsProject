import socket
from concurrent.futures import ThreadPoolExecutor
from urllib import parse
from core.middleware.exceptionMiddleware.exceptionMiddleware import exceptionMiddleware
from core.utils.binaryParser import save_file_from_bytes
from core.utils.slugParser import slugParser
from view.dataView import DataView as dataView
from core.utils.reciveFullRequest import receive_full_request
import os


HOST = '127.0.0.1'
PORT = 8080
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

if not os.path.exists("C:\ProjectFilesNKU"):
    os.mkdir("C:\ProjectFilesNKU")

print(f"Sunucu {HOST}:{PORT} üzerinde çalışıyor...")
while True:
    client_socket, client_address = server_socket.accept()
    request = receive_full_request(client_socket, 67000)
def handle_client(client_socket, client_address):
    try:
        request = client_socket.recv(2048).decode('utf-8')

    @exceptionMiddleware
    def getMethod(request):
        decoded_request = request.decode('utf-8')
        slug:str = slugParser(decoded_request)
        view = dataView(slug).getTemplate()
        return view

    def postMethod():
        save_file_from_bytes(request)
        response = getMethod(request[:100])
        client_socket.sendall(response.encode('utf-8'))

    if request.startswith(b"GET"):
        response = getMethod(request)
        client_socket.sendall(response.encode('utf-8'))

    elif request.startswith(b"POST"):
        postMethod()

    client_socket.close()

            # handle_client fonksiyonunu işçi havuzunda çalıştır
            executor.submit(handle_client, client_socket, client_address)

if __name__ == "__main__":
    main()

