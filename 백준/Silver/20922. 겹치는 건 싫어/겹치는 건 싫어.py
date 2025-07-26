N, K = map(int, input().split())
numbers = list(map(int, input().split()))

from collections import defaultdict

count = defaultdict(int)  
left = 0
max_len = 0

for right in range(N):
    count[numbers[right]] += 1

    while count[numbers[right]] > K:
        count[numbers[left]] -= 1
        left += 1

    max_len = max(max_len, right - left + 1)

print(max_len)
