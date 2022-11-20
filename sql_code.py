import sqlite3
from datetime import datetime
def add_stiuation(lokatsion, situation):
    connect = sqlite3.connect("base.db")
    cursor = connect.cursor()
    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS parking (lokatsion integer, situation integer) " )

    data = cursor.execute(
        f"SELECT * FROM parking WHERE lokatsion={lokatsion}")
    iff = bool( data.fetchall() )
    if iff:
        cursor.execute(
            f"UPDATE  parking SET  situation={situation} where lokatsion={lokatsion}")
    else:
        cursor.execute(
            f"INSERT INTO parking VALUES ('{lokatsion}', '{situation}')")
    connect.commit()
    cursor.close()
    connect.close()

# kiritilgan lakatsiya boyicha joy boshligini tekshiradi
def get_stiuation():
    connect = sqlite3.connect("base.db")
    cursor = connect.cursor()
    data = cursor.execute(
        f"SELECT * FROM parking")
    result = data.fetchall()
    connect.close()
    for x in result:
        if x[1] == 0:
            return x[0]
    connect.close()
    return "Bosh joy yoq"

def get_all():
    connect = sqlite3.connect("base.db")
    cursor = connect.cursor()
    data_sql = cursor.execute(
        f"SELECT * FROM parking")
    data = data_sql.fetchall()
    connect.close()
    band = 0
    bosh = 0
    for x in data:
        if x[1] == 1:
            band += 1
        if x[1] == 0:
            bosh += 1
    return band, bosh


def add_car_number(number):
    connect = sqlite3.connect("base.db")
    cursor = connect.cursor()
    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS car (number text, date DATE)" )
    now = datetime.now()
    cursor.execute(
            f"INSERT INTO car VALUES ('{number}', '{now}')")
    connect.commit()
    cursor.close()
    connect.close()

def get_car_number(number):
    connect = sqlite3.connect("base.db")
    cursor = connect.cursor()
    now = datetime.now()
    data = cursor.execute(f"SELECT * FROM car WHERE number='{number}'")
    result = data.fetchone()
    res = datetime.strptime(result[1], '%Y-%m-%d %H:%M:%S.%f')
    res_time = now - res
    connect.close()
    return result[0], res_time
# add_car_number("01 B 111 BB")
# print( get_car_number("01 B 111 BB") )