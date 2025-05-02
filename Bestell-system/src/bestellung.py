from datetime import datetime
from sqlite3 import Connection


def create_table(conn: Connection):
    query = """
    CREATE TABLE IF NOT EXISTS "bestellung" (
        "id"	INTEGER NOT NULL,
        "datum"	TEXT NOT NULL,
        "name"	TEXT,
        PRIMARY KEY("id" AUTOINCREMENT)
    )
    """
    cursor = conn.cursor()
    cursor.execute(query)
    cursor.close()
    conn.commit()


def read_all_bestellungen(conn: Connection) -> list[tuple]:
    query = """
    SELECT * FROM bestellung;
    """

    cursor = conn.cursor()
    cursor.execute(query)
    bestellungen = cursor.fetchall()
    cursor.close()
    return bestellungen


def create_bestellung(conn: Connection, name) -> int:
    """
    :param conn: Verbindung zur Datenbank
    :param name: Name des Bestellers
    :return: Id der erstellten Bestellung
    """
    query = """
    INSERT INTO bestellung(datum, name)
    VALUES ("%s", "%s");
    """

    datum = datetime.now().isoformat(sep='T', timespec='milliseconds')
    execute_query = query % (datum, name)
    cursor = conn.cursor()
    cursor.execute(execute_query)
    bestellung_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    return bestellung_id


def read_bestellung(conn: Connection, bestellung_id: int) -> tuple:
    query = """
    SELECT * FROM bestellung WHERE id = %s;
    """
    execute_query = query % bestellung_id
    cursor = conn.cursor()
    cursor.execute(execute_query)
    bestellung = cursor.fetchone()
    cursor.close()
    return bestellung


def update_bestellung(conn: Connection, bestellung_id: int, name: str):
    query = """
    UPDATE bestellung
    SET name = "%s"
    WHERE id = %s;
    """
    execute_query = query % (name, bestellung_id)
    cursor = conn.cursor()
    cursor.execute(execute_query)
    bestellung = cursor.fetchone()
    cursor.close()
    return bestellung


def delete_bestellung(conn: Connection, bestellung_id: int):
    query = """
    DELETE
    FROM bestellung
    WHERE id = %s;
    """
    execute_query = query % bestellung_id
    cursor = conn.cursor()
    cursor.execute(execute_query)
    bestellung = cursor.fetchone()
    cursor.close()
    return bestellung
