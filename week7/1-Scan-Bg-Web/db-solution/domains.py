class Domains:
    
    GET_UNVISITED_DOMAINS_SQL = """
        SELECT domain_id, domain
        FROM Domains
        WHERE visited = 0
    """


    @classmethod
    def get_all_unvisited_domains(cls, conn):
        cursor = conn.cursor()
        
        result = cursor.execute(cls.GET_UNVISITED_DOMAINS_SQL)

        return result.fetchmany()
        
