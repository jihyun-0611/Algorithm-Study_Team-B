# 15900 나무 탈출
# 트리 : 1번 - 루트 
# 말 -> 부모노드로옮김 : 한 노드에 여러말 가능
# 말이 루트노드에 도착시 제거 
# 게임말이 게임판에 존재하지 않아 고를수 없는 경우 진다.
# 성원이가 먼저 
# 성원이가 이기는 경우 yes ()
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# n = int(input())

# grp = [[] for _ in range(n+1)]
# for e in range(n-1):
#     x, y = map(int, input().split())
#     grp[x].append(y)
#     grp[y].append(x)

# visited = [0 for _ in range(n+1)]
# distance = [0 for _ in range(n+1)]

# def dfs(cur):
#     visited[cur] = 1
#     for v in grp[cur]:
#         if visited[v] == 0:
#             distance[v] = distance[cur]+1
#             dfs(v)


# # 루트 노드가 1이므로 항상 1부터 시작
# dfs(1)

# answer = 0
# for i in range(1, n+1):
#     if len(grp[i]) == 1:
#         answer += distance[i]

# if answer % 2 == 0:
#     print('No')
# else:
#     print('Yes')

#=> 시간초과

import sys
input = sys.stdin.readline

n = int(input())

grp = [[] for _ in range(n+1)]
for e in range(n-1):
    x, y = map(int, input().split())
    grp[x].append(y)
    grp[y].append(x)

visited = [0 for _ in range(n+1)]
distance = [0 for _ in range(n+1)]

stack = [(1, 0)]

while stack:
    v, d = stack.pop()
    visited[v] = 1
    for nxt in grp[v]:
        if visited[nxt] == 0:
            distance[nxt] = distance[v] + 1
            stack.append((nxt, d+1))

answer = 0
for i in range(1, n+1):
    if len(grp[i]) == 1:
        answer += distance[i]

if answer % 2 == 0:
    print('No')
else:
    print('Yes')

# 파이썬을 사용했을 때 재귀 함수에서 RecursionError 발생 시 스택으로 구현할것. 