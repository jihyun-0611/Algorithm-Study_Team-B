# 분해합 2231
# 245 (생성자) -> 256 (=245+2+4+5) : 분해합
# 최소 생성자 구하기 
# 1. 그냥 0부터 하나씩 탐색?
n = int(input())

ans = 0
for i in range(1, n+1):
    num = i
    res = i
    while True:
        if num // 10 <= 0:
            res += num % 10
            break
        res += num%10
        num//= 10
    if res == n:
        ans = i
        break
print(ans)