from collections import Counter
def solution(k, tangerine):
    
    t_count = Counter(tangerine)
    answer = 0
    answer1 = []
    
    t_count = sorted(t_count.items(), key=lambda x: x[1], reverse=True)
    
    for i in t_count:
        answer += i[1]
        answer1.append(i[0])
        if answer >= k :
            return len(answer1)