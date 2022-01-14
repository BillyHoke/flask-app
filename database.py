import psycopg2
from psycopg2.extras import DictCursor


def sql_select(query, params):
    conn = psycopg2.connect("dbname=project_2")
    cur = conn.cursor(cursor_factory=DictCursor)
    cur.execute(query, params)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results


def sql_write(query, params):
    conn = psycopg2.connect("dbname=project_2")
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    cur.close()
    conn.close()
