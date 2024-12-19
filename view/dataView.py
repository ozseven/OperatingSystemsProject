from view.templateFiles.mainHtmlComponent import homeComponent, aboutComponent, fileComponent, errorComponent ,logComponent
from dataAccess.dataService import DataService as dataService
from core.middleware.loggingMiddleware.loggingMiddleware import LogList as logList

class DataView:
    slug ="/"

    def __init__(self,slug:str):
        self.slug = slug

    def getTemplate(self):
        if self.slug == "/":
            return homeComponent()
        elif self.slug == "/about":
            return aboutComponent()
        elif self.slug.startswith("/files"):
            fileList = dataService.getFileList(self.slug)
            return fileComponent(fileList,self.slug[6:])
        elif self.slug =="/logs":
            logsList = logList().logList
            return logComponent(logsList)
        else :
            return errorComponent("Gitmek istediğiniz adresi kontrol edin.")

