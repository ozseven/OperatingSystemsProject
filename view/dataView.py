from requests import delete

from core.guard import authentication
from core.middleware.exceptionMiddleware.exceptionMiddleware import exceptionMiddleware, errorComponent
from view.templateFiles.mainHtmlComponent import homeComponent, aboutComponent, fileComponent, \
    logComponent, downloadComponent, formComponent, redirectComponent, loginComponent
from dataAccess.dataService import DataService as dataService
from core.middleware.loggingMiddleware.loggingMiddleware import LogList as logList


class DataView:
    def __init__(self, slug: str):
        self.slug = slug
    @exceptionMiddleware
    def getTemplate(self):
        """
        Bu fonksiyon, sağlanan slug nesnesi ile kullanıcıya ilgili html componentlerinden hangisinin dönülmesi gerektiğini belirler
        :return: İlgi sayfa html componenti
        """
        if self.slug == "/":
            return homeComponent().encode("UTF-8")
        elif self.slug == "/about":
            return aboutComponent().encode("UTF-8")
        elif self.slug.startswith("/files"):
            fileList = dataService.getFileList(self.slug[6:])
            return fileComponent(fileList, self.slug[6:]).encode("UTF-8")
        elif self.slug == "/logs":
            logsList = logList().logList
            return logComponent(logsList).encode("UTF-8")
        elif self.slug.startswith("/download"):
            return downloadComponent(self.slug[9:])
        elif self.slug.startswith("/createFolder"):
            dataService.createFolder(self.slug)
            redirectSlug = self.slug.replace("createFolder", "files").replace("?filename=", "/")
            return redirectComponent(redirectSlug).encode("UTF-8")
        elif self.slug == "/admin":
            if not authentication.isAuthenticated:
                return loginComponent().encode("UTF-8")
            else :
                fileList = dataService.getFileList("/")
                return fileComponent(fileList,"/").encode("UTF-8")
        elif self.slug == "/logout":
            authentication.isAuthenticated =False
            return loginComponent().encode("UTF-8")
        elif self.slug.startswith("/delete"):
            if not authentication.isAuthenticated:
                return loginComponent().encode("UTF-8")
            else :
                dataService.deleteFile(self.slug[8:])
                fileList = dataService.getFileList(self.slug[7:].rsplit("/")[0])
                return fileComponent(fileList, self.slug[7:].rsplit("/")[0]).encode("UTF-8")
        else:
            return errorComponent("Gitmek istediğiniz adresi kontrol edin.")
