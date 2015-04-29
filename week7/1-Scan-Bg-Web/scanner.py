from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
from hist import Histogram


def domain_from_url(url):
    parsed = urlparse(url)

    return parsed[0] + "://" + parsed[1]


def has_tld(url, tld):
    return domain_from_url(url).endswith(tld)


def get_html(url):
    return requests.get(url).text

REGISTER = "http://register.start.bg"
HEADERS = {
    "User-Agent": "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0"
}

visited = set()
h = Histogram()
links = [link.get("href") for link in BeautifulSoup(get_html(REGISTER)).find_all("a")]


for link in links:
    if link is not None and "link.php" in link:
        try:
            target_url = REGISTER + "/" + link
            r = requests.head(target_url, headers=HEADERS, allow_redirects=True, timeout=10)
            
            target_url = domain_from_url(r.url)
            
            if target_url not in visited:
                visited.add(target_url)

                if has_tld(target_url, ".bg"):
                    print(target_url)
                    h.add(r.headers["Server"])
        except Exception as e:
            print(e)

result = []

for server, count in h.items():
    result.append("{}: {}".format(server, count))

with open("result.txt", "w") as f:
    f.write("\n".join(result))


