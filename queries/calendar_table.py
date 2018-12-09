DROP_CALENDAR_TABLE = '''
DROP TABLE IF EXISTS calendars;
'''

CREATE_CALENDAR_TABLE = '''
CREATE TABLE IF NOT EXISTS calendars (
  calendar_id int(8),
  year char(4),
  url varchar(256),
  title varchar(256),
  category varchar(64),
  author varchar(32),
  parts int(8),
  likes int(8),
  subsc int(8),
  items int(8),
  actual_items int(8)
);
'''
INSERT_CALENDAR_TABLE = '''
INSERT INTO calendars (
  calendar_id,
  year,
  url,
  title,
  category,
  author,
  parts,
  likes,
  subsc,
  items,
  actual_items
)
VALUES
(
  {calendar_id},
  "{year}",
  "{url}",
  "{title}",
  "{category}",
  "{author}",
  {parts},
  {likes},
  {subsc},
  {items},
  {actual_items}
);
'''

SELECT_URL_TABLE = '''
SELECT *
FROM calendars;
'''

