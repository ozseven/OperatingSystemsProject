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
        body_items = [f"<li class='list-group-item d-flex justify-content-between align-items-center' data-id={file}><a href='/files{slug[1:]}/{file}'>{file}<span class='badge badge-primary badge-pill'><a href='/download/{slug}/{file}'>  &#x2B73;</a></span></li> " for file in fileList]
    else:
        body_items = ""
    body = "<ol class='list-group'>" + "".join(body_items) + "</ol>"
    body += f"""<br>{formComponent(slug)}""" # formComponent fonksiyonunu çağırdık
    return body

@mainComponent
def homeComponent():
    return "<div class='page-title'>Welcome to the Home Page</div>"


@mainComponent
def errorComponent(error: str):
    return f"<div class='page-title'>Error</div><p>{error}</p>"


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

def downloadComponent(slug:str):
    with open(rf"C:\ProjectFilesNKU\{slug}", 'r+b') as f:
        print(f"C:\ProjectFilesNKU\{slug}")
        _,fileName = slug.rsplit("/",1)
        file =f"""HTTP/1.1 200 OK
Content-Type: application/octet-stream
Content-Disposition: attachment; filename="{fileName}"
Content-Length: 


""" .encode("UTF-8")

        file +=f.read()
        return file

def dowload():
    return"""
    <p>Merhan</p>
    """