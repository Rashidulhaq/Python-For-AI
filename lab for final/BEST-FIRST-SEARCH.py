from queue import PriorityQueue
v = 14
graph = [[] for i in range(v)]

def best_first_search(actual_Src, target, n):
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, actual_Src))
    visited[actual_Src] = True

    while pq.empty() == False:
        u = pq.get()[1]
        # Displaying the path having lowest cost
        print(u, end=" ")
        if u == target:
            break

        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))
    print()


# Function for adding edges to graph


def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))


# The nodes shown in above example(by alphabets) are
# implemented using integers addedge(x,y,cost);
addedge('A', 1, 3)
addedge('B', 2, 6)
addedge('C', 3, 5)
addedge('D', 4, 9)
addedge('E', 5, 8)
addedge('F', 6, 12)


source = 'A'
target = 'F'
best_first_search(source, target, v)

# This code is contributed by Jyotheeswar Ganne
