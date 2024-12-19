import requests
import threading

def download_file(url, filename):
    response = requests.get(url, stream =True)
    with open (filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size = 1024):
         if chunk:
            f.write(chunk)

# İndirilecek dosya url'si
url = "http://127.0.0.1/yol/yol2/dosya.txt"
# Kaydedilecek dosya ismi
filename = "indirilmis_dosya.txt"

download_file(url, filename)

def download_multiple_files(urls, filenames):

    threads = []
    for url, filename in zip(urls, filenames):
        thread = threading.Thread(target=download_file, args=(url, filename))
        threads.append(thread)
        thread.start()

        for thread in threads:
            thread.join()

#İndirilecek URL'ler
urls = ["", "http://url2", "http://url3"]
#İndirilecek dosya isimleri
filenames = ["yeni.pptx", "file2.txt", "file3.txt"]


download_multiple_files(urls, filenames)











