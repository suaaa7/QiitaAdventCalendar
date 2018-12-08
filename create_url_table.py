from cursor_execute import cursor_execute
from queries.url_table import DROP_URL_TABLE, CREATE_URL_TABLE, INSERT_URL_TABLE
from scraping import scraping_calendar_url

def main():
    _ = cursor_execute(DROP_URL_TABLE)
    _ = cursor_execute(CREATE_URL_TABLE)

    year_url_list_dic = scraping_calendar_url()
    for y, ul in year_url_list_dic.items():
        for i, u in enumerate(ul):
            query = INSERT_URL_TABLE.format(year=y, url=u)
            cursor_execute(query)
        print("year: {y}, count: {c}".format(y=str(y), c=str(i+1)))

if __name__ == '__main__':
    main()

