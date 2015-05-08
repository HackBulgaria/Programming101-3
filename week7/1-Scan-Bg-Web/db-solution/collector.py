import sqlite3
import sys
from bs4 import BeautifulSoup
import requests


from domains import Domains
from links import Links


if len(sys.argv) <= 1:
    print("Provide database file")
    print("python3.4 collector.py crawler.db")
    sys.exit(1)

db = sys.argv[1]

conn = sqlite3.connect(db)
conn.row_factory = sqlite3.Row


def collect_domain(domain):
    inbound = set()
    outbound = set()
    others = set()

    print("Visiting {}".format(domain))

    r = requests.get(domain)
    soup = BeautifulSoup(r.text)

    for link in soup.find_all("a"):
        href = link.get("href")
        
        if href is None:
            continue

        if "start.bg" in href and "javascript:" not in href:
            inbound.add(href)
        elif "link.php" in href:
            outbound.add(href)
        else:
            others.add(href)

    return {
        "inbound": inbound,
        "outbound": outbound,
        "others": others
    }


while True:
    domains_to_visit = Domains.get_all_unvisited_domains(conn)  
    
    if len(domains_to_visit) == 0:
        break

    for domain_row in domains_to_visit:
        result = collect_domain(domain_row["domain"])
    
    domain_id = domain_row["domain_id"]
    
    Domains.visit_domain(conn, domain_id)
    Domains.insert_domains(conn, result["inbound"])
    Links.insert_links(conn, result["outbound"], domain_id)

