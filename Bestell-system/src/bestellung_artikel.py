from sqlite3 import Connection

def create_table(conn: Connection):
    query = """
    CREATE TABLE IF NOT EXISTS "bestellung_artikel" (
        "bestellung_id"	INTEGER NOT NULL,
        "artikel_id"	INTEGER NOT NULL,
        "artikel_anzahl"	INTEGER NOT NULL,
        PRIMARY KEY("bestellung_id","artikel_id"),
        CONSTRAINT "bestellung_artikel_pk" FOREIGN KEY("artikel_id") REFERENCES "artikel"("id"),
        CONSTRAINT "bestellung_artikel_pk" FOREIGN KEY("bestellung_id") REFERENCES "bestellung"("id")
    )
    """
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()


def read_all_bestellung_artikel(conn: Connection, bestellung_id: int) -> list[tuple]:
    query = """
    SELECT bestellung_artikel.artikel_anzahl, artikel.name, artikel.preis, artikel.mwst
    FROM bestellung_artikel
    JOIN artikel on bestellung_artikel.artikel_id = artikel.id
    WHERE bestellung_artikel.bestellung_id = %s
    """

    execute_query = query % bestellung_id
    cursor = conn.cursor()
    cursor.execute(execute_query)
    rows = cursor.fetchall()
    cursor.close()
    return rows


def create_bestellung_artikel(conn: Connection, bestellung_id: int, artikel_id: int, artikel_anzahl: int):
    query = """
    INSERT INTO "main"."bestellung_artikel"
    ("bestellung_id", "artikel_id", "artikel_anzahl")
    VALUES (%s, %s, %s);
    """
    execute_query = query % (bestellung_id, artikel_id, artikel_anzahl)
    cursor = conn.cursor()
    cursor.execute(execute_query)
    conn.commit()
    cursor.close()


def read_bestellung_artikel(conn: Connection, bestellung_id: int, artikel_id: int) -> tuple:
    query = """
    SELECT bestellung_artikel.artikel_anzahl, artikel.name, artikel.preis, artikel.mwst
    FROM bestellung_artikel
    JOIN artikel on bestellung_artikel.artikel_id = artikel.id
    WHERE bestellung_artikel.bestellung_id = %s AND bestellung_artikel.artikel_id = %s
    """
    execute_query = query % (bestellung_id, artikel_id)
    cursor = conn.cursor()
    cursor.execute(execute_query)
    bestellung_artikel = cursor.fetchone()
    cursor.close()
    return bestellung_artikel


def update_bestellung_artikel(conn: Connection, bestellung_id: int, artikel_id: int, artikel_anzahl: int):
    query = """
    UPDATE bestellung_artikel
    SET artikel_anzahl = %s
    WHERE bestellung_id = %s AND artikel_id = %s
    """
    execute_query = query % (artikel_anzahl, bestellung_id, artikel_id)
    cursor = conn.cursor()
    cursor.execute(execute_query)
    conn.commit()
    cursor.close()


def delete_bestellung_artikel(conn, bestellung_id, artikel_id):
    query = """
    DELETE
    FROM bestellung_artikel
    WHERE bestellung_id = %s AND artikel_id = %s
    """

    execute_query = query % (bestellung_id, artikel_id)
    cursor = conn.cursor()
    cursor.execute(execute_query)
    conn.commit()
    cursor.close()

def add_bestellung_artikel(conn: Connection, bestellung_id: int, artikel_id: int, artikel_anzahl: int):
    bestellung_artikel = read_bestellung_artikel(conn, bestellung_id, artikel_id)

    if bestellung_artikel:
        neue_anzahl = bestellung_artikel[0] + artikel_anzahl
        update_bestellung_artikel(conn, bestellung_id, artikel_id, neue_anzahl)
    else:
        create_bestellung_artikel(conn, bestellung_id, artikel_id, artikel_anzahl)



def subtract_bestellung_artikel(conn: Connection, bestellung_id: int, artikel_id: int, artikel_anzahl: int):
    bestellung_artikel = read_bestellung_artikel(conn, bestellung_id, artikel_id)
    if bestellung_artikel and bestellung_artikel[0] > artikel_anzahl:
        neue_anzahl = bestellung_artikel[0] - artikel_anzahl
        update_bestellung_artikel(conn, bestellung_id, artikel_id, neue_anzahl)
    else:
        delete_bestellung_artikel(conn, bestellung_id, artikel_id)