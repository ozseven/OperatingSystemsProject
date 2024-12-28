from core.guard.authentication import authenticate
from core.utils.binaryParser import save_file_from_bytes
from core.utils.slugParser import slugParser


def postHandle(request):
    slug =slugParser(request[:150].decode('utf-8'))
    if "admin" in slug:
        request = request.decode('utf-8')
        password = request.rsplit("&password=",1)[1]
        name = request.rsplit('username=',1)[1].split('&')[0]
        authenticate(name, password)

    elif "files" in slug:
        save_file_from_bytes(request)