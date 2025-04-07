from collections import deque
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n-1)]
tree = {}
for e in edges:
    if e[0] not in tree:
        tree[e[0]] = []
    if e[1] not in tree:
        tree[e[1]] = []
    tree[e[0]].append(e[1])
    tree[e[1]].append(e[0])

parents = {1: 0}
q = deque([1])
while q:
    cur = q.popleft()
    for nxt in tree[cur]:
        if nxt not in parents:
            parents[nxt] = cur
            q.append(nxt)

for i in range(2, n+1):
    print(parents[i])