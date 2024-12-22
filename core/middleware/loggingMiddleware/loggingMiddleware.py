import datetime


class LogList:
    logList =[]

    def addLog(self,data):
        """
        Bu fonksiyon, logları bellekteki 'logList' değişkenine ekler.
        :param data: log nesneleri
        :returns
            None: Bu fonksiyon herhangi bir değer dönmez

        """
        self.logList.append(data)

def loggingMiddleware(func):
    """
    Bu ara katman, fonksiyonların geri dönüş değerlerini kayıt etmek için yaratılmış bir sarmalayıcı fonksiyonudur.
    :param func: Hata yönetimi ile sarılacak fonksiyon.
    :return:
    """
    def wrapper(*args, **kwargs):
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        LogList().addLog(func(*args, **kwargs)+"-->"+date)
        return func(*args, **kwargs)
    return wrapper


