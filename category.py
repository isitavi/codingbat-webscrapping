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

    # Grab all contents from question links
    for contents in questionURL:
        contentResponse = requests.get(contents, headers=headers)
        contentSoup = BeautifulSoup(contentResponse.content, 'lxml')
        contentDiv = contentSoup.find("div", {"class": "indent"})
        problemStatement = contentDiv.table.div.text
        nextSiblings = contentDiv.table.div.next_siblings

        getExample = [
            sibling for sibling in nextSiblings if sibling.string is not None]
        print(problemStatement)
        for example in getExample:
            print(example)
