import configparser
import sqlite3

def cursor_execute(query):
    config = configparser.ConfigParser()
    config.read('config.ini')

    conn = sqlite3.connect(config['DB']['db_name'])
    results = []

    try:
        cursor = conn.cursor()
        cursor.execute(query)
        if 'SELECT' in query[0:10]:
            results = cursor.fetchall()
    finally:
        conn.commit()
        cursor.close()
        conn.close()

    return results

