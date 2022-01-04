import requests
import time

def download_link(url:str) -> None:
    result = requests.get(url).content
    print(f'Read {len(result)} from {url}')
def download_all(urls:list) -> None:
    for url in urls:
        download_link(url)
        
url_list = ["https://www.google.com/","https://www.bing.com"]*50
start = time.time()
download_all(url_list)
end = time.time()
print(f'download {len(url_list)} links in {end - start} seconds')