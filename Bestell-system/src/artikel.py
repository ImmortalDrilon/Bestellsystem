from sqlite3 import Connection


def create_table(conn: Connection):
    query = """
    CREATE TABLE IF NOT EXISTS "artikel" (
        "id"	INTEGER NOT NULL,
        "name"	TEXT NOT NULL UNIQUE,
        "preis"	REAL NOT NULL,
        "mwst"	REAL NOT NULL DEFAULT 0.19,
        PRIMARY KEY("id" AUTOINCREMENT)
    )
    """
    cursor = conn.cursor()
    cursor.execute(query)
    cursor.close()
    conn.commit()


def initialize_table(conn: Connection):
    query = """
    INSERT INTO "main"."artikel" ("id", "name", "preis", "mwst") VALUES ('2', 'Kaffee', '2.5', '0.19');
    INSERT INTO "main"."artikel" ("id", "name", "preis", "mwst") VALUES ('3', 'Tee', '2.0', '0.19');
    INSERT INTO "main"."artikel" ("id", "name", "preis", "mwst") VALUES ('4', 'Kuchen', '3.0', '0.19');
    INSERT INTO "main"."artikel" ("id", "name", "preis", "mwst") VALUES ('5', 'Apfel', '1.5', '0.19');
    INSERT INTO "main"."artikel" ("id", "name", "preis", "mwst") VALUES ('6', 'Kekse', '0.5', '0.19');
    INSERT INTO "main"."artikel" ("id", "name", "preis", "mwst") VALUES ('7', 'Krombacher 0.3', '3.0', '0.19');
    INSERT INTO "main"."artikel" ("id", "name", "preis", "mwst") VALUES ('8', 'Krombacher 0.5', '6.0', '0.19');
    """
    cursor = conn.cursor()
    cursor.executescript(query)
    cursor.close()
    conn.commit()


def read_all_artikel(conn: Connection) -> list[tuple]:
    query = """
    SELECT *
    FROM artikel
    """
    cursor = conn.cursor()
    cursor.execute(query)
    artikel = cursor.fetchall()
    cursor.close()
    return artikel


def read_artikel(conn: Connection, artikel_id: int):
    query = """
    SELECT *
    FROM artikel
    WHERE id = %s
    """
    execute_query = query % artikel_id
    cursor = conn.cursor()
    cursor.execute(execute_query)
    artikel = cursor.fetchone()
    cursor.close()
    return artikel


def read_artikel_by_name(conn: Connection, artikel_name: str) -> tuple:
    """
    :param conn: Verbindung zur Datenbank
    :param artikel_name: Name des Artikels
    :return: Datenbank Eintrag des Artikels
    """
    query = """
    SELECT *
    FROM artikel
    WHERE name = "%s"
    """
    execute_query = query % artikel_name
    cursor = conn.cursor()
    cursor.execute(execute_query)
    artikel = cursor.fetchone()
    cursor.close()
    return artikel
