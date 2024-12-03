from business.customPageService import CustomPageService



class MethodService:
    def __init__(self,slug):
        self.customPage = CustomPageService(slug)
    def getMethod(self):


        # Bu methodda url alınacak ve istenilen sayfa geri dönülecektir.

        response =  f"""\
HTTP/1.1 200 OK

<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Socket Server</title>
    </head>
    <body>
        <div class="container">
            {self.customPage.page()}
        </div>
        <div class="container">
            <form action="/upload" method="post" enctype="multipart/form-data">
                <label for="files">Birden fazla dosya seçin:</label>
                <input type="file" id="files" name="files[]" multiple>
                <button type="submit">Yükle</button>
            </form>
        </div>
    </body>
</html>
"""
        return response
