import requests
from bs4 import BeautifulSoup

url = "http://teaching.com.tw/member/case-list.php"
html = requests.get(url)
html.encoding = "big5"
#print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')
cases = []
titles = soup.select('tr[title="此案件可接洽"]')
for title in titles:
    case = []
    flag = False
    for inf in title.stripped_strings:
        if (inf == "New!"):
            flag = True
            continue
        case.append(inf)
    if flag:
        case.append("New")
    else:
        case.append("Old")
    cases.append(case)
