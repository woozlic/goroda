from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import socks
import time
import socket
import string

#socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)#ip tor
#socket.socket = socks.socksocket

en_words = string.ascii_uppercase

ua = UserAgent()
headers = {
        "User-Agent": ua.random,
        }

def checkIP():
    ip = requests.get('http://checkip.dyndns.org').content# проверяет наш айпи
    soup = BeautifulSoup(ip, 'html.parser')
    print(soup.find('body').text)
    
checkIP()

def fwrite(fname, lst):
    with open(str(fname)+".txt", "w") as f:
        msg = "\n".join(lst)
        f.write(msg)
city = "Ya"
url = "http://www.1000mest.ru/city"+city#юрл страницы
resp = requests.get(url, headers=headers)
if str(resp) == "<Response [200]>":
    lst = []
    resp.encoding = "utf-8"#кодировка
        #for key, value in resp.request.headers.items(): #наш юзерагент
         #       print(key+": "+value)

    soup = BeautifulSoup(resp.text, 'html.parser')
        #print(soup.prettify())
    posts = soup.findAll("td")
    for post in posts:
        lst.append(post.text)
    print(lst)
    fwrite(city, lst)
else:
    print("нас поймали")
