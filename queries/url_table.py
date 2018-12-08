DROP_URL_TABLE = '''
DROP TABLE IF EXISTS urls;
'''

CREATE_URL_TABLE = '''
CREATE TABLE IF NOT EXISTS urls (
  year char(4),
  url varchar(256)
);
'''

INSERT_URL_TABLE = '''
INSERT INTO urls (
  year,
  url
)
VALUES
(
  "{year}",
  "{url}"
);
'''

SELECT_URL_TABLE = '''
SELECT *
FROM urls;
'''

