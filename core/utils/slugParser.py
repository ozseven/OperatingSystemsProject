from urllib import parse

from core.middleware.exceptionMiddleware.exceptionMiddleware import exceptionMiddleware
from core.middleware.loggingMiddleware.loggingMiddleware import loggingMiddleware

@loggingMiddleware
@exceptionMiddleware
def slugParser(request) -> str:
    lines = request.splitlines()
    line = lines[0]
    _slug = line.replace("GET", "").replace(" ", "").replace("HTTP/1.1", "").replace("POST","")
    _slug = parse.unquote(_slug)
    return _slug