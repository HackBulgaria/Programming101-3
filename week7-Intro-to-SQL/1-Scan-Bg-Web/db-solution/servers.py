class Servers:
    INSERT_SERVER_SQL = """
        INSERT INTO Servers(link_id, url, server_string)
        VALUES(?, ?, ?)
    """

    @classmethod
    def insert_server(cls, conn, link_id, url, server_string):
        cursor = conn.cursor()

        cursor.execute(INSERT_SERVER_SQL, (link_id, url, server_string))
