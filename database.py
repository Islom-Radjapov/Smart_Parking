import sqlite3

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

def get_stiuation(lokatsion):
    connect = sqlite3.connect("base.db")
    cursor = connect.cursor()
    data = cursor.execute(
        f"SELECT situation FROM parking WHERE lokatsion={lokatsion}")
    return data.fetchall()[0][0]

def get_all():
    connect = sqlite3.connect("base.db")
    cursor = connect.cursor()
    data = cursor.execute(
        f"SELECT * FROM parking").fetchall()
    band = 0
    bosh = 0
    for x in data:
        if x[1] == 1:
            band += 1
        if x[1] == 0:
            bosh += 1
    return band, bosh
# print( get_stiuation(17) )
# print( get_all() )