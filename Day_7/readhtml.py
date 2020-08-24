#step1: get the html input using requests library
#step2: use bs4( beautifulsoup library) to read html page


import requests
from bs4 import BeautifulSoup

try:
    url = "https://www.techworldguru.com/python-assignment-2/"
    response= requests.get(url)
    if response.status_code == 200:
        #print(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a'):
            print(link.get('href'))

except Exception as err:
    print(err)