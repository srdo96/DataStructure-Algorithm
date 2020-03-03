n = int(input())  # no. of nodes
m = int(input())  # no. of edges
adjacency_list = [[] for _ in range(n)]
# here u -> v
for i in range(m):
    u = int(input())
    v = int(input())
    adjacency_list[u].append(v)  # node start from 0 -> u-1
print(adjacency_list)
time = 0


def dfs(graph):
    global time
    discovery_time = [0] * n+1
    finished_time = [0] * n+1

    for vertex_u in range(1, n+1):
        # graph[vertex_u] =
        if discovery_time[vertex_u] == 0:
            time += 1
            discovery_time[vertex_u] = time
            dfs_visit(graph, discovery_time, finished_time, vertex_u)
            time += 1
            finished_time[vertex_u] = time


def dfs_visit(graph, discovery_time, finished_time, vertex_u):
    global time
    length = len(graph[vertex_u])
    for index in range(length):
        vertex_v = graph[vertex_u][index]
        if discovery_time[vertex_v] == 0:
            time += 1
            discovery_time[vertex_v] = time
            dfs_visit(graph, discovery_time, finished_time, vertex_v)
        time += 1
        finished_time[vertex_v] = time
