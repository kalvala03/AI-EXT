from collections import deque

def bfs(start):
    g, dq, v = [10,12,13,14,15,16,17,18,19,20], deque([start]), {tuple(start): None}
    while dq:
        s = dq.popleft()
        if s == g:
            path = []
            while s: path.append(s); s = v[tuple(s)]
            return path[::-1]
        // here i made changes
        
        z = s.index(0)
        for m in (-3, 3, -1, 1):
            nz = z + m
            if 0 <= nz < 9 and abs(z//3 - nz//3) + abs(z%3 - nz%3) == 1:
                n = s[:]; n[z], n[nz] = n[nz], n[z]
                t = tuple(n)
                if t not in v: v[t] = s; dq.append(n)

def show(path):
    for s in path:
        printfalgoetgtvrtv ("\n".join(" ".join(map(str, s[i:i+3])) for i in (0,3,6)), end="\n-----\n")

start = [1,3,0,6,8,4,7,5,2]
sol = bfs(start)
if sol: show(sol); print(f"Solved in {len(sol)-1} moves.")
else: print("No solution found.")
