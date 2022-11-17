import sqlite3


def data_sql(in, product_name, price, phone, description, product_url):
    connect = sqlite3.connect("base.db")
    cursor = connect.cursor()
    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {today}(Name text, product_name text, price integer, phone text, description text, url text) ")
    cursor.execute(
        f"INSERT INTO {today} VALUES ('{name}', '{product_name}', '{price}', '{phone}', '{description}', '{product_url}')")
    connect.commit()
    connect.close()