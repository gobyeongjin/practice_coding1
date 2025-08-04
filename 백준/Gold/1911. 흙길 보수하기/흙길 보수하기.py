import sys
input = sys.stdin.readline

N, L = map(int, input().split())

pool = [tuple(map(int,input().split())) for _ in range(N)]
pool.sort()

cur = 0
ans = 0

for st, end in pool:
    if cur < st:
        cur = st
    
    if cur >= end:
        continue

    diff = end - cur
    count = (diff + L-1)//L
    ans += count
    cur += count * L

print(ans)