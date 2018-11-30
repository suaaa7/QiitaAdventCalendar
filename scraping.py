import requests
from bs4 import BeautifulSoup
from time import sleep

QIITA_URL = "https://qiita.com"
CALENDAR_LIST_URL = QIITA_URL + "/advent-calendar/{year}/calendars?page={page}"
YEAR_LIST = [2014, 2015, 2016, 2017, 2018]

def main():
    for year in YEAR_LIST:
        for page in range(1, 2):
            url = CALENDAR_LIST_URL.format(
                        year=str(year), 
                        page=str(page))
            print(url)
            html = requests.get(url).text
            soup = BeautifulSoup(html, "html.parser")
            td = soup.find("tbody")
            if len(td.find_all("a")) == 0:
                break
            sleep(5)
            print(td.find_all("a"))

if __name__ == '__main__':
    main()

