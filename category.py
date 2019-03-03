import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


ua = UserAgent()
url = "https://codingbat.com/java"
headers = {'user-agent': ua.chrome}


# Response
response = requests.get(url, headers=headers)
# print(response.content)

soup = BeautifulSoup(response.content, 'lxml')
expecteDivs = soup.findAll("div", {"class": "summ"})

allResource = {
    allData.a.span.text: allData.a['href'] for allData in expecteDivs}
print(allResource)

# for alldata in expecteDivs:
#     print(alldata)
