import sys

N, K = map(int, sys.stdin.readline().split())

countries=[]
for _ in range(N):
    countries.append(list(map(int,sys.stdin.readline().split())))


target_country = []
for c in countries:
    if c[0] == K:
        target_country = c
        break

ans = 1
for c in countries:
    if (c[1], c[2], c[3]) > (target_country[1], target_country[2], target_country[3]):
        ans += 1

print(ans)