from view.templateFiles.mainHtmlComponent import errorComponent


def exceptionMiddleware(func):
    def wrapper( *args, **kwargs):
        try:
            return func( *args, **kwargs)
        except Exception as e:
            body =f"""<div class="alert alert-warning" role="alert">
  Hata!!! <strong>{e}</strong>
</div>"""
            print(e)
            return errorComponent(body)
    return wrapper