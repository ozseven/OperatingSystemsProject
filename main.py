import socket
from concurrent.futures import ThreadPoolExecutor
import os
from core.middleware.exceptionMiddleware.exceptionMiddleware import exceptionMiddleware
from core.utils.binaryParser import save_file_from_bytes
from core.utils.reciveFullRequest import receive_full_request
from core.utils.slugParser import slugParser
from view.dataView import DataView as dataView

HOST = '127.0.0.1'
PORT = 8080
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

# Ensure the directory exists
if not os.path.exists("C:\\ProjectFilesNKU"):
    os.mkdir("C:\\ProjectFilesNKU")

print(f"Sunucu {HOST}:{PORT} üzerinde çalışıyor...")

@exceptionMiddleware
def handle_get_request(client_socket, request):
        decoded_request = request.decode('utf-8')
        slug = slugParser(decoded_request)
        view= dataView(slug).getTemplate()
        client_socket.sendall(view)


@exceptionMiddleware
def handle_post_request(client_socket, request):
        save_file_from_bytes(request)
        handle_get_request(client_socket, request[:100])  # You can send a similar response as GET for POST


def handle_client(client_socket, client_address):
    """
    İstemci tarafından gelen kodları uygun http methoduna göre işler.
    :param client_socket: İstemciye bağlı sokettir.
    :param client_address: Bağlı olunan istemci adresidir.
    :return: None: Fonksiyon herhangi birşey dönmez.
    """
    try:
        request = receive_full_request(client_socket, 67000)

        if request.startswith(b"GET"):
            handle_get_request(client_socket, request)

        elif request.startswith(b"POST"):
            handle_post_request(client_socket, request)

        else:
            client_socket.sendall("405 Method Not Allowed".encode('utf-8'))

    except Exception as e:
        print(f"Hata: {e}")
        client_socket.sendall("500 Internal Server Error".encode('utf-8'))

    finally:
        client_socket.close()


if __name__ == "__main__":
    # Thread pool for handling multiple client requests
    executor = ThreadPoolExecutor(max_workers=5)

    while True:
        client_socket, client_address = server_socket.accept()
        # Handle client connections asynchronously
        executor.submit(handle_client, client_socket, client_address)
