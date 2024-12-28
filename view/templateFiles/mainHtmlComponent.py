from core.guard import authentication
from core.guard.authentication import authenticate
from core.middleware.exceptionMiddleware.exceptionMiddleware import exceptionMiddleware
from dataAccess.dataService import DataService


@exceptionMiddleware
def mainComponent(func):
    def wrapper(*args, **kwargs):
        body = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Simple Web Server</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
            <style>
                body {{
                    font-family: 'Arial', sans-serif;
                    background-color: #f8f9fa;
                    color: #333;
                }}
                .container {{
                    margin-top: 50px;
                }}
                .page-title {{
                    text-align: center;
                    font-size: 2rem;
                    margin-bottom: 20px;
                    color: #0056b3;
                }}
                .form-container {{
                    background-color: #fff;
                    padding: 30px;
                    border-radius: 8px;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                }}
                .form-container input {{
                    margin-bottom: 15px;
                }}
                .form-container button {{
                    background-color: #007bff;
                    color: white;
                    border: none;
                    padding: 10px 15px;
                    border-radius: 5px;
                    cursor: pointer;
                }}
                .form-container button:hover {{
                    background-color: #0056b3;
                }}
                .footer {{
                    text-align: center;
                    margin-top: 30px;
                    font-size: 0.9rem;
                    color: #777;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                {func(*args, **kwargs)}
            </div>
            <div class="footer">
                <p>&copy; 2024 Your Website. All rights reserved.</p>
            </div>
        </body>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
        </html>"""
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            f"Content-Length: {len(body.encode('utf-8'))}\r\n"
            "\r\n"
            f"{body}"
        )
        return response

    return wrapper

def formComponent(slug):
    return f"""
    <div class="form-container">
        <h3>Upload Your File</h3>
        <form enctype="multipart/form-data" action="http://localhost:8080/files{slug}" method="POST">
            <div class="mb-3">
                <label for="myfile" class="form-label">Select a file:</label>
                <input type="file" class="form-control" id="filename" name="filename">
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
    """

@mainComponent
def fileComponent(fileList, slug):
    if type(fileList) == str:
        body_items = fileList
    elif type(fileList) == list:
        body_items = [
            f"<li class='list-group-item d-flex justify-content-between align-items-center' data-id={file}><a href='/files{slug}/{file}'>{file}</a><span class='ms-auto rounded-right badge badge-primary badge-pill'><a href='/download{slug}/{file}'>&#x2B73;</a></span>"
            +(f"<span class='badge badge-danger badge-pill '><a href='/delete{slug}{file}'>&#x1F5D1;</a></span>" if authentication.isAuthenticated else "")
            +"</li>"
            for file in fileList]
    else:
        body_items = ""
    if "/" in slug:
        parentDirectory, _ = slug.rsplit("/", 1)
    else:
        parentDirectory = slug
    body = "<ol class='list-group'>" + f"<li class='list-group-item d-flex justify-content-between align-items-center'><a href='/files{parentDirectory}'>...</a></li>" + "".join(
        body_items) + f'<li><form method="GET" action="/createFolder{slug}"><input type="text" class="form-control" id="filename" name="filename" placeholder="Yeni klasör eklemek için ismini yazın"><button type="submit" class="btn btn-primary">Submit</button></form></li>' + "</ol>"
    body += f"""<br>{formComponent(slug)}"""  # formComponent fonksiyonunu çağırdık
    return body


@mainComponent
def homeComponent():
    return f"""
    <style>
        body {{
            font-family: Verdana, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f9;
            animation: fadeInAnimation ease 3s;
            animation-iteration-count: 1;
            animation-fill-mode: forwards;
        }}

        @keyframes fadeInAnimation {{
            0% {{
                opacity: 0;
            }}

            100% {{
                opacity: 1;
            }}
        }}
        .container {{
            text-align: center;
        }}
        a {{
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            text-decoration: none;
            color: white;
            background-color: #ff0000e6;
            border-radius: 5px;
            font-size: 16px;
        }}
        a:hover {{
            background-color: #b30000;
        }}
        footer {{
 			position: fixed;
 			bottom: 0px;
 			left: 0px;
 			width: 100%;
            padding-bottom:20px;
}}
        </style>
    <div class="container">
        <h1>Ana Sayfaya Hoşgeldiniz</h1>
        <p>Dizine gitmek için tıklayınız.</p>
        <a href="/files">/files</a>
        <footer>Hazırlayanlar: Ahmet Özseven, Ahmet Hakan Özkurt, Berkay Emikönel, Yiğit Kadayıfçı, Hüseyin Berke Ok, Kerem Batı</footer>
    </div>
"""
    


@mainComponent
def aboutComponent():
    return "<div class='page-title'>About Us</div><p>This is the about page.</p>"


@mainComponent
def logComponent(list):
    body_items = "<ul>"
    for item in list:
        body_items += f"<li>{item}</li>"
    body_items += "</ul>"
    return body_items

@exceptionMiddleware
def downloadComponent(slug: str):
        fileBytes = DataService.downloadFile(slug)
        _, fileName = slug.rsplit("/", 1)
        file = f"""HTTP/1.1 200 OK
Content-Type: application/octet-stream
Content-Disposition: attachment; filename="{fileName}"


""".encode("UTF-8")

        file += fileBytes
        return file

@exceptionMiddleware
def redirectComponent(slug: str):
    body = f"""
    <!DOCTYPE html>
        <html lang="tr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Redirecting...</title>
            <meta http-equiv="refresh" content="1; url=http://localhost:8080{slug}">
        </head>
        <body>
            <h1>Klasör başarıyla oluştu!!!</h1>
            <p>Şimdi yönlendiriliyorsunuz <a href="/{slug}">here</a>.</p>
        </body>
        </html>
    """
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {len(body.encode('utf-8'))}\r\n"
        "\r\n"
        f"{body}"
    )
    return response

@mainComponent
def loginComponent():
    return """    <form method="post" action="http://localhost:8080/admin">
    <input type="text" name="username" placeholder="username">
    <input type="password" name="password" placeholder="password">
    <button type="submit">Giriş</button>
</form>"""
