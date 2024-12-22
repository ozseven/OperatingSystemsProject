from core.middleware.exceptionMiddleware.exceptionMiddleware import exceptionMiddleware, errorComponent
from view.templateFiles.mainHtmlComponent import homeComponent, aboutComponent, fileComponent, \
    logComponent, downloadComponent, formComponent, redirectComponent
from dataAccess.dataService import DataService as dataService
from core.middleware.loggingMiddleware.loggingMiddleware import LogList as logList


class DataView:
    def __init__(self, slug: str):
        self.slug = slug
    @exceptionMiddleware
    def getTemplate(self):
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
        elif self.slug == "/form":
            return formComponent(self.slug).encode("UTF-8")
        elif self.slug.startswith("/download"):
            return downloadComponent(self.slug[9:])
        elif self.slug.startswith("/createFolder"):
            dataService.createFolder(self.slug)
            redirectSlug = self.slug.replace("createFolder", "files").replace("?filename=", "/")
            return redirectComponent(redirectSlug).encode("UTF-8")
        else:
            return errorComponent("Gitmek istediğiniz adresi kontrol edin.")
