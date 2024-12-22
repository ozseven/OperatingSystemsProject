
def exceptionMiddleware(func):
    def wrapper( *args, **kwargs):
        try:
            return func( *args, **kwargs)
        except Exception as e:
            print(e)
            return errorComponent(str(e))
    return wrapper

def errorComponent(error: str):
    body =f"""<!DOCTYPE html>
<html>
<head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Simple Web Server</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<body>
<div class="container mt-4 alert alert-danger" role="alert">
  Hata!!!<a href="#" class="alert-link"> {error}</a>. Lütfen hata mesajını dikkate alınız.
</div>
</body>

</html>"""
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {len(body.encode('utf-8'))}\r\n"
        "\r\n"
        f"{body}"
    )
    return response.encode("utf-8")