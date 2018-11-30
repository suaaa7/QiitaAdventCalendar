DROP_CALENDAR_TABLE = '''
DROP TABLE IF EXISTS calenders;
'''

CREATE_CALENDAR_TABLE = '''
CREATE TABLE IF NOT EXISTS calendars (
    id varchar(32),
    calendar_name varchar(256)
);
'''

