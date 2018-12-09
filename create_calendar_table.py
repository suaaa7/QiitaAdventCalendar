from cursor_execute import cursor_execute
from queries.calendar_table import (
    DROP_CALENDAR_TABLE, 
    CREATE_CALENDAR_TABLE, 
    INSERT_CALENDAR_TABLE
)
from scraping import scraping_calendar_detail

def main():
    calendar_detail_list = scraping_calendar_detail()

    _ = cursor_execute(DROP_CALENDAR_TABLE)
    _ = cursor_execute(CREATE_CALENDAR_TABLE)

    for i, d in enumerate(calendar_detail_list):
        query = INSERT_CALENDAR_TABLE.format(
                    calendar_id = i+1,
                    year = d[0],
                    url = d[1],
                    title = "title",
                    category = d[3],
                    author = d[4],
                    parts = d[5],
                    likes = d[6],
                    subsc = d[7],
                    items = d[8],
                    actual_items = d[9]
                )
        cursor_execute(query)

    print("INSERT: {count}".format(count=i+1))

if __name__ == '__main__':
    main()

