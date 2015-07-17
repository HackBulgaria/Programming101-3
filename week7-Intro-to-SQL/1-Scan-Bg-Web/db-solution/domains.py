class Domains:
    
    GET_UNVISITED_DOMAINS_SQL = """
        SELECT domain_id, domain
        FROM Domains
        WHERE visited = 0
    """
    
    INSERT_DOMAIN_SQL = """
        INSERT INTO Domains(domain, visited)
        VALUES(?, ?)
    """

    VISIT_DOMAIN_SQL = """
        UPDATE Domains
        SET visited = 1
        WHERE domain_id = ?
    """


    @classmethod
    def insert_domains(cls, conn, domains):
        try:
            cursor = conn.cursor()

            for domain in domains:
                cursor.execute(cls.INSERT_DOMAIN_SQL, (domain, 0))

            conn.commit()
        except:
           pass
    
    @classmethod
    def visit_domain(cls, conn, domain_id):
        cursor = conn.cursor()

        cursor.execute(cls.VISIT_DOMAIN_SQL, (domain_id, ))

        conn.commit()

    @classmethod
    def get_all_unvisited_domains(cls, conn):
        cursor = conn.cursor()
        
        result = cursor.execute(cls.GET_UNVISITED_DOMAINS_SQL)

        return result.fetchmany()
        
