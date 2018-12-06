from cursor_execute import cursor_execute
from queries.create_table import DROP_URL_TABLE, CREATE_URL_TABLE, INSERT_URL_TABLE
from scraping import scraping_calendar_url

def main():
    _ = cursor_execute(DROP_URL_TABLE)
    _ = cursor_execute(CREATE_URL_TABLE)

    year_url_list_dic = scraping_calendar_url()
    for y, ul in year_url_list_dic.items():
        for u in ul:
            query = INSERT_URL_TABLE.format(year=y, url=u)
            print(query)
            cursor_execute(query)

if __name__ == '__main__':
    main()

