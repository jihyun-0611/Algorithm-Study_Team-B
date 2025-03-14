# 설탕 배달 https://www.acmicpc.net/problem/2839
# 3kg, 5kg 봉투
n = int(input())
cur_val, cur_cnt = n, 0

while cur_val >= 0:
    if cur_val % 5 == 0:
        print(cur_cnt + (cur_val // 5))
        break
    cur_val -= 3
    cur_cnt += 1

else:
    print(-1)
