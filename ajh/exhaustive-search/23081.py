# 오델로 https://www.acmicpc.net/problem/23081
# 상대의 돌을 가장 많이 뒤집을 수 있는 위치
# . : 빈공간, W: 백돌, B: 흑돌(종민이)
n = int(input())
grp = [list(input()) for _ in range(n)]

dx = [1, 0, -1, 0, 1, -1, 1, -1]
dy = [0, 1, 0, -1, 1, -1, -1, 1]

memo=[0, (-1, -1)]
for i in range(n):
    for j in range(n):
        if grp[i][j] == '.':
            cnt = 0
            for k in range(8):
                # W 개수 탐색
                k_cnt = 0
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                while 0 <= nx < n and 0 <= ny < n and grp[nx][ny] == 'W':
                    k_cnt += 1
                    nx += dx[k]
                    ny += dy[k]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n: # 범위 관련 에러 처리하기 -> 여기서는 한번 범위를 벗어나면 계속 벗어나지므로 continue가 아닌 break가 맞음
                        break
                    if grp[nx][ny]=='B':
                        cnt += k_cnt
                        if memo[0] < cnt:
                            memo = [cnt, (j, i)]
                        elif memo[0] == cnt:
                            tmp = [memo[1], (j, i)]
                            tmp.sort(key=lambda x:(x[1], x[0]))
                            memo = [cnt, tmp[0]] # 리스트를 튜플로 저장해서 틀림
                        break
                        
if memo[0] == 0:
    print("PASS")       
else:
    print(*memo[1])
    print(memo[0])