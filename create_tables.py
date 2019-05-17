import psycopg2

from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    create and connect to database `sparkify` to be used in ETL process.
    :return: cursor and connection instances.
    """

    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()

    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    return cur, conn


def drop_tables(cur, conn):
    """
    drop tables.
    iterate through the list of `drop table` queries and drop tables one by one.
    :param cur: cursor instance.
    :param conn: connection instance.
    :return: None.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    create tables.
    iterate though a list of `create table` queries and execute them.
    :param cur: cursor instance.
    :param conn: connection instance.
    :return: None.
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    main function to be executed on running this file.
    :return: None.
    """
    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
