import requests
from bs4 import BeautifulSoup
from time import sleep

QIITA_URL = "https://qiita.com"
CALENDAR_LIST_URL = QIITA_URL + "/advent-calendar/{year}/calendars?page={page}"
YEAR_LIST = [2015, 2016]
MAX_PAGE = 2
SLEEP_TIME = 2

def scraping_calendar_url():
    year_url_list_dic = {}
    for year in YEAR_LIST:
        url_list = []
        for page in range(1, MAX_PAGE):
            url = CALENDAR_LIST_URL.format(
                        year=str(year),
                        page=str(page))
            html = requests.get(url).text
            soup = BeautifulSoup(html, "html.parser")
            td = soup.find("tbody")
            if len(td.find_all("a")) == 0:
                break
            sleep(SLEEP_TIME)
            for a in td.find_all("a"):
                href = a.get("href")
                if "advent-calendar" in href and "subscr" not in href:
                    url_list.append(QIITA_URL + href)
        year_url_list_dic[year] = url_list
    return year_url_list_dic

def main():
    year_url_list_dic = scraping_calendar_url()
    for y, ul in year_url_list_dic.items():
        print(y, len(ul))

if __name__ == '__main__':
    main()

