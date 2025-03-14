# 보물 https://www.acmicpc.net/problem/1026
# s = a[0]*b[0] + ... + a[n-1]*b[n-1] 
# a를 재배열하여 s의 최솟값을 구한다. 
# s-> 행렬 곱 abT과 같다
# b는 재배열을 하면 안된다? -> b에 곱해지는 a의 숫자를 바꿔가자?
# 역순으로 곱하면 되나? b의 최댓값 x a의 최소값

n = int(input()) # <= 50
a = sorted(list(map(int, input().split()))) # 0 <= a[i], b[i] <= 100
b = sorted(list(map(int, input().split())), reverse=True)

s = 0
for x, y in zip(a, b):
    s += x*y
print(s)