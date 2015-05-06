import sqlite3
import sys
from domains import Domains


if len(sys.argv) <= 1:
    print("Provide database file")
    print("python3.4 collector.py crawler.db")
    sys.exit(1)

db = sys.argv[1]

conn = sqlite3.connect(db)
conn.row_factory = sqlite3.Row

domains_to_visit = Domains.get_all_unvisited_domains(conn)

for domain_row in domains_to_visit:
    print(domain_row["domain"])










