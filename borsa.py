
import requests
from bs4 import BeautifulSoup as bs
import time
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/80.0.3987.163 Safari/537.36 "
}
def sisecam():
     site="https://www.google.com/finance/quote/SISE:IST"
     request=requests.get(site,headers=header)
     kod=bs(request.content,'html5lib')
     marka=kod.find("div",{"class":"zzDege"}).text
     deger=kod.find("div",{"class":"YMlKec fxKbKc"}).text
     print(marka+" :"+deger)

def eregli():
     site="https://www.google.com/finance/quote/EREGL:IST"
     request=requests.get(site,headers=header)
     kod=bs(request.content,'html5lib')
     marka=kod.find("div",{"class":"zzDege"}).text
     deger=kod.find("div",{"class":"YMlKec fxKbKc"}).text
     print(marka+" :"+deger)

def ihlas():
     site="https://www.google.com/finance/quote/IHYAY:IST"
     request=requests.get(site,headers=header)
     kod=bs(request.content,'html5lib')
     marka=kod.find("div",{"class":"zzDege"}).text
     deger=kod.find("div",{"class":"YMlKec fxKbKc"}).text
     print(marka+" :"+deger)


while True:
 eregli()
 sisecam()
 ihlas()
 time.sleep(15)

