from cursor_execute import cursor_execute
from queries.calendar_table import (
    DROP_CALENDAR_TABLE, 
    CREATE_CALENDAR_TABLE, 
    INSERT_CALENDAR_TABLE
)
from scraping import scraping_calendar_detail

def main():
    _ = cursor_execute(DROP_CALENDAR_TABLE)
    _ = cursor_execute(CREATE_CALENDAR_TABLE)

    calendar_detail_list = scraping_calendar_detail()
    for i, d in enumerate(calendar_detail_list):
        query = INSERT_CALENDAR_TABLE.format(
                    calendar_id = i+1,
                    year = d[0],
                    url = d[1],
                    title = "title",
                    parts = d[3],
                    likes = d[4],
                    subsc = d[5],
                    items = d[6],
                    actual_items = d[7]
                )
        cursor_execute(query)

    print("INSERT: {count}".format(count=i+1))

if __name__ == '__main__':
    main()

