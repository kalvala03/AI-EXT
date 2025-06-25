from collections import deque

def tsp_bfs(g):
    n, dq = len(g), deque([([0], 0)])
    min_cost, opt_path = float('inf'), []

    print("Path Traversal:")
    while dq:
        p, c = dq.popleft()
        print(f"Current Path: {p}, Current Cost: {c}")
        if len(p) == n and p[0] == 0:
            tc = c + g[p[-1]][0]
            if tc < min_cost: min_cost, opt_path = tc, p + [0]
            continue
        dq.extend((p + [i], c + g[p[-1]][i]) for i in range(n) if i not in p)

    return min_cost, opt_path

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

c, p = tsp_bfs(graph)
print("\nOptimal Solution:")
print(f"Minimum cost: {c}")
print(f"Optimal path: {p}")
