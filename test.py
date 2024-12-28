import threading
import requests

def make_download_request():
        response = requests.get("http://localhost:8080/download/WIN_20240301_16_45_28_Pro.mp4")
        print(f"download:ilk dosya {response.status_code}")


def make_download_request2():
    response = requests.get("http://localhost:8080/download/WIN_20240301_17_02_25_Pro.mp4")
    print(f"download:ikinci dosya {response.status_code}")

def make_get_request():
        response = requests.get("http://localhost:8080/files")
        print(f"Files:{response.status_code}")


for i in range(100):
    t = threading.Thread(target=make_get_request)
    t.start()



thread1 = threading.Thread(target=make_download_request)
thread2 = threading.Thread(target=make_download_request2)
thread3 = threading.Thread(target=make_download_request2)
thread4 = threading.Thread(target=make_download_request)
thread5 = threading.Thread(target=make_download_request)
thread6 = threading.Thread(target=make_download_request2)

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()