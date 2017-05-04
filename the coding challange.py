import requests
from bs4 import BeautifulSoup
def urlextractor (max):
    page=1
    while max <= 1:
     try:
        url='https://www.amazon.com/s/ref=sr_pg_2?rh=n%3A283155%2Ck%3Ahistory&page='+str(page)
        sourcecode=requests.get(url)
        file=sourcecode.text
        s= BeautifulSoup(file)
        for link in s.findall('a',{'class':'item-name'}):
            href ='https://www.amazon.com' + link.get('href')
            page +=1
            break

        print(href)

    except:




urlextractor(2)
