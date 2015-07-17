from hist import Histogram
import matplotlib.pyplot as plt


servers = {
    "apache": "Apache",
    "nginx": "nginx",
    "iis": "IIS",
    "lighttpd": "lighttpd"
}
h = Histogram()

with open("result.txt", "r") as f:
    lines = f.read().split("\n")

    for line in lines:
        for server in servers:
            if server in line.lower():
                count = line.split(":")[1]
                count = int(count)

                for _ in range(count):
                    h.add(servers[server])

h = h.get_dict()
print(h)
keys = list(h.keys())
values = list(h.values())

X = list(range(len(keys))) 

plt.bar(X, list(h.values()), align="center")
plt.xticks(X, keys)

plt.title(".bg servers")
plt.xlabel("Server")
plt.ylabel("Count")

plt.savefig("histogram.png")
