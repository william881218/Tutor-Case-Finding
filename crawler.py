import requests
from bs4 import BeautifulSoup

class TutorCase:
    url = ""
    cases = []

    def __init__(self, url=""):
        self.url = url
        self.cases.clear()
        html = requests.get(self.url)
        html.encoding = "big5"
        soup = BeautifulSoup(html.text, 'html.parser')
        titles = soup.select('tr[title="此案件可接洽"]')
        for title in titles:
            case = []
            for infor in title.stripped_strings:
                case.append(infor)
            if 'New!' not in case:
                case.insert(4, "Old!")
            self.cases.append(case)

    def printCases(self):
        for case in self.cases:
            for infor in case:
                print(infor, end=' ')
            print("")
