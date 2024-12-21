

def receive_full_request(client_socket, buffer_size = 4096):

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
                    content_length = int(line.split(":")[1].strip())
                    break

                if headers_received:
                    body = request_data.split(b"\r\n\r\n", 1)[1]
                    if len (body) >= content_length:
                        break

    return request_data

 #Post isteği bitmiştir.