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
        {self.customPage.page()}
    </body>
</html>
"""
        return response
