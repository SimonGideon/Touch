from collections import deque
d = deque([1, 2, 3])
p =  d.popleft()
print(p)

d.append(5)
print(d)
# Creating empty deque
d1 = deque()
# limiting deque size
d = deque(maxlen=3)
d.append(1)
d.append(2)
d.append(3)
d.append(4)
print(d)

# Breadth First Search
def bfs(graph, root):
    distances = {}
    distances[root] = 0
    q = deque([root])
    while q:
        current = q.popleft()
        for neighbor in graph[current]:
            distances[neighbor] = distances[current] + 1
            q.append(neighbor)
    return distances
graph = {1:[2,3], 2:[4], 3:[4,5], 4:[3,5], 5:[]}

print(bfs(graph, 1))