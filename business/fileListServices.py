import os

class FileListServices:
    def __init__(self):
        pass
    def fileList(self,directory):
        try:
            return os.listdir("C:\ProjectFilesNKU" + directory)
        except FileNotFoundError:
            return ["Böyle bir dizin yok"]