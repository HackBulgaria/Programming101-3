import sqlite3
import sys
import requests
import time


from domains import Domains
from links import Links
from servers import Servers



if len(sys.argv) <= 1:
    print("Provide database file")
    print("python3.4 collector.py crawler.db")
    sys.exit(1)

db = sys.argv[1]

conn = sqlite3.connect(db)
conn.row_factory = sqlite3.Row


def head_for_server(domain, url):
    target_url = domain + "/" + url
    print(target_url)
    headers = {}
    r = requests.head(target_url, 
                      headers=headers, 
                      allow_redirects=True, 
                      timeout=10)         

    return {
        "url": r.url,
        "headers": r.headers
    }

while True:
    unvisited_links = Links.get_unvisited_links(conn)
    
    if len(unvisited_links) == 0:
        print("Nothing to crawl, going to sleep")
        time.sleep(5)
        continue

    for link in unvisited_links:
        print("Going to {}".format(link["url"]))
        try:
            result = head_for_server(link["domain"], link["url"]) 
            print("Got result for {}. It is {}".format(link["url"], result["url"])) 
            Servers.insert_server(conn, link["link_id"], result["url"], result["headers"]["Server"])
        except:
            pass
    
    conn.commit()

