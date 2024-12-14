from business.fileListServices import FileListServices

fileList = FileListServices()
class CustomPageService:
    def __init__(self, slug):
        self.slug = slug

    def page (self):
        if self.slug.startswith("/files/"):
            files = fileList.fileList(self.slug[6:])
            text = ""
            for file in files:
                text = text + "<br>" + file
            return f"""
            <h1>File listesi</h1>
                {text}
            """
        match self.slug:
            case "/home":
                return """
                <h1>Merhaba, Socket Sunucusu Çalışıyor!</h1>
                """
            case "/":
                return """
                <h1>Merhaba, Socket Sunucusu Çalışıyor!</h1>
                """
            case "/files":
                htmlText =""
                files =fileList.fileList("")
                for file in files:
                    htmlText = htmlText +"<br>" +  file
                return f"""
                <h1>File listesi</h1>
                    {htmlText}
                """
            case default:
                return """
                <h1>Böyle bir sayfa yok</h1>
                """

