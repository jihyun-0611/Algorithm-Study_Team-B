# 카드 합체 놀이 : https://www.acmicpc.net/problem/15903
# 카드 n장 : a[i]
# 1. a[x] + a[y]
# 2. a[x], a[y] = a[x] + a[y]
# 3. 1-2를 m번 반복 -> sum(a) = score 
# min score 구하기

n, m = map(int, input().split())
a = list(map(int, input().split()))

cur = a
for i in range(m):
    cur = sorted(cur)
    cur[0], cur[1] = cur[0] + cur[1], cur[0] + cur[1]
    
print(sum(cur))