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
    def parse_request(request):
        lines = request.splitlines()
        method, path, _ = lines[0].split()
        headers = {}

        for header_line in lines[2:]:
            try:
                header, value = header_line.split(':', 1)  # karakterine göre ayır
                headers[header] = value.strip()  # Boşlukları sil ve sözlüğe ekle
            except ValueError:  # Eğer ayırma işlemi başarısız olursa
                pass
        return method, path, headers




    method, path, headers = parse_request(request)
    if request.startswith("GET"):
        client_socket.sendall(response.encode('utf-8'))

    elif request.startswith("POST"):
        content_length = int(headers['Content-Length'])
        post_data = client_socket.recv(content_length).decode('utf-8')
        post_data = urllib.parse.parse_qs(post_data)
        if 'name' in post_data:
            name = post_data['name'][0]
        else:
            name = "İsim bilgisi yok"


        if 'headers' in post_data:
            with open('C:/ProjectFilesNKU/garbage.txt', 'a' , encoding ='utf-8') as f:
                f.write(f"Name:{name}" + '\n')
            response = "POST isteği alındı. Veri: " + post_data
            client_socket.sendall(
            f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body>{response}</body></html>".encode('utf-8'))
        else:
            response ="Name parametresi bulunamadi."
            client_socket.sendall(f"HTTP/1.1 400 Bad Request\r\nContent-Type: text/plain\r\n\r\n{response}".encode('utf-8'))
         #client_socket.sendall(response.encode('utf-8'))
    client_socket.close()