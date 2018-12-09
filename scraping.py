import requests
from bs4 import BeautifulSoup
from time import sleep
from cursor_execute import cursor_execute
from queries.url_table import SELECT_URL_TABLE

QIITA_URL = "https://qiita.com"
CALENDAR_LIST_URL = QIITA_URL + "/advent-calendar/{year}/calendars?page={page}"
YEAR_LIST = [2015, 2016, 2017, 2018]
MAX_PAGE = 50
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

def scraping_calendar_detail():
    calendar_list = cursor_execute(SELECT_URL_TABLE)
    calendar_detail_list = []
    for y, u in calendar_list:
        html = requests.get(u).text
        soup = BeautifulSoup(html, "html.parser")
        sleep(SLEEP_TIME)

        title = soup.find("title").contents[0].split(" Advent")[0]
        info = soup.find_all("div", {"class": "adventCalendarSection_info"})
        category = info[0].find("a").contents[0]
        author = info[1].find("a").contents[1]

        parts = soup.find("div", {"title": "Participants"}).contents[1].replace(" ", "")
        likes = soup.find("div", {"title": "Likes"}).contents[1].replace(" ", "")
        subsc = soup.find("div", {"title": "Subscribers"}).contents[1].replace(" ", "")

        blocks = soup.find_all("div", {"class": "adventCalendarItem"})
        items = len(blocks)

        cancel_title = "Overwritable because of past due"
        cancels = ["items" for b in blocks if b.find("a", {"title": cancel_title})]
        actual_items = items - len(cancels)

        calendar_detail_list.append(
            [
                y, u, title, category, author,
                int(parts), int(likes), int(subsc), 
                items, actual_items
            ]
        )

    return calendar_detail_list

def main():
    #year_url_list_dic = scraping_calendar_url()
    #for y, ul in year_url_list_dic.items():
    #    print(y, len(ul))

    calendar_detail_list = scraping_calendar_detail()

if __name__ == '__main__':
    main()

