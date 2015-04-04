import json

graph = {
    "1": ["2", "3", "5"],
    "2": ["4", "1"],
    "3": ["1", "6"],
    "4": ["2", "5", "6"],
    "5": ["4", "1"],
    "6": ["3", "4", "7"],
    "7": ["6", "8"],
    "8": ["7", "9"],
    "9": ["8", "10"],
    "10": ["9"],
    "11": ["12"],
    "12": ["11"]
}


def bfs(graph, start, end):
    visited = set()
    queue = []
    # path_to[x] = y
    # if we go to x through y
    path_to = {}

    queue.append(start)
    visited.add(start)
    path_to[start] = None
    found = False
    path_length = 0

    while len(queue) != 0:
        current_node = queue.pop(0)
        if current_node == end:
            found = True
            break

        for neighbour in graph[current_node]:
            if neighbour not in visited:
                path_to[neighbour] = current_node
                visited.add(neighbour)
                queue.append(neighbour)

    if found:
        while path_to[end] is not None:
            path_length += 1
            end = path_to[end]

    print(json.dumps(path_to, sort_keys=True, indent=4))
    return path_length

result = bfs(graph, "1", "10")
print(result)
