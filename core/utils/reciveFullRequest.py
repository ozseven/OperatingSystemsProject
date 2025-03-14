

def receive_full_request(client_socket, buffer_size = 65550):
    """
    Bu fonksiyon, TCP üzerinden gelen istekleri alır ve birleştirir.
    İçerik uzunluğu bilgisi sağlandığında döngü sonlanır.
    :param client_socket: Verilerin alındığı soket nesnesi
    :param buffer_size: Her defasında alınacak veri miktarı (TCP üzerinden tek seferde aktarılabilecek maksimum paket boyutu 66550'dir.)
    :return: Tüm paketleri birleştirilmiş http isteği.
    """

    request_data = b""
    headers_received = False
    content_length = 0

    while True:
        chunk = client_socket.recv(buffer_size)
        request_data += chunk

        if not headers_received and b"\r\n\r\n" in request_data:
            headers, body = request_data.split(b"\r\n\r\n", 1)
            headers_received = True

            for line in headers.split(b"\r\n"):
                if line.startswith(b"Content-Length:"):
                    content_length = int(line.split(b":")[1].strip())
                    break

        if headers_received:
            body = request_data.split(b"\r\n\r\n", 1)[1]
            if len (body) >= content_length:
                break

    return request_data

 #Post isteği bitmiştir.