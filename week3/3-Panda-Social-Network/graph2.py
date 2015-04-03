graph = {
    "1": ["2", "3", "4"],
    "2": ["1", "4"],
    "3": ["1","4"],
    "4": ["1", "2", "5","3"],
    "5": ["4"]
}

def bfs(graph, start, end):
    visited = set()
    previous_path = {}
    queue = []
    found = False
    path = 0
    
    previous_path[start] = None
    queue.append(start)
    visited.add(start)

    while len(queue) != 0:
        current_node = queue.pop(0)

        if current_node == end:
            found = True
            break
        
        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                previous_path[neighbour] = current_node
                queue.append(neighbour)
    
    if found:
        x = end
        print(x)
        while previous_path[x] is not None:
            x = previous_path[x]
            print(x)
            path += 1


    return path
            

print(bfs(graph,"3", "5"))
