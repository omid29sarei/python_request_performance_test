import requests
import time
from requests.sessions import Session


##### SYNC WITH SESSION OBJECT
def download_link(link:str,session:Session)->None:

    with session.get(link) as response:
        result = response.content
        print(f'Read {len(result)} from {link}')

def download_all_link(link_list:list)->None:
    with requests.Session() as session:
        for link in link_list:
            download_link(link,session=session)



url_list = ["https://www.google.com/","https://www.bing.com"]*50
start = time.time()
download_all_link(url_list)
end = time.time()
print(f'download {len(url_list)} links in {end - start} seconds')
