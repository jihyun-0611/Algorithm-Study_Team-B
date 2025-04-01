# 체스판 다시 칠하기 1018
# 첫번째 칸이 W or B로 정해진 순간 나머지칸의 색은 이미 정해짐
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]


cnt = n*m # 만약 cnt가 n or m이었다면 grid에서 세는 바꿔야할 최소값보다 작을 가능성이 있다;; 초기값을 뭘줘야할지 잘생각해보기
for c in ['W', 'B']:
    grid = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == 0 and board[i][j] != c:
                grid[i][j] = 1
            elif (i + j) % 2 == 1 and board[i][j] == c:
                grid[i][j] = 1
    for i in range(7, n):
        for j in range(7, m):
            tmp = 0
            for k in range(i-7, i+1):
                tmp += sum(grid[k][j-7:j+1])
            cnt = min(tmp, cnt)

print(cnt)



