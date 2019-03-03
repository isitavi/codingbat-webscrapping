import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


ua = UserAgent()
baseURL = "https://codingbat.com"
requestURL = "https://codingbat.com/java"
headers = {'user-agent': ua.chrome}


# Response
response = requests.get(requestURL, headers=headers)
# print(response.content)

soup = BeautifulSoup(response.content, 'lxml')
expecteDivs = soup.findAll("div", {"class": "summ"})

# Dict Comprehension
# allResource = {
#     allData.a.span.text: baseURL+allData.a['href'] for allData in expecteDivs}
# print(allResource)

#
# for alldata in expecteDivs:
#     print(alldata)


# List Comprehension
allResource = [baseURL+allData.a['href'] for allData in expecteDivs]

for innerlink in allResource:
    individualLink = requests.get(innerlink, headers=headers)
    innerSoup = BeautifulSoup(individualLink.content, 'lxml')
    targetDivs = innerSoup.find("div", {"class": "tabin"})
    questionURL = [baseURL+td.a['href']
                   for td in targetDivs.table.find_all('td')]
    for url in questionURL:
        print(url)
    break

    # allCategory = [allCat.table.tr.td.a['href'] for allCat in targetDivs]
    # print(allCategory)
