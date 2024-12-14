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
    <h1> POST İsteği Test Formu </h1>
        <div class="container">                 
            <form action="/" method="POST"  enctype="application/x-www-form-urlencoded">
                <label for="name">İSİM:</label><input type="text" id="name" name="name" required></form>
                <button type="submit" onclick="submitForm()" >Yükle</button>
            </form>
            <script>
            function submitForm() {{
                var form = document.querySelector('form');
                var name = document.getElementById('name').value;
                // Burada JavaScript değişkeni ile POST isteği çıktısı oluşturuluyor
                var response = 'POST isteği alındı. Veri: ' + name;
                // Formu gönder
                form.submit();
            }}
            </script>
        </div>
    </body>
</html>
"""




        return response
