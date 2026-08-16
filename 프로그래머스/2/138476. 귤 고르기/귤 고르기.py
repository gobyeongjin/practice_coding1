from collections import Counter
def solution(k, tangerine):
    answer = 0
    count = 0
    
    t_count = sorted(Counter(tangerine).values(), reverse=True)
    
    for i in t_count:
        answer += i
        count += 1
        if answer >= k:
            return count
            
    