from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = {(0, 0): 0}
q = deque()
q.append((0, 0, 1))

ans = 0
while q:
    cx, cy, cnt = q.popleft()
    if cx == N-1 and cy == M-1:
        ans = cnt
        break

    for i in range(4):
        nx, ny = cx+dx[i], cy+dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if (nx, ny) not in visited and graph[nx][ny] == 1:
            visited[(nx, ny)] = 1
            q.append((nx, ny, cnt+1))

print(ans)