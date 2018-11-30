from cursor_execute import cursor_execute
from queries.create_table import DROP_CALENDAR_TABLE, CREATE_CALENDAR_TABLE

def main():
    _ = cursor_execute(DROP_CALENDAR_TABLE)
    _ = cursor_execute(CREATE_CALENDAR_TABLE)

if __name__ == '__main__':
    main()

