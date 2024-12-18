import socket
from concurrent.futures import ThreadPoolExecutor
from urllib import parse
from core.middleware.exceptionMiddleware.exceptionMiddleware import exceptionMiddleware
from core.utils.slugParser import slugParser
from view.dataView import DataView as dataView

HOST = '127.0.0.1'
PORT = 8080

def handle_client(client_socket, client_address):
    try:
        request = client_socket.recv(2048).decode('utf-8')

        @exceptionMiddleware
        def getMethod():
            slug: str = slugParser(request)
            view = dataView(slug).getTemplate()
            return view

        if request.startswith("GET"):
            response = getMethod()
            client_socket.sendall(response.encode('utf-8'))

        elif request.startswith("POST"):
            # POST işleme mantığınız buraya eklenebilir.
            pass

        else:
            client_socket.sendall(
                b"HTTP/1.1 405 Method Not Allowed\r\nContent-Type: text/plain\r\n\r\nMethod not allowed."
            )

    except Exception as e:
        print(f"Bağlantı hatası: {e}")

    finally:
        client_socket.close()
        print(f"Bağlantı kapatıldı: {client_address}")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"Sunucu {HOST}:{PORT} üzerinde çalışıyor...")

    # ThreadPoolExecutor ile bir işçi havuzu oluştur
    with ThreadPoolExecutor(max_workers=10) as executor:  # Maksimum 10 iş parçacığı çalıştırılabilir
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Yeni bağlantı: {client_address}")

            # handle_client fonksiyonunu işçi havuzunda çalıştır
            executor.submit(handle_client, client_socket, client_address)

if __name__ == "__main__":
    main()