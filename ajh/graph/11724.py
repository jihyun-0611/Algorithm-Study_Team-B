# https://www.acmicpc.net/problem/11724
# 연결 요소 (Connected Component)
# : 
from collections import deque
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
grp = {}
for e in edges:
    if e[0] not in grp:
        grp[e[0]] = []
    if e[1] not in grp:
        grp[e[1]] = []
    grp[e[0]].append(e[1])
    grp[e[1]].append(e[0])


cnt = 0
visited = []


for i in range(1, n+1):
    q = deque()
    q.append(i)
    if i not in visited:
        cnt += 1
        visited.append(i)
        while q:
            cur = q.popleft()
            if cur not in grp: # 연결된 엣지가 없는경우 고려
                break
            for v in grp[cur]:
                if v not in visited:
                    q.append(v)
                    visited.append(v)

print(cnt)

