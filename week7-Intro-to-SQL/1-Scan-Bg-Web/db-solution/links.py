class Links:

    INSERT_LINK_SQL = """
        INSERT INTO Links(url, domain_id)
        VALUES(?, ?)
    """
    
    UNVISITED_LINKS_SQL = """
        SELECT link_id, url, links.domain_id, domain
        FROM links
        JOIN domains
                ON links.domain_id = domains.domain_id
        WHERE link_id NOT IN (
                SELECT link_id FROM Servers
        );
    """

    @classmethod
    def get_unvisited_links(cls, conn):
        cursor = conn.cursor()
        result = cursor.execute(cls.UNVISITED_LINKS_SQL)
        
        return result.fetchall()

    @classmethod
    def insert_links(cls, conn, links, domain_id):
        try:
            for link in links:
                cursor = conn.cursor()
                cursor.execute(cls.INSERT_LINK_SQL, (link, domain_id))
            conn.commit()
        except:
            pass
