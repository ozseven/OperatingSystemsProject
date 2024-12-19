from os import error


def mainComponent(func):
    def wrapper(*args, **kwargs):
        body = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        </head>
        <body>
            {func(*args, **kwargs)}
            <div>
            {formComponent()}
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


@mainComponent
def fileComponent(fileList) -> str:
    if type(fileList) == str:
        body_items = fileList
    elif type(fileList) == list:
        body_items = [f"<li>{file}</li>" for file in fileList]
    else:
        body_items = ""

    body = f'<a href="{""}">' +"<ul>" + "".join(body_items) + "</ul>"

    return body

@mainComponent
def homeComponent():
    return "This is the home page"

@mainComponent
def errorComponent(error:str):
    return error

@mainComponent
def aboutComponent():
    return "This is the about page"

@mainComponent
def logComponent(list):
    body_items ="<ul>"
    for item in list:
        body_items += f"<li>{item}</li>"
    body_items +="</ul>"
    return body_items

def formComponent():
    return """
<form action="localhost:8080"  method="POST">
    <div class="form-group">
        <label for="ControlFile">Dosya seçiniz</label>
        <br><br>
        <input type="file" value="yükle" class="control-file" id="ControlFile" name="control_file">
        <br><br>
        <input type="submit" value="Kaydet">
    </div>
</form>
    """

